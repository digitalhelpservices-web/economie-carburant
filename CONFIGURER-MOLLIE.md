# Configurer le paiement Mollie - Guide pas a pas

Ton site est deja pret pour Mollie. Il te reste 4 etapes (15 min).

---

## Comment ca marche (le parcours du client)

1. Le client arrive sur ta page **guide-bareme-ik-2026-pdf.html**
2. Il saisit son **email** dans le champ prevu
3. Il clique **Acheter - 9,99 EUR** -> il est redirige vers la page de paiement **Mollie** (avec ton nom d'entreprise, ton logo)
4. Il paie (carte, Bancontact, etc.)
5. Mollie le renvoie automatiquement vers ta page **merci.html**
6. Sur cette page, il **telecharge le PDF**

Tout est automatique, sans serveur a gerer.

---

## Etape 1 - Creer ton compte Mollie (si pas deja fait)

1. Va sur https://www.mollie.com/fr
2. Cree ton compte avec ton **nom d'entreprise** (il s'affichera sur la page de paiement)
3. Ajoute ton logo et tes couleurs dans **Parametres > Profil** (pour une page de paiement a ton image)
4. Renseigne ton IBAN pour recevoir les paiements

> Mollie verifie ton compte sous 1-2 jours. En attendant, tu peux deja creer le lien en mode test.

---

## Etape 2 - Creer le lien de paiement

1. Dans ton tableau de bord Mollie, menu **Liens de paiement**
2. Clique **Creer** (en haut a droite)
3. Remplis :
   - **Description** : "Guide Bareme IK 2026-2030 (PDF + Excel)"
   - **Montant** : 9,99 EUR
   - **Date d'expiration** : laisse vide (lien reutilisable a l'infini)
4. Clique **Creer**
5. **Copie l'URL** generee (elle ressemble a : `https://paymentlink.mollie.com/payment/xxxxx`)

---

## Etape 3 - Coller le lien dans ton site

1. Ouvre le fichier **guide-bareme-ik-2026-pdf.html**
2. Cherche cette ligne (vers la fin, dans la partie script) :
   ```
   const MOLLIE_PAYMENT_LINK = 'https://paymentlink.mollie.com/payment/VOTRE_LIEN';
   ```
3. Remplace `https://paymentlink.mollie.com/payment/VOTRE_LIEN` par **TON vrai lien** copie a l'etape 2
4. Sauvegarde et pousse le fichier sur GitHub (ou redeploie)

---

## Etape 4 - Configurer la redirection vers merci.html

Pour que le client soit renvoye vers ta page de remerciement apres paiement :

1. Dans Mollie, lors de la creation du lien (ou dans ses parametres), cherche le champ **URL de redirection** (Redirect URL)
2. Mets : `https://economie-carburant.fr/merci.html`
   (ou ton URL Netlify : `https://joyful-salmiakki-9416e9.netlify.app/merci.html` en attendant le domaine)

> Si Mollie ne propose pas la redirection sur les liens simples, utilise l'option "Mollie Checkout" ou garde la page merci accessible : le client recevra de toute facon l'email de confirmation Mollie.

---

## Etape 5 - Remplacer le PDF de demonstration

Le fichier `telechargements/guide-bareme-ik-2026.pdf` est un EXEMPLE.
Remplace-le par ton vrai guide :
1. Mets ton vrai PDF dans le dossier `telechargements/`
2. Garde exactement le meme nom : `guide-bareme-ik-2026.pdf`
   (ou change le nom dans merci.html si tu veux un autre nom)
3. Pousse sur GitHub / redeploie

---

## Important - Limite de cette methode simple

Avec un site statique, le lien de telechargement sur merci.html est **accessible a qui connait l'URL**. Pour 9,99 EUR c'est acceptable (le risque de partage est faible), mais si tu veux une securite forte (lien unique, email avec PDF en piece jointe, anti-partage), il faudra ajouter une **Netlify Function** + le service email **Resend** (gratuit). Dis-le moi et je te construis cette version securisee.

---

## Recapitulatif

- [x] Champ email sur la page guide : FAIT
- [x] Bouton qui redirige vers Mollie : FAIT (lien a coller)
- [x] Page merci.html avec telechargement : FAIT
- [x] Dossier telechargements/ avec PDF : FAIT (PDF a remplacer)
- [ ] Creer le lien Mollie et le coller (toi)
- [ ] Configurer la redirection merci.html (toi)
- [ ] Remplacer le PDF par le vrai (toi)
