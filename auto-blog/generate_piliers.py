#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
economie-carburant.fr - Generateur d'ARTICLES PILIERS (5000 mots)
+ Programme de MISE A JOUR automatique des articles.

- Genere des articles de reference longs (5000 mots) sur les sujets
  principaux, en plusieurs appels IA assembles (slug fixe, page stable).
- Met a jour la date (dateModified) des piliers et peut les regenerer.
- Lance par GitHub Actions, par exemple 1 fois par semaine.

Usage :
  python3 auto-blog/generate_piliers.py            # genere/maj les piliers
  python3 auto-blog/generate_piliers.py --refresh  # force la regeneration
"""
import os
import re
import sys
import json
import html as html_lib
import urllib.request
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO = os.path.join(ROOT, "auto-blog")
PILIERS_FILE = os.path.join(AUTO, "piliers.json")
STYLE_FILE = os.path.join(AUTO, "_style.txt")
SCRIPT_FILE = os.path.join(AUTO, "_script.txt")
STATE_FILE = os.path.join(AUTO, "_piliers_state.json")
LOG_DIR = os.path.join(AUTO, "logs")
SITE = "https://xn--conomie-carburant-9sb.fr"
MONTHS_FR = ["", "janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet",
             "aout", "septembre", "octobre", "novembre", "decembre"]


def log(msg):
    os.makedirs(LOG_DIR, exist_ok=True)
    line = "[%s] %s" % (datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"), msg)
    print(line)
    with open(os.path.join(LOG_DIR, "piliers.log"), "a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_state():
    if os.path.exists(STATE_FILE):
        try:
            return json.load(open(STATE_FILE, encoding="utf-8"))
        except Exception:
            pass
    return {}


def save_state(s):
    json.dump(s, open(STATE_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def ai_part(prompt):
    """Appelle Claude pour generer une partie d'article. Retourne du HTML."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return None
    try:
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 4000,
                "messages": [{"role": "user", "content": prompt}],
            }).encode("utf-8"),
            headers={"Content-Type": "application/json", "x-api-key": key,
                     "anthropic-version": "2023-06-01"})
        resp = json.loads(urllib.request.urlopen(req, timeout=120).read())
        return resp["content"][0]["text"].strip()
    except Exception as e:
        log("IA erreur: %s" % e)
        return None


def generate_pilier(pilier):
    """Genere un article pilier complet (5000 mots) en assemblant les parties."""
    kw = ", ".join(pilier["keywords"])
    parts_html = []
    for i, consigne in enumerate(pilier["parties"], 1):
        prompt = (
            "Tu es un redacteur SEO expert francais (automobile, fiscalite) pour economie-carburant.fr.\n"
            "Tu rediges UNE PARTIE d'un grand article pilier intitule : \"" + pilier["title_hint"] + "\".\n\n"
            "Consigne pour cette partie : " + consigne + "\n"
            "Mots-cles a placer naturellement : " + kw + "\n\n"
            "REGLES :\n"
            "- Reponds UNIQUEMENT en HTML (pas de markdown, pas de <html> ni <body>).\n"
            "- Utilise <h2> pour le titre de section, <h3> pour les sous-sections, <p>, <ul><li>, <table> si pertinent.\n"
            "- Donne des chiffres concrets, exemples calcules, cas pratiques 2026.\n"
            "- Ton expert mais accessible. Pas de bourrage de mots-cles.\n"
            "- Ne repete pas l'introduction generale si ce n'est pas la partie 1.\n"
            "- Ecris du contenu dense et utile, vise la longueur demandee."
        )
        h = ai_part(prompt)
        if not h:
            return None  # pas de cle ou erreur -> on abandonne (les piliers exigent l'IA)
        # nettoyer d'eventuels ```html
        h = re.sub(r"^```(?:html)?", "", h).strip()
        h = re.sub(r"```$", "", h).strip()
        parts_html.append(h)
        log("  partie %d/%d generee (%d car.)" % (i, len(pilier["parties"]), len(h)))
    return "\n".join(parts_html)


