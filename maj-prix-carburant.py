#!/usr/bin/env python3
"""
=============================================================
  économie-carburant.fr — Script Auto-MAJ
  Barèmes IK 2026–2030 + Prix carburant France
  Exécuté 1×/semaine (cron : 0 3 * * 0)
  Auteur : économie-carburant.fr
  Version : 2.0 — Mai 2026
=============================================================
"""

import requests
import json
import logging
import sys
import os
from datetime import datetime
from pathlib import Path

# ── CONFIG ──────────────────────────────────────────────────
BASE_DIR  = Path('/var/www/economie-carburant.fr')
DATA_DIR  = BASE_DIR / 'data'
LOG_DIR   = Path('/var/log/economie-carburant')
LOG_FILE  = LOG_DIR / 'updates.log'
ERR_FILE  = LOG_DIR / 'errors.log'
DATA_FILE = DATA_DIR / 'baremes-fiscaux.json'

# Assure la création des dossiers
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# ── LOGGING ─────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Error file séparé
err_handler = logging.FileHandler(ERR_FILE, encoding='utf-8')
err_handler.setLevel(logging.ERROR)
err_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logging.getLogger().addHandler(err_handler)

logger = logging.getLogger(__name__)


# ── BARÈME IK OFFICIEL 2026 ──────────────────────────────────
BAREME_BASE_2026 = {
    "3CV": {"d5000": 0.529, "coeff": 0.316, "intercept": 1065, "d20000": 0.370},
    "4CV": {"d5000": 0.596, "coeff": 0.356, "intercept": 1200, "d20000": 0.414},
    "5CV": {"d5000": 0.636, "coeff": 0.378, "intercept": 1290, "d20000": 0.440},
    "6CV": {"d5000": 0.665, "coeff": 0.396, "intercept": 1340, "d20000": 0.458},
    "7CV": {"d5000": 0.697, "coeff": 0.413, "intercept": 1420, "d20000": 0.478},
    "ve_majoration": 1.20,
    "source": "service-public.gouv.fr",
    "officiel": True,
}

# Prix carburant de fallback (mis à jour manuellement si scraper échoue)
PRIX_FALLBACK = {
    "SP95": 2.06,
    "SP98": 2.10,
    "E10":  2.00,
    "Diesel": 2.33,
    "E85":  0.84,
    "GPL":  1.05,
    "source": "fallback_statique",
    "last_update": datetime.now().isoformat()
}


def fetch_prix_carburant() -> dict:
    """
    Tente de récupérer les prix carburant depuis l'API gouvernementale.
    Retourne les prix statiques en cas d'échec.
    """
    urls = [
        "https://prix-carburants.gouv.fr/api/prix-moyens",
        "https://data.economie.gouv.fr/api/records/1.0/search/?dataset=prix_des_carburants_en_france_flux_instantane_v2&rows=1",
    ]

    for url in urls:
        try:
            resp = requests.get(
                url,
                headers={"User-Agent": "EconomieCarburant-Bot/2.0 (contact@economie-carburant.fr)"},
                timeout=15
            )
            resp.raise_for_status()

            # Essai de parse JSON
            data = resp.json()
            logger.info(f"Prix carburant récupérés depuis {url}")

            # L'API peut retourner différentes structures — on valide et normalise
            prix = _normalize_prix(data)
            if prix:
                prix["source"] = url
                prix["last_update"] = datetime.now().isoformat()
                logger.info(f"Prix normalisés : {prix}")
                return prix

        except requests.Timeout:
            logger.warning(f"Timeout sur {url}")
        except requests.HTTPError as e:
            logger.warning(f"HTTP {e.response.status_code} sur {url}")
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            logger.warning(f"Parse error sur {url} : {e}")
        except Exception as e:
            logger.error(f"Erreur inattendue sur {url} : {e}")

    # Tous les endpoints ont échoué → fallback statique
    logger.warning("Tous les endpoints carburant ont échoué → utilisation des prix statiques")
    return PRIX_FALLBACK.copy()


def _normalize_prix(data) -> dict | None:
    """Normalise les différentes structures possibles de l'API."""
    # Si c'est un dict avec des clés directes
    expected_keys = {"SP95", "SP98", "Diesel", "E85"}
    if isinstance(data, dict) and expected_keys.issubset(data.keys()):
        return {k: float(v) for k, v in data.items() if k in expected_keys | {"E10", "GPL"}}

    # Fallback : on ne peut pas parser → retourne None
    return None


def generate_baremes_multi_annuels() -> dict:
    """
    Génère les barèmes IK 2026–2030 à partir du barème officiel 2026.
    Revalorisation : +2,5%/an (inflation prévue).
    Le barème 2026 est officiel ; 2027–2030 sont des estimations.
    """
    baremes = {}
    inflation = 0.025  # +2,5% par an

    for annee in range(2026, 2031):
        facteur = (1 + inflation) ** (annee - 2026)
        est = annee > 2026  # estimation si pas 2026

        baremes[str(annee)] = {
            "officiel": not est,
            "estimation": est,
            "facteur_revalorisation": round(facteur, 4),
            "source": "service-public.gouv.fr" if not est else "estimation +2.5%/an",
        }

        for cv_key in ["3CV", "4CV", "5CV", "6CV", "7CV"]:
            base = BAREME_BASE_2026[cv_key]
            baremes[str(annee)][cv_key] = {
                "d5000":     round(base["d5000"]     * facteur, 4),
                "coeff":     round(base["coeff"]     * facteur, 4),
                "intercept": round(base["intercept"] * facteur, 0),
                "d20000":    round(base["d20000"]    * facteur, 4),
            }

        baremes[str(annee)]["ve_majoration"] = BAREME_BASE_2026["ve_majoration"]

    logger.info(f"Barèmes générés pour les années : {list(baremes.keys())}")
    return baremes


