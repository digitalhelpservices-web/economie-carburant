# Guide : Analytics + Indexation Google + Bing

Ce guide regroupe les 3 etapes pour suivre ton trafic et faire indexer ton site.
A faire dans l'ordre, UNE FOIS que economie-carburant.fr est en ligne avec HTTPS.

---

## ETAPE 1 - Google Analytics (suivre ton trafic)

### Creer ton compte et ta propriete
1. Va sur **analytics.google.com**
2. Connecte-toi avec ton compte Google
3. Clique **Commencer la mesure** (ou Administration > Creer > Propriete)
4. Nom du compte : "Economie-Carburant" (parametres de partage par defaut : OK)
5. Nom de la propriete : "Site Economie-Carburant"
6. Fuseau horaire : France (Paris) - Devise : Euro
7. Renseigne le secteur (ex : Finance/Automobile) et la taille (Petite)

### Creer le flux de donnees et recuperer ton ID
8. Choisis la plateforme **Web**
9. URL du site : `https://economie-carburant.fr` - Nom du flux : "Site"
10. Laisse "Mesure amelioree" cochee (suivi automatique des clics, scroll, etc.)
11. Clique **Creer le flux**
12. **COPIE ton ID de mesure** : il est en haut a droite, au format **G-XXXXXXXXXX**

### Mettre ton ID dans le site
- Dans tous les fichiers HTML, cherche `G-XXXXXXXXXX` (Ctrl+F)
- Remplace par TON vrai ID (ex : G-AB12CD34EF)
- OU demande a Claude de le faire sur toutes les pages d'un coup, puis redeploie

> Une fois en ligne, reviens sur Analytics > Temps reel et ouvre ton site :
> tu devrais te voir apparaitre comme visiteur actif. C'est la preuve que ca marche.

---

## ETAPE 2 - Google Search Console (faire indexer par Google)

### Ajouter et verifier le domaine
1. Va sur **search.google.com/search-console**
2. Connecte-toi (meme compte Google que Analytics, c'est plus simple)
3. **Ajouter une propriete** > type **Domaine** (colonne de gauche)
4. Tape `economie-carburant.fr`
5. Google te donne un enregistrement **TXT** (commence par `google-site-verification=...`)
6. Chez OVH > Zone DNS > Ajouter une entree > type **TXT** > colle ce code (sous-domaine vide)
7. Attends quelques minutes, reviens sur Search Console > **Valider**

### Soumettre le sitemap
8. Menu **Sitemaps** (a gauche)
9. Tape `sitemap.xml`
10. Clique **Envoyer**
> C'est ce qui dit a Google : "voici toutes mes pages, viens les indexer."

### Forcer l'indexation des pages cles (optionnel mais utile)
11. Barre du haut "Inspection d'URL" > colle l'URL de ta page d'accueil
12. Clique **Demander une indexation**
13. Refais-le pour : bareme IK, comparatif carburants, guide PDF

---

## ETAPE 3 - Bing Webmaster Tools (faire indexer par Bing + IA)

> Important : Bing alimente ChatGPT et Copilot. Utile pour etre cite par les IA.

### Le plus rapide : importer depuis Google
1. Va sur **bing.com/webmasters**
2. Connecte-toi (compte Microsoft OU Google)
3. Cherche l'option **Importer depuis Google Search Console**
4. Autorise > Bing reprend ton site et ton sitemap automatiquement

### Sinon, manuellement
- Ajoute `economie-carburant.fr`
- Verifie (par DNS TXT, comme pour Google, ou via le fichier de verification)
- Menu Sitemaps > soumets `https://economie-carburant.fr/sitemap.xml`

---

## ETAPE 4 - Patienter et suivre

- L'indexation prend de quelques JOURS a quelques SEMAINES. Normal.
- Si Search Console affiche "0 page indexee" au debut : c'est normal, attends.
- Reviens chaque semaine voir : Search Console > Pages (indexation) et Performances (clics).
- Analytics > Rapports : tu verras le trafic, les pages vues, les sources.

---

## RAPPEL HONNETE

Etre indexe = Google CONNAIT ton site.
Etre premier = il faut du TEMPS, du contenu regulier (ton blog auto aide), et des
backlinks (sites qui parlent de toi). Ne sois pas decu si le trafic met du temps :
un site neuf met souvent 3 a 6 mois a decoller. C'est la patience qui paie ici.

---

## CHECKLIST RAPIDE

- [ ] GA4 cree, ID G-XXXX recupere
- [ ] ID colle dans le site (toutes les pages) + redeploye
- [ ] Search Console : domaine verifie (TXT chez OVH)
- [ ] Search Console : sitemap.xml soumis
- [ ] Pages cles : indexation demandee
- [ ] Bing : importe depuis Google (ou ajoute manuellement)
- [ ] Verifie Analytics Temps reel (tu te vois en visitant le site)
