#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
economie-carburant.fr - Generateur de blog AUTOMATIQUE v2
Articles 2000-2500 mots, SEO + citation LLM, sources citees,
maillage interne, CTA PDF, partage social, logs.
Concu pour GitHub Actions (1 execution / jour).
"""
import os
import re
import json
import html as html_lib
import urllib.request
import urllib.parse
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO = os.path.join(ROOT, "auto-blog")
TOPICS_FILE = os.path.join(AUTO, "topics.json")
STYLE_FILE = os.path.join(AUTO, "_style.txt")
SCRIPT_FILE = os.path.join(AUTO, "_script.txt")
STATE_FILE = os.path.join(AUTO, "_state.json")
LOG_DIR = os.path.join(AUTO, "logs")
SITE = "https://economie-carburant.fr"
MONTHS_FR = ["", "janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet",
             "aout", "septembre", "octobre", "novembre", "decembre"]


def log(msg):
    os.makedirs(LOG_DIR, exist_ok=True)
    line = "[%s] %s" % (datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"), msg)
    print(line)
    with open(os.path.join(LOG_DIR, "blog.log"), "a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_state():
    if os.path.exists(STATE_FILE):
        try:
            return json.load(open(STATE_FILE, encoding="utf-8"))
        except Exception:
            pass
    return {"published": [], "topic_index": 0}


def save_state(s):
    json.dump(s, open(STATE_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def slugify(t):
    t = t.lower()
    for a, b in [("\u00e0\u00e2\u00e4", "a"), ("\u00e9\u00e8\u00ea\u00eb", "e"),
                 ("\u00ee\u00ef", "i"), ("\u00f4\u00f6", "o"), ("\u00f9\u00fb\u00fc", "u"), ("\u00e7", "c")]:
        for ch in a:
            t = t.replace(ch, b)
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")[:65]


def fetch_rss():
    feeds = [
        "https://news.google.com/rss/search?q=prix+carburant+France&hl=fr&gl=FR&ceid=FR:fr",
        "https://news.google.com/rss/search?q=bareme+kilometrique+impots&hl=fr&gl=FR&ceid=FR:fr",
        "https://news.google.com/rss/search?q=voiture+electrique+prix&hl=fr&gl=FR&ceid=FR:fr",
    ]
    items = []
    for url in feeds:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            xml = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
            for b in re.findall(r"<item>(.*?)</item>", xml, re.DOTALL)[:3]:
                tm = re.search(r"<title>(.*?)</title>", b)
                lm = re.search(r"<link>(.*?)</link>", b)
                sm = re.search(r"<source[^>]*>(.*?)</source>", b)
                if tm:
                    items.append({
                        "title": html_lib.unescape(re.sub(r"<.*?>", "", tm.group(1))).strip(),
                        "link": (lm.group(1).strip() if lm else ""),
                        "source": (html_lib.unescape(sm.group(1)).strip() if sm else "Google News"),
                    })
        except Exception as e:
            log("RSS erreur: %s" % e)
    seen, out = set(), []
    for it in items:
        if it["title"] and it["title"] not in seen and len(it["title"]) > 15:
            seen.add(it["title"]); out.append(it)
    return out[:6]


def generate_with_ai(topic, rss, sources):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        log("Pas de cle ANTHROPIC_API_KEY -> fallback")
        return None
    rss_txt = "\n".join("- %s (source: %s)" % (r["title"], r["source"]) for r in rss) or "Aucune"
    src_txt = "\n".join("- %s : %s" % (s["nom"], s["url"]) for s in sources)
    kw = ", ".join(topic["keywords"])
    prompt = (
        "Tu es un redacteur SEO expert francais specialise automobile et fiscalite, pour economie-carburant.fr.\n\n"
        "Redige un article de blog COMPLET de 2000 a 2500 mots sur :\n\"" + topic["title_hint"] + "\"\n\n"
        "Type: " + topic["type"] + "\nAngle: " + topic["angle"] + "\n"
        "Mots-cles SEO a placer naturellement: " + kw + "\n\n"
        "Actualites a citer si pertinent:\n" + rss_txt + "\n\n"
        "Sources officielles a citer (2 a 4 en liens <a> dans le corps):\n" + src_txt + "\n\n"
        "CONTRAINTES:\n"
        "- 2000-2500 mots, francais impeccable, expert mais accessible\n"
        "- intro accrocheuse + 5-8 sections H2 + H3 si utile\n"
        "- AU MOINS un tableau comparatif en HTML <table>\n"
        "- une FAQ de 3-4 questions a la fin\n"
        "- chiffres concrets, exemples calcules, cas pratiques\n"
        "- citer les sources avec de vrais <a href>\n"
        "- mailler vers l'outil du site: " + topic["outil_nom"] + "\n"
        "- ne pas inventer de fausses stats precises, rester credible 2026\n"
        "- pas de bourrage de mots-cles\n\n"
        "REPONDS UNIQUEMENT EN JSON VALIDE:\n"
        '{"title":"H1 SEO accrocheur avec mot-cle","meta_desc":"150-160 car","tag":"categorie 1 mot",'
        '"keywords":["k1","k2","k3"],"intro":"intro HTML","body_html":"corps HTML complet avec <h2><h3><p><ul><table><a>, FAQ a la fin, SANS le H1 ni intro",'
        '"sources_citees":[{"nom":"...","url":"..."}]}'
    )
    try:
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 8000,
                "messages": [{"role": "user", "content": prompt}],
            }).encode("utf-8"),
            headers={"Content-Type": "application/json", "x-api-key": key,
                     "anthropic-version": "2023-06-01"})
        resp = json.loads(urllib.request.urlopen(req, timeout=120).read())
        text = resp["content"][0]["text"].strip()
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
        s, e = text.find("{"), text.rfind("}")
        data = json.loads(text[s:e + 1])
        data["source_type"] = "IA (Claude Sonnet 4)"
        log("Article IA genere: %s" % data.get("title", "?"))
        return data
    except Exception as e:
        log("IA erreur: %s -> fallback" % e)
        return None


def generate_fallback(topic, rss, sources):
    kw = topic["keywords"]
    body = ""
    for h, p in [
        ("Ce qu'il faut savoir", "Le sujet de %s concerne de nombreux automobilistes francais en 2026. Comprendre les regles, les chiffres et les bonnes pratiques permet d'economiser plusieurs centaines d'euros par an." % kw[0]),
        ("Les chiffres cles 2026", "SP95-E10 autour de 2,06 EUR/L, diesel a 2,33 EUR, E85 a 0,84 EUR. Le bareme kilometrique 2026 pour 5 CV atteint 6 960 EUR pour 15 000 km."),
        ("Comment optimiser", "Choisir le bon carburant, conduire souplement, entretenir le vehicule, comparer l'assurance, bien declarer aux impots. Combines, ces leviers reduisent le budget de 20 a 40%."),
        ("Cas pratique chiffre", "15 000 km/an en 5 CV : en frais reels plutot que l'abattement 10%, on deduit jusqu'a 6 960 EUR, soit plusieurs centaines d'euros d'impot economises."),
        ("Erreurs a eviter", "Confondre CV fiscaux et DIN, oublier les justificatifs, inclure les peages dans le bareme, choisir les frais reels sans calcul prealable."),
    ]:
        body += "<h2>%s</h2><p>%s</p>" % (h, p)
    body += ("<h2>Tableau recapitulatif</h2><table><thead><tr><th>Carburant</th><th>Prix</th><th>Cout/100km</th></tr></thead>"
             "<tbody><tr><td>SP95-E10</td><td>2,06 EUR/L</td><td>14,42 EUR</td></tr>"
             "<tr><td>Diesel</td><td>2,33 EUR/L</td><td>13,98 EUR</td></tr>"
             "<tr class='highlight'><td>E85</td><td>0,84 EUR/L</td><td>7,06 EUR</td></tr></tbody></table>")
    body += ("<h2>Questions frequentes</h2>"
             "<h3>Quel est le bareme kilometrique 2026 ?</h3><p>Pour 5 CV : jusqu'a 5 000 km, x0,636 ; 5 001-20 000 km, x0,378 + 1 290 EUR ; au-dela, x0,440.</p>"
             "<h3>Les frais reels sont-ils avantageux ?</h3><p>Oui des que vos frais depassent l'abattement de 10%, frequent au-dela de 10 000 km/an.</p>"
             "<h3>Quel carburant est le moins cher ?</h3><p>L'E85 reste le moins cher au km en 2026 malgre une surconsommation de 20-25%.</p>")
    return {
        "title": topic["title_hint"],
        "meta_desc": ("%s : guide 2026 avec chiffres, exemples et conseils pour economiser." % kw[0].capitalize())[:160],
        "tag": topic["type"].capitalize(), "keywords": kw,
        "intro": "Tout savoir sur <strong>%s</strong> en 2026 : chiffres a jour, methode, exemples et astuces." % kw[0],
        "body_html": body, "sources_citees": sources[:3], "source_type": "stock structure",
    }


def nav_header():
    return ('<header class="site-header"><div class="container header-inner">'
            '<a href="index.html" class="logo"><div class="logo-icon">&#9981;</div>'
            '<div class="logo-text">&Eacute;conomie<span>-Carburant</span>.fr</div></a>'
            '<nav class="nav"><a href="bareme-kilometrique-2026.html">Bar&egrave;me IK</a>'
            '<a href="cout-trajet.html">Co&ucirc;t trajet</a><a href="calculateur-consommation.html">L/100km</a>'
            '<a href="comparatif-carburants.html">Comparatif</a><a href="blog.html" class="active">Blog</a>'
            '<a href="guide-bareme-ik-2026-pdf.html" class="nav-cta">&#128196; Guide PDF &mdash; 9,99 &euro;</a>'
            '</nav><button class="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>'
            '</div></header>')


def footer():
    return ('<footer class="site-footer"><div class="container"><div class="footer-grid">'
            '<div class="footer-brand"><a href="index.html" class="logo"><div class="logo-icon">&#9981;</div>'
            '<div class="logo-text" style="color:rgba(255,255,255,.9)">&Eacute;conomie<span>-Carburant</span>.fr</div></a>'
            '<p class="footer-desc">Calculateurs auto gratuits. Prix carburant France 2026.</p></div>'
            '<div><div class="footer-title">Calculateurs</div><ul class="footer-links">'
            '<li><a href="bareme-kilometrique-2026.html">Bar&egrave;me IK 2026</a></li>'
            '<li><a href="cout-trajet.html">Co&ucirc;t trajet</a></li>'
            '<li><a href="calculateur-consommation.html">L/100km</a></li>'
            '<li><a href="budget-auto-mensuel.html">Budget auto</a></li>'
            '<li><a href="comparatif-carburants.html">Comparatif</a></li>'
            '<li><a href="carte-grise-2026.html">Carte grise</a></li></ul></div>'
            '<div><div class="footer-title">Ressources</div><ul class="footer-links">'
            '<li><a href="blog.html">Blog</a></li><li><a href="guide-bareme-ik-2026-pdf.html">Guide PDF 9,99 &euro;</a></li></ul></div>'
            '<div><div class="footer-title">L&eacute;gal</div><ul class="footer-links">'
            '<li><a href="mentions-legales.html">Mentions l&eacute;gales</a></li>'
            '<li><a href="cgv.html">CGV</a></li><li><a href="rgpd.html">RGPD</a></li>'
            '<li><a href="contact.html">Contact</a></li></ul></div></div>'
            '<div class="footer-bottom"><div class="footer-copy">&copy; 2026 &Eacute;conomie-Carburant.fr</div>'
            '<div class="trust-badges"><div class="trust-badge">SSL</div><div class="trust-badge">RGPD</div></div>'
            '</div></div></footer>')


def share_block(title, url_enc):
    t = urllib.parse.quote(title)
    return ('<div style="background:var(--green-light);border-radius:var(--radius-lg);padding:24px;margin:32px 0;text-align:center">'
            '<div style="font-weight:700;color:var(--green-dark);font-size:1.05rem;margin-bottom:6px">Cet article vous a aide ?</div>'
            '<p style="color:var(--dark-3);margin-bottom:14px;font-size:0.92rem">Partagez-le, vous aiderez un proche a economiser sur son budget auto.</p>'
            '<div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap">'
            '<a href="https://www.facebook.com/sharer/sharer.php?u=' + url_enc + '" target="_blank" rel="noopener" class="btn btn-sm" style="background:#1877F2;color:#fff">Facebook</a>'
            '<a href="https://twitter.com/intent/tweet?url=' + url_enc + '&text=' + t + '" target="_blank" rel="noopener" class="btn btn-sm" style="background:#000;color:#fff">X</a>'
            '<a href="https://www.linkedin.com/sharing/share-offsite/?url=' + url_enc + '" target="_blank" rel="noopener" class="btn btn-sm" style="background:#0A66C2;color:#fff">LinkedIn</a>'
            '<a href="https://api.whatsapp.com/send?text=' + t + '%20' + url_enc + '" target="_blank" rel="noopener" class="btn btn-sm" style="background:#25D366;color:#fff">WhatsApp</a>'
            '</div></div>')


def build_article(data, topic, rss, date_human, slug):
    style = open(STYLE_FILE, encoding="utf-8").read()
    script = open(SCRIPT_FILE, encoding="utf-8").read()
    url = SITE + "/" + slug + ".html"
    url_enc = urllib.parse.quote(url)
    title = html_lib.escape(data["title"])
    desc = html_lib.escape(data.get("meta_desc", data["title"]))[:160]
    tag = html_lib.escape(data.get("tag", "Guide"))
    intro = data.get("intro", "")
    body = data.get("body_html", "")
    kws = ", ".join(data.get("keywords", topic["keywords"]))

    rss_html = ""
    if rss:
        lis = ""
        for r in rss[:4]:
            if r.get("link"):
                lis += '<li><a href="%s" target="_blank" rel="noopener nofollow">%s</a> <span style="color:var(--gray-light)">&mdash; %s</span></li>' % (r["link"], html_lib.escape(r["title"]), html_lib.escape(r["source"]))
            else:
                lis += "<li>%s</li>" % html_lib.escape(r["title"])
        rss_html = '<h2>L\'actualite recente sur le sujet</h2><ul style="padding-left:20px;line-height:1.9;color:var(--dark-3)">' + lis + '</ul>'

    src_html = ""
    srcs = data.get("sources_citees", [])
    if srcs:
        lis = "".join('<li><a href="%s" target="_blank" rel="noopener nofollow">%s</a></li>' % (s.get("url", "#"), html_lib.escape(s.get("nom", s.get("url", "")))) for s in srcs)
        src_html = '<div class="sources-section" style="margin-top:32px"><div class="sources-title">Sources officielles</div><ul style="padding-left:20px;line-height:1.9">' + lis + '</ul></div>'

    cta_outil = ('<div class="art-cta"><h3>Passez au calcul concret</h3><p>Utilisez notre ' + html_lib.escape(topic["outil_nom"]) + ', gratuit et immediat.</p><a href="' + topic["outil_lie"] + '" class="btn btn-green">Ouvrir l\'outil &rarr;</a></div>')
    cta_pdf = ('<div style="background:linear-gradient(135deg,#1A252F,#1E3A28);border-radius:var(--radius-lg);padding:24px 28px;margin:24px 0;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap">'
               '<div><div style="color:#4ADE80;font-weight:700;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px">Guide premium</div>'
               '<div style="color:#fff;font-family:var(--font-head);font-weight:700;font-size:1.1rem">Guide complet Bar&egrave;me IK 2026-2030</div>'
               '<div style="color:rgba(255,255,255,0.6);font-size:0.85rem">30 pages, 100 exemples, calculateurs Excel inclus</div></div>'
               '<div style="text-align:center"><div style="font-family:var(--font-head);font-weight:800;font-size:1.8rem;color:#4ADE80">9,99 &euro;</div>'
               '<a href="guide-bareme-ik-2026-pdf.html" class="btn btn-green btn-sm">Decouvrir</a></div></div>')

    art_style = ('<style>.art-hero{background:linear-gradient(135deg,#0D1B2A,#152A1E);padding:48px 0 72px;position:relative;overflow:hidden}'
                 '.art-hero::after{content:"";position:absolute;bottom:-1px;left:0;right:0;height:40px;background:#FAFBFC;border-radius:40px 40px 0 0}'
                 '.art-wrap{max-width:760px;margin:0 auto;padding:0 20px}'
                 '.art-content{background:var(--bg-2);padding:48px 0 80px}'
                 '.art-content h2{margin:32px 0 14px;font-size:1.5rem}'
                 '.art-content h3{margin:22px 0 10px;font-size:1.15rem;color:var(--dark-2)}'
                 '.art-content p{margin-bottom:16px;color:var(--dark-3);line-height:1.8}'
                 '.art-content ul,.art-content ol{margin:0 0 16px 0;padding-left:24px;color:var(--dark-3);line-height:1.9}'
                 '.art-content table{width:100%;border-collapse:collapse;margin:20px 0;font-size:0.92rem}'
                 '.art-content th{background:#1A252F;color:#fff;padding:10px 14px;text-align:left}'
                 '.art-content td{padding:10px 14px;border-bottom:1px solid #E5E9ED}'
                 '.art-content tr.highlight td{background:var(--green-light);font-weight:600}'
                 '.art-content a{color:var(--green-dark);text-decoration:underline}'
                 '.art-cta{background:linear-gradient(135deg,#1A252F,#1E3A28);border-radius:var(--radius-lg);padding:28px 32px;margin:32px 0;text-align:center}'
                 '.art-cta h3{color:#fff;margin-bottom:8px}.art-cta p{color:rgba(255,255,255,0.6);margin-bottom:16px}'
                 '.art-meta-top{display:flex;align-items:center;gap:12px;color:rgba(255,255,255,0.5);font-size:0.85rem;margin-top:12px}</style>')

    schema = ('<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Article", "headline": data["title"],
        "description": data.get("meta_desc", ""), "datePublished": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "dateModified": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "author": {"@type": "Organization", "name": "Economie-Carburant.fr", "url": SITE},
        "publisher": {"@type": "Organization", "name": "Economie-Carburant.fr", "url": SITE},
        "mainEntityOfPage": url, "keywords": kws}, ensure_ascii=False) + '</script>')

    body_full = (art_style + '<div class="art-hero"><div class="container art-wrap">'
                 '<div class="breadcrumb"><a href="index.html">Accueil</a><span class="breadcrumb-sep">/</span>'
                 '<a href="blog.html">Blog</a><span class="breadcrumb-sep">/</span><span>Article</span></div>'
                 '<span class="article-tag" style="background:var(--green-light);color:var(--green-dark);margin-bottom:12px">' + tag + '</span>'
                 '<h1 style="color:#fff">' + title + '</h1>'
                 '<div class="art-meta-top">' + date_human + ' &middot; &Eacute;conomie-Carburant.fr &middot; Mis a jour 2026</div></div></div>'
                 '<div class="art-content"><div class="art-wrap">'
                 '<p style="font-size:1.12rem;color:var(--dark-2);line-height:1.7">' + intro + '</p>'
                 + body + cta_outil + rss_html + cta_pdf + share_block(data["title"], url_enc) + src_html +
                 '<div class="related-tools" style="margin-top:32px">'
                 '<a href="bareme-kilometrique-2026.html" class="related-card"><div class="related-icon icon-green">&#128202;</div><div class="related-text">Bar&egrave;me IK 2026</div></a>'
                 '<a href="cout-trajet.html" class="related-card"><div class="related-icon icon-blue">&#128506;</div><div class="related-text">Co&ucirc;t trajet</div></a>'
                 '<a href="blog.html" class="related-card"><div class="related-icon icon-purple">&#128221;</div><div class="related-text">Tous les articles</div></a>'
                 '</div></div></div>')

    return ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>' + title + ' &mdash; Economie-Carburant.fr</title>\n'
            '<meta name="description" content="' + desc + '">\n'
            '<meta name="keywords" content="' + html_lib.escape(kws) + '">\n'
            '<link rel="canonical" href="' + url + '">\n'
            '<meta property="og:title" content="' + title + '">\n'
            '<meta property="og:description" content="' + desc + '">\n'
            '<meta property="og:type" content="article">\n<meta property="og:url" content="' + url + '">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;1,14..32,400&display=swap">\n'
            '<style>\n' + style + '\n</style>\n' + schema + '\n</head>\n<body>\n'
            + nav_header() + body_full + footer() + '\n<script>\n' + script + '\n</script>\n</body>\n</html>')


def rebuild_index(published):
    style = open(STYLE_FILE, encoding="utf-8").read()
    script = open(SCRIPT_FILE, encoding="utf-8").read()
    grads = ["linear-gradient(135deg,#EAFAF1,#A9DFBF)", "linear-gradient(135deg,#EBF5FB,#85B7EB)",
             "linear-gradient(135deg,#FEF9E7,#F6C142)", "linear-gradient(135deg,#F5EEF8,#D7BDE2)",
             "linear-gradient(135deg,#FDEDEC,#F1948A)", "linear-gradient(135deg,#E8F8F5,#76D7C4)"]
    icons = ["&#128202;", "&#9881;", "&#9889;", "&#128176;", "&#128663;", "&#128221;"]
    cards = ""
    for i, a in enumerate(reversed(published[-60:])):
        cards += ('<a href="' + a["file"] + '" class="article-card">'
                  '<div class="article-img" style="background:' + grads[i % len(grads)] + '">' + icons[i % len(icons)] + '</div>'
                  '<div class="article-body"><span class="article-tag" style="background:var(--green-light);color:var(--green-dark)">'
                  + html_lib.escape(a["tag"]) + '</span><h3>' + html_lib.escape(a["title"]) + '</h3>'
                  '<p>' + html_lib.escape(a.get("desc", "")) + '</p>'
                  '<div class="article-meta">' + a["date"] + '</div></div></a>')
    blog_style = ('<style>.blog-hero{background:linear-gradient(135deg,#0D1B2A,#152A1E);padding:56px 0 80px;position:relative;overflow:hidden}'
                  '.blog-hero::after{content:"";position:absolute;bottom:-1px;left:0;right:0;height:40px;background:#FAFBFC;border-radius:40px 40px 0 0}'
                  '.article-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}'
                  '.article-card{background:var(--white);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--card-shadow);border:1px solid rgba(44,62,80,0.06);transition:all var(--transition);display:flex;flex-direction:column}'
                  '.article-card:hover{transform:translateY(-6px);box-shadow:var(--card-hover)}'
                  '.article-img{height:160px;display:flex;align-items:center;justify-content:center;font-size:3.5rem}'
                  '.article-body{padding:24px}.article-tag{display:inline-block;font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;padding:3px 10px;border-radius:100px;margin-bottom:10px}'
                  '.article-card h3{font-size:1.05rem;margin-bottom:8px;line-height:1.3}'
                  '.article-card p{font-size:0.88rem;color:var(--gray);line-height:1.5;margin-bottom:14px}'
                  '.article-meta{font-size:0.78rem;color:var(--gray-light);margin-top:auto}'
                  '@media(max-width:768px){.article-grid{grid-template-columns:1fr}}</style>')
    body = (blog_style + '<div class="blog-hero"><div class="container">'
            '<div class="breadcrumb"><a href="index.html">Accueil</a><span class="breadcrumb-sep">/</span><span>Blog</span></div>'
            '<span class="hero-badge" style="margin:0 0 12px">&#128221; Le blog</span>'
            '<h1 style="color:#fff;margin-bottom:10px">Conseils &amp; guides auto 2026</h1>'
            '<p class="tool-tldr">Un nouvel article chaque jour : bar&egrave;me kilometrique, economies de carburant, fiscalite, comparatifs.</p>'
            '</div></div><div style="background:var(--bg-2);padding:60px 0 80px"><div class="container">'
            '<div class="article-grid">' + cards + '</div></div></div>')
    page = ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>Blog Auto 2026 &mdash; Conseils Budget, Carburant &amp; Fiscalite | Economie-Carburant.fr</title>\n'
            '<meta name="description" content="Guides et conseils pour optimiser votre budget auto 2026. Nouvel article chaque jour.">\n'
            '<link rel="canonical" href="' + SITE + '/blog.html">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;1,14..32,400&display=swap">\n'
            '<style>\n' + style + '\n</style>\n</head>\n<body>\n'
            + nav_header() + body + footer() + '\n<script>\n' + script + '\n</script>\n</body>\n</html>')
    open(os.path.join(ROOT, "blog.html"), "w", encoding="utf-8").write(page)
    log("blog.html reconstruit (%d articles)" % len(published))


def update_sitemap(published):
    sm = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(sm):
        return
    c = open(sm, encoding="utf-8").read()
    c = re.sub(r"\s*<!-- AUTO-BLOG -->.*?<!-- /AUTO-BLOG -->", "", c, flags=re.DOTALL)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    block = "\n  <!-- AUTO-BLOG -->"
    for a in published[-60:]:
        block += ('\n  <url><loc>' + SITE + '/' + a["file"] + '</loc><lastmod>' + today +
                  '</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>')
    block += "\n  <!-- /AUTO-BLOG -->"
    c = c.replace("</urlset>", block + "\n</urlset>")
    open(sm, "w", encoding="utf-8").write(c)
    log("sitemap.xml mis a jour")


def main():
    log("=== Demarrage generation ===")
    cfg = json.load(open(TOPICS_FILE, encoding="utf-8"))
    topics, sources = cfg["topics"], cfg["sources_officielles"]
    state = load_state()
    idx = state.get("topic_index", 0) % len(topics)
    topic = topics[idx]
    state["topic_index"] = idx + 1
    log("Sujet #%d: %s" % (idx, topic["title_hint"]))
    rss = fetch_rss()
    log("%d actualites RSS" % len(rss))
    data = generate_with_ai(topic, rss, sources) or generate_fallback(topic, rss, sources)
    now = datetime.now(timezone.utc)
    date_human = "%d %s %d" % (now.day, MONTHS_FR[now.month], now.year)
    base = "blog-" + slugify(data["title"])
    slug, n = base, 2
    existing = {a["file"] for a in state["published"]}
    while (slug + ".html") in existing:
        slug = base + "-" + str(n); n += 1
    fn = slug + ".html"
    page = build_article(data, topic, rss, date_human, slug)
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write(page)
    words = len(re.sub(r"<[^>]+>", " ", data.get("body_html", "")).split())
    log("Article: %s (~%d mots, %s)" % (fn, words, data.get("source_type")))
    state["published"].append({"file": fn, "title": data["title"], "desc": data.get("meta_desc", ""),
                               "tag": data.get("tag", "Guide"), "date": date_human, "source": data.get("source_type", "?")})
    save_state(state)
    rebuild_index(state["published"])
    update_sitemap(state["published"])
    log("=== Termine ===")


if __name__ == "__main__":
    main()
