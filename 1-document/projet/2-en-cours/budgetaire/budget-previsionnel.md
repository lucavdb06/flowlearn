# FlowLearn — Budget prévisionnel

**Période couverte** : Avril 2026 → Mars 2028 (24 mois)
**Équipe** : 7 personnes rémunérées au SMIC sur l'ensemble de la période
**Cadre** : projet pédagogique Epitech, équipe stable, infrastructure majoritairement gratuite ou open-source

---

## 1. Vue d'ensemble

### 1.1 Objectif

Ce document propose une estimation budgétaire pour le projet FlowLearn sur 24 mois. Il couvre la masse salariale, les abonnements outils, les déplacements (transport/logement), et un **pôle communication structuré** : salons et foires, présence événementielle, supports imprimés, partenariats de visibilité et publicité en ligne — pour faire connaître le projet hors du seul bouche-à-oreille.

L'idée n'est pas de produire un budget ambitieux de levée de fonds, mais un cadrage **réaliste** que l'équipe peut tenir avec ses moyens actuels.

### 1.2 Hypothèses de chiffrage


| #   | Hypothèse                                                                                                              | Commentaire                                                                         |
| --- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| 1   | Équipe stable à 7 personnes sur 24 mois                                                                                | Pas de recrutement, pas de turnover anticipé                                        |
| 2   | Rémunération au SMIC brut + charges (~1 750 €/mois employeur)                                                          | Choix assumé pour un projet étudiant                                                |
| 3   | Pas de bureau privé (équipe en remote ou locaux Epitech)                                                               | Économie ~50 k€/an                                                                  |
| 4   | Infrastructure : 1 VPS mutualisé + stack gratuite ailleurs                                                             | GitHub / Firebase en gratuit tant que le volume le permet                           |
| 5   | Abonnements **payants** : **7 licences** (Cursor, Claude, Notion, Discord, Obsidian) ; **Figma en gratuit** pour les 7 | Maquettes partagées sans poste Pro budgété                                          |
| 6   | Déplacements : missions Paris / Londres / Europe pour rdv et salons                                                    | Transport + nuitées séparés du budget « stand & communication »                     |
| 7   | Communication : salons + visibilité budgétés explicitement                                                             | Stand partagé, kit salon, pub en ligne, événements partenaires (~18 k€ sur 24 mois) |


### 1.3 Synthèse globale


| Pôle                                                      | Total 24 mois | Part       |
| --------------------------------------------------------- | ------------- | ---------- |
| Salaires (7 personnes au SMIC)                            | 294 000 €     | 85,4 %     |
| Abonnements outils & hébergement                          | 11 390 €      | 3,3 %      |
| Déplacements (Paris + Londres + Europe, hors frais salon) | 4 380 €       | 1,3 %      |
| Communication, salons & visibilité                        | 18 000 €      | 5,2 %      |
| **Sous-total**                                            | **327 770 €** | **95,2 %** |
| Provision de sécurité (~5 %)                              | 16 389 €      | 4,8 %      |
| **Total prévisionnel recommandé**                         | **344 159 €** | **100 %**  |


---

## 2. Détail des postes budgétaires

### 2.1 Salaires — 294 000 €

C'est de très loin le plus gros poste du budget (~90 %), ce qui est attendu sur un projet logiciel : la valeur produite, c'est avant tout du temps humain.

**Hypothèse** : 7 personnes payées au SMIC pendant l'intégralité des 24 mois.


| Poste                                      | Mensuel par personne (charge employeur) | Mensuel équipe | Annuel équipe | Total 24 mois |
| ------------------------------------------ | --------------------------------------- | -------------- | ------------- | ------------- |
| 7 × SMIC brut + charges patronales (~22 %) | ~1 750 €                                | 12 250 €       | 147 000 €     | **294 000 €** |


**Choix expliqués** :

- Le SMIC est le seul niveau de rémunération soutenable à notre échelle (équipe étudiante, pas de financement extérieur). Sur le marché de l'IA, un dev expérimenté coûterait 4-5× plus cher.
- L'équipe reste stable à 7 sur 24 mois (pas de recrutement supplémentaire, pas de hiérarchie). On limite les coûts cachés (process RH, formation…).
- Aucune prime, intéressement ou variable n'est budgétée. Si la situation évolue (levée, première vente significative), on rouvrira le sujet.

