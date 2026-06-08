# Architecture des documents

## Définition

### Flux documentaire

`projet` regroupe les livrables FlowLearn. Point d’entrée : [`00-guide-lecture.md`](00-guide-lecture.md) (index T-ESP-800 ↔ fichiers).

- **`2-en-cours/`** — cadrage, qualité, specs, budget, planning, risques, stack, OBS/RACI, charte, livret.
- **`3-a-revoir/`** — PBS / WBS / DoD (`mvp-pbs/`) + plan de communication ; relecture → charte → `4-termine/`.
- **`4-termine/`** — copies validées après charte (vide tant que rien n’est figé).

```txt
├── 1-document
│   ├── 00-guide-lecture.md         // index livrables & correspondance jury
│   ├── architecture.md
│   └── projet/
│       ├── 2-en-cours/
│       │   ├── budgetaire/
│       │   ├── cadrage-projet/
│       │   ├── charte-graphique/
│       │   ├── description-fonctionnelle.md
│       │   ├── livret-accueil/
│       │   ├── plan-qualite.md
│       │   ├── planning/
│       │   ├── risques/
│       │   ├── stack-technique/
│       │   └── structure-organisation/   // OBS, orga, matrice-raci
│       ├── 3-a-revoir/
│       │   ├── README.md
│       │   ├── pbs-wbs-dod-a-revoir.md
│       │   ├── mvp-pbs/                  // PBS, WBS, DoD
│       │   └── plan-de-communication/
│       └── 4-termine/
│           └── README.md
└── README.md
```

### Légende `2-en-cours`

| Dossier / fichier | Contenu |
| --- | --- |
| `cadrage-projet/` | Genèse, objectifs SMART |
| `plan-qualite.md` | Processus, tickets, tests, CI, livraisons |
| `description-fonctionnelle.md` | Exigences testables, lien PBS/WBS/OBS/DoD |
| `budgetaire/` | Budget prévisionnel (+ HTML charte) |
| `planning/` | Gantt, gates, KPI |
| `risques/` | Registre des risques |
| `stack-technique/` | Choix technos |
| `structure-organisation/` | Organisation, OBS, **matrice RACI** |
| `charte-graphique/` | Identité visuelle, HTML |
| `livret-accueil/` | Onboarding équipe |

### Dossier `3-a-revoir`

| Élément | Contenu |
| --- | --- |
| `README.md` | Processus relecture → charte → `4-termine/` |
| `mvp-pbs/` | MVP, PBS, WBS, DoD (fichiers de fond) |
| `pbs-wbs-dod-a-revoir.md` | Checklist liens PBS/WBS/DoD |
| `plan-de-communication/` | Plan com HTML + PDF (en relecture) |

### Dossier `4-termine`

| Fichier | Contenu |
| --- | --- |
| `README.md` | Archivage après charte et validation finale |
