# FlowLearn — Guide de lecture des livrables

> Version charte : [`FlowLearn-Guide-Lecture.html`](FlowLearn-Guide-Lecture.html)

**Formation :** T-ESP-800  
**Dépôt équipe :** [github.com/lucavdb06/flowlearn](https://github.com/lucavdb06/flowlearn)

Ce document indique **quels fichiers lire**, **à quoi ils répondent** (attendus jury / pilotage) et **où ils se trouvent** dans l’arborescence. Il ne remplace pas le contenu des livrables : il sert d’index.

---

## 1. Mots simples

| Mot | Sens |
| --- | --- |
| **MVP** | Première version utile et montrable (pas tout le produit final). |
| **PBS** | Découpage du **produit** : ce que le logiciel contient. |
| **WBS** | Découpage du **travail** : ce que l’équipe doit faire. |
| **OBS** | Organisation : qui fait quoi (rôles, gouvernance). |
| **RACI** | Qui **R**éalise, **A**pprouve, est **C**onsulté, est **I**nformé. |
| **DoD** | Critères pour dire qu’une tâche est vraiment terminée. |
| **Staging** | Environnement de test proche de la prod, avant démo ou livraison. |
| **CI/CD** | Automatisation (tests, déploiement) sur chaque changement de code. |

---

## 2. Correspondance attendus T-ESP-800 ↔ FlowLearn

Numérotation inspirée du référentiel livrables (cadrage, qualité, specs, PBS, WBS, etc.). Les chemins sont relatifs à `1-document/`.

| N° | Livrable type | Fichier FlowLearn | Dossier flux |
| --- | --- | --- | --- |
| **00** | Guide de lecture | [`00-guide-lecture.md`](00-guide-lecture.md) | racine `1-document/` |
| **01** | Note de cadrage | [`projet/2-en-cours/cadrage-projet/geneses-projet-objectifs.md`](projet/2-en-cours/cadrage-projet/geneses-projet-objectifs.md) | `2-en-cours` |
| **02** | Plan qualité | [`projet/2-en-cours/plan-qualite.md`](projet/2-en-cours/plan-qualite.md) | `2-en-cours` |
| **03** | Description fonctionnelle | [`projet/2-en-cours/description-fonctionnelle.md`](projet/2-en-cours/description-fonctionnelle.md) | `2-en-cours` |
| **04** | PBS | [`projet/3-a-revoir/mvp-pbs/pbs-globale.md`](projet/3-a-revoir/mvp-pbs/pbs-globale.md) + [`mvp-pbs.md`](projet/3-a-revoir/mvp-pbs/mvp-pbs.md) | `3-a-revoir` |
| **05** | WBS | [`projet/3-a-revoir/mvp-pbs/wbs/`](projet/3-a-revoir/mvp-pbs/wbs/) | `3-a-revoir` |
| **06** | OBS + RACI | [`projet/2-en-cours/structure-organisation/schema-obs.md`](projet/2-en-cours/structure-organisation/schema-obs.md) + [`matrice-raci.md`](projet/2-en-cours/structure-organisation/matrice-raci.md) | `2-en-cours` |
| **07** | Definition of Done | [`projet/3-a-revoir/mvp-pbs/dod-globale.md`](projet/3-a-revoir/mvp-pbs/dod-globale.md) + [`dod/`](projet/3-a-revoir/mvp-pbs/dod/) | `3-a-revoir` |
| **08** | Besoins & budget | [`projet/2-en-cours/budgetaire/budget-previsionnel.md`](projet/2-en-cours/budgetaire/budget-previsionnel.md) + [`stack-technique/`](projet/2-en-cours/stack-technique/) | `2-en-cours` |
| **09** | Planning & suivi | [`projet/2-en-cours/planning/planning-detaille.md`](projet/2-en-cours/planning/planning-detaille.md) | `2-en-cours` |
| **10** | Gestion des risques | [`projet/2-en-cours/risques/gestion-des-risques.md`](projet/2-en-cours/risques/gestion-des-risques.md) | `2-en-cours` |
| **11** | Communication & identité | [`projet/3-a-revoir/plan-de-communication/`](projet/3-a-revoir/plan-de-communication/) + [`projet/2-en-cours/charte-graphique/`](projet/2-en-cours/charte-graphique/) | `3-a-revoir` + `2-en-cours` |
| **12** | Livret d’accueil | [`projet/2-en-cours/livret-accueil/livret-accueil.md`](projet/2-en-cours/livret-accueil/livret-accueil.md) | `2-en-cours` |
| — | Architecture dépôt | [`architecture.md`](architecture.md) | racine `1-document/` |
| — | Organisation & gouvernance | [`projet/2-en-cours/structure-organisation/organisation-general.md`](projet/2-en-cours/structure-organisation/organisation-general.md) | `2-en-cours` |

---

## 3. Flux des dossiers `projet/`

| Dossier | Rôle |
| --- | --- |
| **`2-en-cours/`** | Travail actif : cadrage, qualité, specs, budget, planning, risques, stack, OBS, charte HTML, livret. |
| **`3-a-revoir/`** | Fond **PBS / WBS / DoD** (`mvp-pbs/`) + **plan de communication** en cours de relecture. Processus : relecture → charte → archivage. |
| **`4-termine/`** | Copies **validées** après charte et accord équipe (vide tant que rien n’est figé). |

Détail du processus : [`projet/3-a-revoir/README.md`](projet/3-a-revoir/README.md).

---

## 4. Par où commencer ?

| Profil | Lire en priorité |
| --- | --- |
| **Nouveau membre** | Livret → organisation générale → OBS → plan qualité → DoD globale |
| **Jury / soutenance courte** | Cadrage → description fonctionnelle → DoD globale → budget → planning → risques |
| **Relecture PBS/WBS/DoD** | [`projet/3-a-revoir/pbs-wbs-dod-a-revoir.md`](projet/3-a-revoir/pbs-wbs-dod-a-revoir.md) |
| **Com & charte** | Plan com (`3-a-revoir`) puis pages HTML `charte-graphique/` |

---

## 5. Versions « charte » (HTML / PDF)

Certains livrables existent aussi en **mise en forme charte** (CSS partagée `flowlearn-document.css`) :

| Sujet | Fichier HTML |
| --- | --- |
| Guide de lecture | [`FlowLearn-Guide-Lecture.html`](FlowLearn-Guide-Lecture.html) |
| Plan qualité | [`projet/2-en-cours/FlowLearn-Plan-Qualite.html`](projet/2-en-cours/FlowLearn-Plan-Qualite.html) |
| Description fonctionnelle | [`projet/2-en-cours/FlowLearn-Description-Fonctionnelle.html`](projet/2-en-cours/FlowLearn-Description-Fonctionnelle.html) |
| Matrice RACI | [`projet/2-en-cours/structure-organisation/FlowLearn-Matrice-RACI.html`](projet/2-en-cours/structure-organisation/FlowLearn-Matrice-RACI.html) |
| Budget | [`projet/2-en-cours/budgetaire/Flowlearn budget-previsionnel.html`](projet/2-en-cours/budgetaire/Flowlearn%20budget-previsionnel.html) |
| Charte | [`projet/2-en-cours/charte-graphique/charte-graphique.html`](projet/2-en-cours/charte-graphique/charte-graphique.html) |
| Communication | [`projet/3-a-revoir/plan-de-communication/FlowLearn-Plan-Communication.html`](projet/3-a-revoir/plan-de-communication/FlowLearn-Plan-Communication.html) (+ PDF dans le même dossier) |
| PBS / WBS / DoD (à revoir) | Un `.html` charte par `.md` dans [`projet/3-a-revoir/mvp-pbs/`](projet/3-a-revoir/mvp-pbs/) — index : [`pbs-wbs-dod-a-revoir.html`](projet/3-a-revoir/pbs-wbs-dod-a-revoir.html) |

Les versions figées validées iront dans **`4-termine/`** une fois l’équipe d’accord.