### 2.2 Abonnements aux outils & hébergement — 11 390 €

Liste des outils et services **payants** (et des gratuits utilisés à l’équipe). **Règle d’équipe** : sur chaque outil **en abonnement**, les **7 personnes** ont un siège payant — pas seulement les profils « tech » ou « design », afin que tout le monde puisse pairer, relire, documenter et intervenir au même niveau.

Tarifs indicatifs mai 2026 (à reconfirmer à la souscription).


| Outil                       | Plan                                                                  | Tarif unitaire                     | Sièges    | Mensuel   | Total 24 mois |
| --------------------------- | --------------------------------------------------------------------- | ---------------------------------- | --------- | --------- | ------------- |
| Cursor Pro                  | IDE assisté par IA                                                    | 20 €/user/mois                     | 7         | 140 €     | 3 360 €       |
| Anthropic Claude Pro        | Assistant IA (rédaction, analyse, veille)                             | 20 €/user/mois                     | 7         | 140 €     | 3 360 €       |
| Notion Plus                 | Documentation & wiki équipe                                           | 10 €/user/mois                     | 7         | 70 €      | 1 680 €       |
| Discord Nitro               | Serveur équipe + communauté (qualité stream, uploads, boosts cumulés) | ~10 €/user/mois                    | 7         | 70 €      | 1 680 €       |
| Obsidian Sync               | Vault partagé / notes synchronisées (prd, rétro, veille)              | 5 €/user/mois                      | 7         | 35 €      | 840 €         |
| Figma                       | Maquettes & prototypage                                               | **Gratuit** (Starter)              | 7 comptes | 0 €       | 0 €           |
| VPS Shifteck (Extreme NVMe) | Backend + base (1 machine partagée par l’équipe)                      | 10 € le 1ᵉʳ mois puis 19,99 €/mois | 1 serveur | ~20 €     | 470 €         |
| GitHub                      | Repo + CI/CD + Actions                                                | Free plan                          | 7         | 0 €       | 0 €           |
| Firebase Analytics          | Analytics produit                                                     | Free tier                          | –         | 0 €       | 0 €           |
| **Total**                   |                                                                       |                                    |           | **475 €** | **11 390 €**  |


**Choix expliqués** :

- **7 × Cursor** : tout le monde peut faire du pair programming, relire du code et extraire du contexte du repo sans « emprunter » la machine d’un dev. Ça coûte plus cher qu’un découpage 4 devs / 3 autres, mais c’est plus simple en organisation (pas de gestion de comptes « nominatifs » qui bloquent).
- **7 × Claude Pro** : même logique pour les specs, les comptes-rendus, la veille marché et l’aide à la com. On reste en **Pro** (20 €/user) plutôt qu’en **Team** (souvent ~25 €/user min. 5 sièges) tant que les besoins « workspace partagé » restent couverts par Notion.
- **Notion, Discord, Obsidian ×7** : une seule stack de doc + comm + notes pour toute l’équipe, sans exemptions.
- **Figma gratuit (7 comptes)** : tout le monde peut commenter et éditer dans les limites du **plan Starter** (fichiers / projets gratuits, pas de bibliothèques d’équipe avancées). Si un blocage apparaît (handoff lourd, composants partagés à grande échelle), on arbitrera une **montée en Professional** ou un **plan Education** si l’école le permet.
- **VPS Shifteck** : une seule machine pour le backend ; le coût n’est pas multiplié par 7 (c’est une infrastructure commune).
- **GitHub & Firebase** : pas d’abonnement payant au niveau prévu ; les **7 contributeurs** restent sur le **plan gratuit** GitHub (équipe à taille de repo modérée) et Firebase **Spark** tant que le volume d’événements reste faible.

> **Note** : si l’école ou Epitech fournit déjà des licences (ex. Notion Education, **Figma Education** pour débloquer plus de fichiers / bibliothèques sans payer), on peut **réduire ou éviter** certains postes après vérification des conditions — le tableau ci-dessus représente le cas « on paie nous-mêmes » sur les outils listés en payant.

### 2.3 Déplacements (transport & hébergement) — 4 380 €

**Hors** frais de stand/salon : ceux-ci sont dans la section **2.4 Communication**.