def build_page(pilier, body_html, date_human):
    style = open(STYLE_FILE, encoding="utf-8").read()
    script = open(SCRIPT_FILE, encoding="utf-8").read()
    slug = pilier["slug"]
    url = SITE + "/" + slug + ".html"
    title = html_lib.escape(pilier["title_hint"])
    desc = html_lib.escape(pilier["title_hint"])[:160]
    kws = html_lib.escape(", ".join(pilier["keywords"]))

    header = (
        '<header class="site-header"><div class="container header-inner">'
        '<a href="index.html" class="logo"><div class="logo-icon">&#9981;</div>'
        '<div class="logo-text">&Eacute;conomie<span>-Carburant</span>.fr</div></a>'
        '<nav class="nav"><a href="bareme-kilometrique-2026.html">Bar&egrave;me IK</a>'
        '<a href="cout-trajet.html">Co&ucirc;t trajet</a><a href="calculateur-consommation.html">L/100km</a>'
        '<a href="comparatif-carburants.html">Comparatif</a><a href="blog.html">Blog</a>'
        '<a href="guide-bareme-ik-2026-pdf.html" class="nav-cta">&#128196; Guide PDF &mdash; 9,99 &euro;</a>'
        '</nav><button class="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>'
        '</div></header>'
    )
    footer = (
        '<footer class="site-footer"><div class="container"><div class="footer-bottom">'
        '<div class="footer-copy">&copy; 2026 &Eacute;conomie-Carburant.fr</div>'
        '<div class="trust-badges"><div class="trust-badge">SSL</div>'
        '<div class="trust-badge">RGPD</div></div></div></div></footer>'
    )
    cta = (
        '<div class="art-cta" style="background:linear-gradient(135deg,#1A252F,#1E3A28);border-radius:16px;padding:28px 32px;margin:32px 0;text-align:center">'
        '<h3 style="color:#fff;margin-bottom:8px">Passez au calcul concret</h3>'
        '<p style="color:rgba(255,255,255,0.6);margin-bottom:16px">Utilisez notre ' + html_lib.escape(pilier["outil_nom"]) + ', gratuit.</p>'
        '<a href="' + pilier["outil_lie"] + '" class="btn btn-green">Ouvrir l\'outil &rarr;</a></div>'
    )
    art_style = (
        '<style>.art-hero{background:linear-gradient(135deg,#0D1B2A,#152A1E);padding:48px 0 72px;position:relative;overflow:hidden}'
        '.art-hero::after{content:"";position:absolute;bottom:-1px;left:0;right:0;height:40px;background:#FAFBFC;border-radius:40px 40px 0 0}'
        '.art-wrap{max-width:760px;margin:0 auto;padding:0 20px}.art-content{background:var(--bg-2);padding:48px 0 80px}'
        '.art-content h2{margin:32px 0 14px;font-size:1.5rem}.art-content h3{margin:22px 0 10px;font-size:1.15rem;color:var(--dark-2)}'
        '.art-content p{margin-bottom:16px;color:var(--dark-3);line-height:1.8}.art-content ul,.art-content ol{margin:0 0 16px 0;padding-left:24px;color:var(--dark-3);line-height:1.9}'
        '.art-content table{width:100%;border-collapse:collapse;margin:20px 0;font-size:0.92rem}.art-content th{background:#1A252F;color:#fff;padding:10px 14px;text-align:left}'
        '.art-content td{padding:10px 14px;border-bottom:1px solid #E5E9ED}.art-content a{color:var(--green-dark);text-decoration:underline}</style>'
    )
    schema = ('<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Article", "headline": pilier["title_hint"],
        "description": pilier["title_hint"], "datePublished": "2026-01-01",
        "dateModified": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "author": {"@type": "Organization", "name": "Economie-Carburant.fr", "url": SITE},
        "publisher": {"@type": "Organization", "name": "Economie-Carburant.fr", "url": SITE},
        "mainEntityOfPage": url, "keywords": ", ".join(pilier["keywords"])}, ensure_ascii=False) + '</script>')
    breadcrumb = ('<script type="application/ld+json">'
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Accueil","item":"' + SITE + '/"},'
        '{"@type":"ListItem","position":2,"name":"Blog","item":"' + SITE + '/blog.html"},'
        '{"@type":"ListItem","position":3,"name":"Guide","item":"' + url + '"}]}</script>')

    body = (
        art_style +
        '<div class="art-hero"><div class="container art-wrap">'
        '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><a href="index.html">Accueil</a>'
        '<span class="breadcrumb-sep">/</span><a href="blog.html">Blog</a>'
        '<span class="breadcrumb-sep">/</span><span>Guide</span></nav>'
        '<span class="article-tag" style="background:var(--green-light);color:var(--green-dark);margin-bottom:12px">Guide complet</span>'
        '<h1 style="color:#fff">' + title + '</h1>'
        '<div style="color:rgba(255,255,255,0.5);font-size:0.85rem;margin-top:12px">Mis a jour le ' + date_human + ' &middot; &Eacute;conomie-Carburant.fr</div>'
        '</div></div>'
        '<div class="art-content"><div class="art-wrap">'
        + body_html + cta +
        '<div class="related-tools" style="margin-top:32px">'
        '<a href="bareme-kilometrique-2026.html" class="related-card"><div class="related-icon icon-green">&#128202;</div><div class="related-text">Bar&egrave;me IK</div></a>'
        '<a href="blog.html" class="related-card"><div class="related-icon icon-purple">&#128221;</div><div class="related-text">Tous les articles</div></a>'
        '</div></div></div>'
    )
    return (
        '<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>' + title + ' &mdash; Economie-Carburant.fr</title>\n'
        '<meta name="description" content="' + desc + '">\n'
        '<meta name="keywords" content="' + kws + '">\n'
        '<link rel="canonical" href="' + url + '">\n'
        '<meta property="og:title" content="' + title + '">\n'
        '<meta property="og:description" content="' + desc + '">\n'
        '<meta property="og:type" content="article">\n'
        '<meta property="og:url" content="' + url + '">\n'
        '<meta property="og:image" content="' + SITE + '/og-image.png">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;1,14..32,400&display=swap">\n'
        '<style>\n' + style + '\n</style>\n' + schema + '\n' + breadcrumb + '\n</head>\n<body>\n'
        + header + body + footer + '\n<script>\n' + script + '\n</script>\n</body>\n</html>'
    )