def calculer_ik(km: float, cv: str, annee: str, electrique: bool = False, baremes: dict = None) -> float:
    """
    Calcule les indemnités kilométriques.
    Utile pour valider les barèmes générés.
    """
    if baremes is None:
        baremes = generate_baremes_multi_annuels()

    b = baremes.get(annee, {}).get(cv, {})
    if not b:
        raise ValueError(f"Barème non trouvé : {annee}/{cv}")

    if km <= 5000:
        ik = km * b["d5000"]
    elif km <= 20000:
        ik = km * b["coeff"] + b["intercept"]
    else:
        ik = km * b["d20000"]

    if electrique:
        ik *= baremes[annee].get("ve_majoration", 1.20)

    return round(ik, 2)


def valider_baremes(baremes: dict) -> bool:
    """Valide que les barèmes générés sont cohérents."""
    errors = []

    # Test référence : 15 000 km, 5 CV, 2026 = (15000 × 0.378) + 1290 = 6960
    ik_ref = calculer_ik(15000, "5CV", "2026", baremes=baremes)
    expected = (15000 * 0.378) + 1290  # = 6960
    if abs(ik_ref - expected) > 1:
        errors.append(f"Barème 2026 incorrect : attendu ~{expected}, obtenu {ik_ref}")

    # Vérifie que chaque année augmente
    for cv in ["3CV", "5CV", "7CV"]:
        prev = None
        for annee in ["2026", "2027", "2028", "2029", "2030"]:
            curr = baremes[annee][cv]["d5000"]
            if prev is not None and curr <= prev:
                errors.append(f"{cv}/{annee}: taux {curr} pas supérieur à {prev}")
            prev = curr

    if errors:
        for err in errors:
            logger.error(f"[VALIDATION] {err}")
        return False

    logger.info("[VALIDATION] Barèmes valides ✓")
    return True


def main():
    """Point d'entrée principal."""
    logger.info("=" * 60)
    logger.info("=== DÉMARRAGE MAJ AUTO === économie-carburant.fr ===")
    logger.info(f"=== Heure : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    logger.info("=" * 60)

    try:
        # 1. Prix carburant
        logger.info("→ Étape 1 : Récupération prix carburant...")
        prix = fetch_prix_carburant()

        # 2. Barèmes multi-annuels
        logger.info("→ Étape 2 : Génération barèmes IK 2026–2030...")
        baremes = generate_baremes_multi_annuels()

        # 3. Validation
        logger.info("→ Étape 3 : Validation barèmes...")
        if not valider_baremes(baremes):
            logger.error("Validation échouée — arrêt, fichier non écrasé")
            sys.exit(1)

        # 4. Assemblage JSON final
        data = {
            "meta": {
                "site": "economie-carburant.fr",
                "generated_at": datetime.now().isoformat(),
                "version": "2.0",
                "description": "Barèmes IK 2026–2030 + Prix carburant France",
            },
            "prix_carburants": prix,
            "baremes_ik": baremes,
        }

        # 5. Écriture atomique (via fichier temp)
        tmp_file = DATA_FILE.with_suffix('.tmp')
        with open(tmp_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        # Remplace le fichier existant (atomique)
        tmp_file.replace(DATA_FILE)

        logger.info(f"→ Étape 5 : Fichier écrit → {DATA_FILE}")
        logger.info("=" * 60)
        logger.info("=== MAJ AUTO TERMINÉE AVEC SUCCÈS ===")
        logger.info("=" * 60)

        # 6. Log récap
        for annee in ["2026", "2027", "2028", "2029", "2030"]:
            ik = calculer_ik(15000, "5CV", annee, baremes=baremes)
            tag = "(officiel)" if annee == "2026" else "(estimation)"
            logger.info(f"  IK {annee} 5CV 15 000km {tag} : {ik:.2f} €")

        return 0

    except Exception as e:
        logger.exception(f"Erreur critique : {e}")
        return 1


# ── WATERMARK PDF (utilitaire séparé) ──────────────────────
def watermark_pdf(input_path: str, output_path: str, buyer_email: str, year: str = "2026"):
    """
    Ajoute un watermark discret au PDF (email acheteur + année).
    Nécessite : pip install pypdf reportlab
    """
    try:
        from pypdf import PdfWriter, PdfReader
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        import io

        # Créer watermark page
        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=A4)
        c.setFont("Helvetica", 8)
        c.setFillAlpha(0.15)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        # Diagonal watermark
        c.saveState()
        c.translate(297, 421)  # Centre A4
        c.rotate(45)
        c.drawCentredString(0, 0, f"{buyer_email} — {year} — economie-carburant.fr")
        c.restoreState()
        c.save()

        # Merge watermark sur chaque page
        packet.seek(0)
        watermark = PdfReader(packet)
        writer = PdfWriter()
        reader = PdfReader(input_path)

        for page in reader.pages:
            page.merge_page(watermark.pages[0])
            writer.add_page(page)

        with open(output_path, 'wb') as f:
            writer.write(f)

        logger.info(f"Watermark appliqué : {output_path} ({buyer_email})")
        return True

    except ImportError:
        logger.error("pypdf ou reportlab non installé. Installez : pip install pypdf reportlab --break-system-packages")
        return False
    except Exception as e:
        logger.error(f"Erreur watermark : {e}")
        return False


if __name__ == "__main__":
    sys.exit(main())