| Activité                                                        | Fréquence                   | Coût unitaire | Total 24 mois |
| --------------------------------------------------------------- | --------------------------- | ------------- | ------------- |
| Missions Paris (TGV + 1 nuit Airbnb + repas)                    | 3 par an, soit 6 missions   | ~280 €        | 1 680 €       |
| Missions Londres (Eurostar/avion + 2 nuits + repas)             | 2 par an, soit 4 missions   | ~500 €        | 2 000 €       |
| Conférences / meetups Europe (Bruxelles, Amsterdam, Berlin, FR) | 2 par an, soit 4 événements | ~175 €        | 700 €         |
| **Total**                                                       |                             |               | **4 380 €**   |


**Choix expliqués** :

- **Paris en mission régulière** (3/an) : partenaires écoles, préparation salons. Budget optimisé (TGV réservé tôt + Airbnb).
- **Londres** (2/an) : hub EdTech UK (dont **Bett Show** en janvier) ; le voyage et l'hébergement sont ici, le **coût de participation / stand / kit** est en 2.4.
- **Conférences européennes ponctuelles** : vol low-cost + 1 nuit si événement pertinent.
- Pas de séminaire d'équipe budgété (l'équipe est déjà réunie au quotidien).

### 2.4 Communication, salons & visibilité — 18 000 €

Enveloppe dédiée pour **être vus** : foires et salons, présence partenaire, supports physiques, petites actions terrain et push digital. Chiffres volontairement **supérieurs** au seul « quelques pubs », pour ne pas sous-estimer le coût réel d'une présence crédible sur un salon.


| Poste                                      | Détail                                                                                                                                                                                      | Total 24 mois |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Salons & foires EdTech / éducation**     | 3 participations sur 24 mois (ex. Bett UK, salon FR ou EU régional, événement campus / learning) — stand **partagé**, corner partenaire ou table projet étudiant (pas de grand stand perso) | 8 700 €       |
| **Kit présence salon**                     | Roll-up, flyers A5, QR code, goodies légers, impressions badges                                                                                                                             | 1 600 €       |
| **Événements & concours**                  | Frais d'inscription pitch / hackathon / startup contest, déplacement complémentaire si une équipe est sélectionnée (hors ligne 2.3 quand c'est intégré dans un forfait)                     | 1 500 €       |
| **Relations presse & annonces**            | Communiqués, relais réseaux presse école / assos, éventuellement petit budget « visibilité média » locale                                                                                   | 700 €         |
| **Partenariats & co-visibilité**           | Logo sur support partenaire, petite bannière événement, co-animateur atelier avec une école / asso                                                                                          | 1 200 €       |
| **Terrain & animation**                    | Mini ateliers / démos (prévoir café, prints, location salle modeste si besoin)                                                                                                              | 900 €         |
| **Publicité en ligne**                     | TikTok + Meta + boosts LinkedIn ciblés (lancement et pics salon) — **après** premier feedback utilisateurs (ex. M9+)                                                                        | 1 500 €       |
| **SEA / recherche ciblée (pilote)**        | Campagne Google Ads très limitée sur mots-clés de marque + EdTech, pour capter les curieux post-salon                                                                                       | 700 €         |
| **Micro-influence / contenus sponsorisés** | 2-3 collaborations modestes avec micro-créateurs éducation / étudiants (honoraires symboliques + produit)                                                                                   | 700 €         |
| **Outils communication**                   | Newsletter payante légère si besoin (ex. Mailchimp plan bas), nom de domaine dédié landing produit                                                                                          | 500 €         |
| **Total**                                  |                                                                                                                                                                                             | **18 000 €**  |


**Choix expliqués** :

- **Les salons coûtent cher même en mode étudiant** : une participation « sérieuse » (même en stand partagé) se situe souvent entre **2 000 € et 4 000 €** par événement selon l'organisateur. On budgète **3 × ~2 900 € en moyenne ≈ 8 700 €** sur 24 mois (ajustable si tarif réduit ou partenariat école).
- **Le digital complète le terrain** : la pub en ligne et le pilote SEA ne remplacent pas le salon ; elles prolongent l'effet (QR code, recherche après l'événement).
- **Micro-influence** : budget volontairement modeste ; l'idée est d'acheter du **credibility** étudiante, pas du reach massif.
- Si une année ne prévoit **aucun** gros salon, la ligne peut être basculée vers plus de pub ou un second événement partenaire (arbitrage trimestriel, cf. gouvernance).

---

## 3. Synthèse budgétaire

