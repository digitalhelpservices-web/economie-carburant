# Blog automatique - Mode d'emploi

Ton blog publie maintenant **un nouvel article chaque jour, tout seul**, sans aucune action de ta part.

---

## Comment ca marche

Un robot gratuit (GitHub Actions) se reveille **chaque matin a 8h** (heure de Paris) et :

1. Genere un nouvel article en combinant 3 sources :
   - **IA** (si tu fournis une cle API) - article redige automatiquement
   - **Actualites RSS** - dernieres news carburant injectees dans l'article (gratuit)
   - **Stock pre-ecrit** - banque d'articles de reserve (gratuit, garanti)
2. Reconstruit la page `blog.html` avec le nouvel article en tete
3. Met a jour le `sitemap.xml` (pour Google)
4. Publie automatiquement sur GitHub -> Netlify met le site a jour tout seul

**Resultat : tu ne touches a rien, jamais. Le blog se remplit chaque jour.**

---

## Activation (a faire UNE SEULE FOIS)

### Etape 1 - Mettre les fichiers sur GitHub
Assure-toi que ces dossiers sont bien dans ton depot GitHub :
- `.github/workflows/blog-quotidien.yml` (le robot)
- `auto-blog/` (le generateur + le stock)

> Important : sur GitHub, verifie que le dossier `.github` est bien present (il commence par un point, certains uploads le cachent).

### Etape 2 - Verifier que le robot est actif
1. Sur GitHub, va dans l'onglet **Actions** de ton depot
2. Tu dois voir "Blog automatique quotidien"
3. Si GitHub demande d'activer les workflows, clique **I understand my workflows, go ahead and enable them**

### Etape 3 - Tester tout de suite (sans attendre demain)
1. Onglet **Actions** -> clique "Blog automatique quotidien"
2. Bouton **Run workflow** -> **Run workflow**
3. Au bout d'1 minute, un nouvel article apparait sur ton site

C'est tout. A partir de la, ca tourne tout seul chaque jour.

---

## Option : activer l'IA (articles plus varies)

Par defaut, le systeme fonctionne **gratuitement** avec le stock + les actus RSS.

Si tu veux des articles 100% rediges par IA (plus de variete), ajoute une cle API :

1. Procure-toi une cle :
   - **Anthropic (Claude)** : https://console.anthropic.com -> tres bon marche (~0,01 $/article)
   - **ou OpenAI** : https://platform.openai.com
2. Sur GitHub : **Settings** -> **Secrets and variables** -> **Actions** -> **New repository secret**
3. Nom : `ANTHROPIC_API_KEY` (ou `OPENAI_API_KEY`) - Valeur : ta cle
4. C'est tout. Le robot detecte la cle et l'utilise automatiquement.

> Sans cle, aucune erreur : le systeme bascule sur le stock + RSS, gratuitement.

---

## Changer l'heure de publication

Dans `.github/workflows/blog-quotidien.yml`, la ligne :
```
- cron: "0 6 * * *"
```
`6` = 6h UTC (8h Paris en ete, 7h en hiver). Pour midi Paris : mets `10`.

---

## Ajouter tes propres sujets au stock

Ouvre `auto-blog/articles-stock.json` et ajoute des entrees sur le meme modele. Plus le stock est grand, plus les articles de secours sont varies.

---

## Surveiller

Onglet **Actions** sur GitHub : chaque execution quotidienne y apparait avec une coche verte (succes) ou une croix rouge (probleme). Tu peux cliquer pour voir les details.
