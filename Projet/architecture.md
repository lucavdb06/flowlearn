# Architecture des documents

## Définition

### Principe d'organisation

`Projet/` regroupe l'ensemble de la documentation FlowLearn. Point d'entrée :
[`FlowLearn-Guide-Lecture.html`](FlowLearn-Guide-Lecture.html) (index T-ESP-800 ↔ fichiers).

L'arborescence est **à plat par sujet** : il n'y a plus d'étapes `2-en-cours/`,
`3-a-revoir/` ou `4-termine/`. Chaque livrable vit dans son **dossier-sujet** sous
`Projet/Document/`.

**Convention de chaque dossier-sujet :**

- la version **HTML (charte graphique)** reste visible à la racine du dossier ;
- les **sources `.md`** (et anciennes versions) sont rangées dans un sous-dossier **`archives/`**.

La feuille de style commune `flowlearn-document.css` et le logo sont centralisés dans
`Document/charte-graphique/`.

```txt
Lucavdb06-flowlearn/
├── README.md
├── .gitignore
└── Projet/
    ├── FlowLearn-Guide-Lecture.html   // guide de lecture : index des livrables (correspondance jury)
    ├── architecture.md                // ce document
    ├── media/
    │   └── FlowLearn_MVP_Engineering_Blueprint.pdf
    └── Document/
        ├── Geneses-Projet-Objectifs/  // cadrage : genèse & objectifs
        ├── structure-organisation/    // OBS, RACI, compétences, orga, manuel
        │   ├── FlowLearn-Carte-Competences/
        │   ├── FlowLearn-Matrice-RACI/
        │   ├── Manuel-utilisateur/
        │   ├── Organisation-Generale/
        │   ├── schema-obs/
        │   └── archives/              // description fonctionnelle, plan qualité, matrice, OBS (.md)
        ├── mvp-pbs-dod/               // MVP, PBS, WBS, DoD
        │   ├── mvp/
        │   ├── pbs/
        │   ├── wbs/
        │   ├── dod/
        │   └── pbs-wbs-dod-a-revoir.html
        ├── budgetaire/               // budget prévisionnel
        ├── stack-technique/          // synthèse technique & choix technos
        ├── planning/                 // Gantt, jalons
        ├── risques/                  // registre des risques
        ├── plan-de-communication/    // plan com (HTML + PDF)
        ├── livret-accueil/           // onboarding équipe / manuel utilisateur
        └── charte-graphique/         // identité visuelle
            ├── charte-graphique.html
            ├── assets/flowlearn-logo.svg
            ├── archives/flowlearn-document.css   // CSS partagée des livrables
            └── figma/
```

### Légende des dossiers-sujets (`Projet/Document/`)

| Dossier | Contenu |
| --- | --- |
| `Geneses-Projet-Objectifs/` | Note de cadrage : genèse, objectifs SMART |
| `structure-organisation/` | Organisation générale, **OBS** (`schema-obs/`), **matrice RACI**, **carte des compétences**, **manuel utilisateur** ; `archives/` contient description fonctionnelle, plan qualité, matrice-raci et schema-obs en `.md` |
| `mvp-pbs-dod/` | **MVP** (`mvp/`), **PBS** (`pbs/`), **WBS** (`wbs/`), **DoD** (`dod/`) ; `pbs-wbs-dod-a-revoir.html` = index de relecture |
| `budgetaire/` | Budget prévisionnel (HTML charte + source `.md`) |
| `stack-technique/` | Synthèse technique et choix des technologies |
| `planning/` | Planning détaillé et diagramme de Gantt |
| `risques/` | Registre et gestion des risques |
| `plan-de-communication/` | Plan de communication (HTML + PDF archivé) |
| `livret-accueil/` | Livret d'accueil et manuel utilisateur |
| `charte-graphique/` | Identité visuelle, logo (`assets/`), CSS partagée (`archives/flowlearn-document.css`), maquettes (`figma/`) |

### Détail `mvp-pbs-dod/`

| Élément | Contenu |
| --- | --- |
| `mvp/` | Définition du MVP (`mvp-definition.html`, `mvp-pbs.html`) |
| `pbs/` | PBS globale (`pbs-globale.html`) |
| `wbs/` | WBS globale (`schema-wbs-global.html`) + un dossier par lot (1 à 5) |
| `dod/` | DoD globale (`dod-globale.html`) + un dossier par lot (1 à 5) |
| `pbs-wbs-dod-a-revoir.html` | Checklist de relecture avec liens vers chaque `.html` |
| `**/archives/` | Sources `.md` de chaque PBS / WBS / DoD |

### Convention HTML / archives

Chaque dossier-sujet présente sa **version HTML** mise au format de la
[charte graphique](Document/charte-graphique/charte-graphique.html) (CSS partagée
`flowlearn-document.css`). Les **sources Markdown** correspondantes sont conservées dans
le sous-dossier `archives/` du même dossier, pour garder l'historique sans encombrer la vue.