### 3.1 Récapitulatif par poste


| Catégorie                                     | Mensuel moyen | Annuel (moy. sur 2 ans) | Total 24 mois |
| --------------------------------------------- | ------------- | ----------------------- | ------------- |
| Salaires (7 SMIC charges incluses)            | 12 250 €      | 147 000 €               | 294 000 €     |
| Abonnements outils & hébergement (VPS inclus) | 475 €         | 5 695 €                 | 11 390 €      |
| Déplacements (hors frais salon)               | 183 €         | 2 190 €                 | 4 380 €       |
| Communication, salons & visibilité            | 750 €         | 9 000 €                 | 18 000 €      |
| **Sous-total**                                | **13 657 €**  | **163 885 €**           | **327 770 €** |
| Provision de sécurité (~5 %)                  | 683 €         | 8 195 €                 | 16 389 €      |
| **Total recommandé**                          | **14 340 €**  | **172 080 €**           | **344 159 €** |


> *Le mensuel moyen du sous-total (13 657 €) correspond à 327 770 € ÷ 24. La ligne « outils » est affichée à **475 €/mois** (ordre de grandeur) alors que le total 24 mois **11 390 €** fait foi (section 2.2).*

> **Note importante** : ces valeurs sont des estimations de cadrage pour un projet pédagogique. Elles ne tiennent pas compte d'un éventuel financement externe (subvention, bourse French Tech, ou levée de fonds), qui modifierait la structure du budget. Avant validation finale, vérifier les tarifs SaaS au moment de la souscription, le nombre exact de sièges payants par outil, et le périmètre exact des déplacements (devis transport/hébergement réels).

### 3.2 Logique de la provision de sécurité

Les **16 389 €** de provision (~5 % du sous-total hors provision) couvrent les imprévus suivants :

- **Hausse de tarifs SaaS** : les éditeurs (Notion, Cursor, Claude…) augmentent régulièrement leurs prix.
- **Frais administratifs** : compte bancaire pro, expert-comptable ponctuel, frais juridiques de base.
- **Casse matérielle** : remplacement d'un laptop ou d'un téléphone de test.
- **Déplacements non prévus** : opportunité de présenter le projet à un événement non identifié au départ.

La provision **ne sert jamais aux dépenses normales**. Si elle est consommée à plus de 50 % avant M18, on déclenche une revue en équipe.

---

## 4. Gouvernance et suivi

### 4.1 Rythme de revue

- **Revue mensuelle** : le premier lundi du mois, l'équipe compare le réel au prévisionnel par catégorie. 30 minutes max.
- **Arbitrage trimestriel** : tous les 3 mois, on décide si on ajuste les abonnements (ajout d'un siège, suppression d'un outil non utilisé), si on lance ou non une vague de pub, et si on confirme les déplacements du trimestre suivant.
- **Bilan annuel** : à la fin de chaque année (M12 puis M24), bilan budgétaire complet pour préparer la suite.

### 4.2 Indicateurs de pilotage


| Indicateur                             | Cible                                    | Seuil d'alerte           |
| -------------------------------------- | ---------------------------------------- | ------------------------ |
| Coût réel mensuel total                | ≤ 14 700 €                               | > 16 200 € sur 1 mois    |
| Cumul annuel vs budget validé          | ≤ 100 %                                  | > 110 %                  |
| Consommation de la provision           | ≤ 30 % à mi-parcours (M12)               | > 50 % avant M12         |
| Nombre de sièges payants par outil     | suivi mensuel (Notion / Cursor / Claude) | augmentation non décidée |
| Coût publicitaire / installation (CPI) | ≤ 2 € en phase de test                   | > 5 € durable            |


### 4.3 Règles d'or

1. **Aucun nouvel abonnement** sans validation en revue mensuelle.
2. **La provision de sécurité ne sert jamais à payer un dépassement de budget normal**, uniquement à couvrir un vrai imprévu.
3. **Tout dépassement supérieur à 10 %** d'un poste budgétaire déclenche une note explicative de la personne responsable du poste.
4. **Communication** : pas de dépense pub majeure avant retours utilisateurs (repère **M9+**). En phase active, le **digital** (ligne 2.4) reste piloté mois par mois ; le **salon** se valide à l'arbitrage trimestriel (devis réel obligatoire avant engagement).

---

**Document maintenu par** : équipe FlowLearn
**Version** : 2.3