def main():
    refresh = "--refresh" in sys.argv
    log("=== Generation/MAJ des piliers (refresh=%s) ===" % refresh)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        log("Pas de cle ANTHROPIC_API_KEY : les piliers exigent l'IA. Arret.")
        return
    cfg = json.load(open(PILIERS_FILE, encoding="utf-8"))
    state = load_state()
    now = datetime.now(timezone.utc)
    date_human = "%d %s %d" % (now.day, MONTHS_FR[now.month], now.year)

    for pilier in cfg["piliers"]:
        slug = pilier["slug"]
        path = os.path.join(ROOT, slug + ".html")
        exists = os.path.exists(path)
        # Generer si : n'existe pas, OU refresh demande, OU pas mis a jour depuis 90 jours
        last = state.get(slug, {}).get("generated")
        stale = False
        if last:
            try:
                d = datetime.fromisoformat(last)
                stale = (now - d).days >= 90
            except Exception:
                stale = True
        if exists and not refresh and not stale:
            log("%s : a jour, ignore" % slug)
            continue
        log("Generation de %s ..." % slug)
        body = generate_pilier(pilier)
        if not body:
            log("%s : echec generation (IA indispo)" % slug)
            continue
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        page = build_page(pilier, body, date_human)
        open(path, "w", encoding="utf-8").write(page)
        state[slug] = {"generated": now.isoformat(), "words": words}
        log("%s : ecrit (~%d mots)" % (slug, words))

    save_state(state)
    log("=== Termine ===")


if __name__ == "__main__":
    main()
