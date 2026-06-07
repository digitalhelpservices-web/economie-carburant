# Blog automatique PRO - Activation + Feuille de route

## ⚠️ URGENT - Securite

Tu as colle ta cle API Claude dans le chat. **Revoque-la maintenant** :
1. https://console.anthropic.com -> Settings -> API Keys
2. Supprime la cle commencant par `sk-ant-api03-RkYVnST...`
3. Cree une NOUVELLE cle
4. Ne la colle JAMAIS ailleurs - elle va dans les Secrets GitHub (chiffres)

---

## Ce qui a ete construit

Un systeme qui publie **1 article par jour, 100% automatique** :
- **2000-2500 mots** rediges par Claude Sonnet 4 (ta cle API)
- **24 sujets** en rotation (guides, comparatifs, informatifs) -> jamais repetitif
- **Mots-cles SEO** Google places naturellement dans chaque article
- **Sources officielles citees** (service-public, impots.gouv, ADEME...) avec liens
- **Actualites RSS** fraiches injectees et sourcees
- **Maillage interne** : chaque article renvoie vers tes 6 outils + le PDF
- **CTA PDF 9,99 EUR** + **boutons de partage** (Facebook, X, LinkedIn, WhatsApp)
- **Schema.org Article** (pour Google + citation par les LLM)
- **Sitemap mis a jour** automatiquement
- **Logs** dans auto-blog/logs/blog.log
- **Heure : 8h du matin** (Paris) - choisie pour l'indexation Google

Fonctionne meme sans cle (mode secours gratuit avec stock + RSS).

---

## Activation (une seule fois)

### 1. Mettre le code sur GitHub avec le dossier .github
Le dossier `.github` est "cache" et les uploads web le ratent souvent.
**Solution fiable : decompresse le ZIP et verifie que `.github/workflows/blog-quotidien.yml` est present, puis pousse TOUT sur GitHub via GitHub Desktop** (qui preserve les dossiers caches), ou en glissant le contenu decompresse.

> Astuce : sur GitHub web, active "Show hidden files" ou utilise GitHub Desktop.

### 2. Ajouter ta cle API en secret (chiffre, invisible)
1. Depot GitHub -> **Settings** -> **Secrets and variables** -> **Actions**
2. **New repository secret**
3. Nom : `ANTHROPIC_API_KEY`
4. Valeur : ta NOUVELLE cle (celle creee apres revocation)
5. **Add secret**

### 3. Activer et tester
1. Onglet **Actions** -> activer les workflows si demande
2. "Blog automatique quotidien" -> **Run workflow** -> **Run workflow**
3. ~2 min plus tard : un article de 2000+ mots apparait sur ton site

A partir de la : 1 article chaque matin a 8h, sans rien faire.

---

## AUTO-EVALUATION : ce qui est fait / ce qui manque pour etre n.1

### Deja en place (fort)
- [x] Contenu quotidien automatique, long, SEO, non repetitif
- [x] Maillage interne site <-> outils <-> PDF
- [x] Sources citees (E-E-A-T : credibilite pour Google)
- [x] Schema.org Article + FAQ (rich snippets + citation LLM)
- [x] Partage social
- [x] Sitemap auto

### A faire par TOI (hors code) - PRIORITAIRE
1. **Google Search Console** : ajoute le site, soumets sitemap.xml. INDISPENSABLE pour ranker.
2. **Bing Webmaster Tools** : meme chose (Bing alimente ChatGPT/Copilot).
3. **Domaine propre** : connecte economie-carburant.fr (un .netlify.app ne rankera jamais n.1).
4. **Backlinks** : inscris le site sur annuaires fiables, reponds sur forums (avec lien naturel), propose des articles invites. Le netlinking reste le facteur n.1 de Google.

### Ameliorations que je peux coder ensuite (dis-moi)
- **llms.txt** : fichier qui indique aux LLM (ChatGPT, Perplexity, Claude) comment citer ton site
- **Schema.org Organization + WebSite + sitelinks** sur la home (autorite de marque)
- **Page "A propos" + auteur** : Google valorise l'E-E-A-T (qui ecrit ?)
- **Fil d'Ariane Schema** sur toutes les pages
- **Image Open Graph** auto par article (apercu sur reseaux sociaux)
- **Newsletter** (capture email = trafic recurrent)
- **Tableau de bord analytics** (Plausible/GA4) pour suivre ce qui marche
- **Articles "piliers"** longs (5000 mots) sur tes 3 sujets principaux + clusters
- **Liens d'affiliation** : envoie-les, je les integre dans les CTA des articles
- **Programme de mise a jour** : re-generer les vieux articles tous les 6 mois (Google aime le frais)

### Anti-spam (important pour ne pas etre penalise)
- 1 article/jour = rythme sain (ne PAS monter a 10/jour, Google penalise)
- Contenu unique a chaque fois (la rotation des 24 sujets + IA l'assure)
- Pas de bourrage de mots-cles (le prompt l'interdit)
- Sources reelles (credibilite)

---

## Mon avis honnete

Le systeme de contenu automatique est solide et bien au-dessus de la moyenne des sites "passive income". Mais **le contenu seul ne suffit pas pour etre n.1** : il faut absolument le **domaine propre + Search Console + quelques backlinks**. Sans ca, meme 365 super articles resteront invisibles.

Ordre de priorite pour toi :
1. Revoquer la cle API (securite)
2. Brancher le domaine OVH
3. Search Console + sitemap
4. Activer le blog auto (ce systeme)
5. Construire des backlinks petit a petit
6. Me demander les ameliorations ci-dessus une par une
