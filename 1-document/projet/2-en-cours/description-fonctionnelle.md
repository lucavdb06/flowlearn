# FlowLearn — Description fonctionnelle logicielle

Ce que le logiciel doit faire, comment il est découpé, et comment relier **exigences ↔ PBS ↔ WBS ↔ OBS ↔ DoD**.

Sources détaillées : [`../3-a-revoir/mvp-pbs/`](../3-a-revoir/mvp-pbs/) (PBS, WBS, DoD par lot).

---

## 1. Objet

Décrire le **comportement attendu** du MVP FlowLearn et la **traçabilité** vers les livrables de découpage et d’organisation.

---

## 2. Description générale du produit

FlowLearn est une plateforme d’**apprentissage par micro-sessions ludiques** : l’utilisateur construit une base de connaissances (import, dialogue IA) et la révise via des **expériences** (quiz, jeux, scroll éducatif, etc.) branchées sur un **noyau commun** (API, RAG, MCP).

**Périmètre MVP (v0.1)** : noyau RAG + au moins deux modes d’expérience + conteneur multiplateforme + algorithmes de rétention de base + socle sécurité/RGPD. Voir [cadrage](cadrage-projet/geneses-projet-objectifs.md) pour objectifs SMART.

---

## 3. Vue synthétique PBS (lots produit)

| ID | Bloc produit | Contenu (résumé) | Priorité MVP |
| --- | --- | --- | --- |
| **1** | Conteneur multiplateforme | Electron, Capacitor, shell React | Must |
| **2** | Jeux & expériences | API RAG↔jeux, quiz, Godot (Archero / VS-like), IoT optionnel | Must |
| **3** | Intelligence centrale / RAG | FastAPI, base vectorielle, ingestion, orchestrateur, générateurs LLM | Must |
| **4** | Algorithmes personnalisation | Sélection questions, rétention (type Anki / flow) | Must |
| **5** | Sécurité & gouvernance | Coffre-fort données, RGPD | Must |

Détail arborescence : [`../3-a-revoir/mvp-pbs/pbs-globale.md`](../3-a-revoir/mvp-pbs/pbs-globale.md), [`mvp-pbs.md`](../3-a-revoir/mvp-pbs/mvp-pbs.md).

---

## 4. Exigences fonctionnelles testables (extraits)

Chaque exigence doit être vérifiable via scénario de test ou critère DoD.

| ID | Exigence | Critère de validation | Lot PBS |
| --- | --- | --- | --- |
| **EF-01** | Importer un document (PDF/texte) dans la base | Fichier indexé, consultable pour génération QCM | 3 |
| **EF-02** | Générer un quiz JSON à partir du cours | QCM valide, questions liées au contenu importé | 3 |
| **EF-03** | Jouer une session quiz avec score | Enchaînement question → réponse → score final | 2 |
| **EF-04** | Alimenter un jeu via l’API RAG | Le gameplay reçoit des questions du module cours | 2 |
| **EF-05** | Proposer la « prochaine question à revoir » | Priorité cartes dues puis nouvelles (algo rétention) | 4 |
| **EF-06** | Exécuter l’app sur web + au moins une cible desktop ou mobile | Build encapsulateur fonctionnel | 1 |
| **EF-07** | Données utilisateur protégées (chiffrement / RGPD) | Checklist DoD lot 5 validée | 5 |

Liste complète des mécaniques : [`../3-a-revoir/mvp-pbs/mvp-definition.md`](../3-a-revoir/mvp-pbs/mvp-definition.md).

---

## 5. Vue synthétique WBS (lots travail)

| Lot | Thème | Fichiers WBS |
| --- | --- | --- |
| 1 | Encapsulateurs | [`wbs/1-conteneur-multiplateforme/`](../3-a-revoir/mvp-pbs/wbs/1-conteneur-multiplateforme/) |
| 2 | Jeux & API | [`wbs/2-jeux-et-experiences/`](../3-a-revoir/mvp-pbs/wbs/2-jeux-et-experiences/) |
| 3 | RAG / backend | [`wbs/3-intelligence-centrale-module-rag/`](../3-a-revoir/mvp-pbs/wbs/3-intelligence-centrale-module-rag/) |
| 4 | Algorithmes | [`wbs/4-algorithmes-personnalisation/`](../3-a-revoir/mvp-pbs/wbs/4-algorithmes-personnalisation/) |
| 5 | Sécurité | [`wbs/5-securite-gouvernance-donnees/`](../3-a-revoir/mvp-pbs/wbs/5-securite-gouvernance-donnees/) |

Schéma global : [`../3-a-revoir/mvp-pbs/wbs/schema-wbs-global.md`](../3-a-revoir/mvp-pbs/wbs/schema-wbs-global.md).

---

## 6. Lien OBS & RACI

- **OBS** (rôles, gouvernance) : [`structure-organisation/schema-obs.md`](structure-organisation/schema-obs.md)
- **RACI** (matrice par activité) : [`structure-organisation/matrice-raci.md`](structure-organisation/matrice-raci.md)

---

## 7. Lien DoD

- **DoD globale** : [`../3-a-revoir/mvp-pbs/dod-globale.md`](../3-a-revoir/mvp-pbs/dod-globale.md)
- **DoD par feature** : [`../3-a-revoir/mvp-pbs/dod/`](../3-a-revoir/mvp-pbs/dod/)

Une exigence **EF-xx** est considérée livrée lorsque le lot WBS associé est **Done** selon la DoD correspondante.

---

## 8. Stack & contraintes techniques

Référence : [`stack-technique/technos.md`](stack-technique/technos.md), [`mvp-techno.md`](stack-technique/mvp-techno.md).
