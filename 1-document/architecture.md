# Architecture des documents

## Définition

### Flux documentaire

`projet` regroupe les livrables FlowLearn. Sous **`2-en-cours`** : budget, planning, risques, charte, stack, etc. **PBS / WBS / DoD** vivent sous **`3-a-revoir/mvp-pbs/`** ; le flux est : **relecture des docs** → **mise en forme charte** (`2-en-cours/charte-graphique/`) → **copie figée dans `4-termine/`** (voir [`3-a-revoir/README.md`](projet/3-a-revoir/README.md)).

```txt
├── 1-document
│   ├── architecture.md
│   └── projet/
│       ├── 2-en-cours/
│           ├── budgetaire/
│           │   └── budget-previsionnel.md
│           ├── cadrage-projet/
│           │   └── geneses-projet-objectifs.md
│           ├── charte-graphique/
│           │   ├── TODO.md
│           │   └── pages/          // charte HTML
│           ├── plan-de-communication/
│           │   ├── plan-de-communication.md
│           │   └── *.html          // versions exportées
│           ├── planning/
│           │   └── planning-detaille.md
│           ├── risques/
│           │   └── gestion-des-risques.md
│           ├── stack-technique/
│           │   ├── technos.md
│           │   └── mvp-techno.md
│           └── structure-organisation/
│               ├── organisation-general.md
│               └── schema-obs.md
│       ├── 3-a-revoir/             // PBS / WBS / DoD (fichiers + checklist)
│       │   ├── README.md
│       │   ├── pbs-wbs-dod-a-revoir.md
│       │   └── mvp-pbs/
│       │       ├── dod-globale.md
│       │       ├── mvp-definition.md
│       │       ├── mvp-pbs.md
│       │       ├── pbs-globale.md
│       │       ├── dod/
│       │       └── wbs/
│       └── 4-termine/              // après charte + validation (copies figées)
│           └── README.md
└── README.md
```

### Légende des dossiers `2-en-cours`

| Dossier | Contenu |
| --- | --- |
| `budgetaire/` | Budget prévisionnel, enveloppes, contingence |
| `cadrage-projet/` | Genèse du projet, objectifs, périmètre |
| `charte-graphique/` | Identité visuelle, pages HTML de la charte |
| `plan-de-communication/` | Plan com (markdown + exports HTML) |
| `planning/` | Gantt, dépendances, gates, KPI |
| `risques/` | Registre des risques, matrices, plans de réponse |
| `stack-technique/` | Choix technos, variantes MVP techno |
| `structure-organisation/` | Organisation générale, schéma OBS |

### Dossier `3-a-revoir`

| Fichier | Contenu |
| --- | --- |
| `README.md` | **Processus** : relecture des docs → charte graphique → archivage dans `4-termine/` |
| `pbs-wbs-dod-a-revoir.md` | Liste détaillée (liens) vers chaque fichier PBS / WBS / DoD dans `mvp-pbs/` |
| `mvp-pbs/` | MVP, PBS, DoD globale, arborescence PBS, dossiers `dod/` et `wbs/` (contenu **physiquement** ici) |

### Dossier `4-termine`

| Fichier | Contenu |
| --- | --- |
| `README.md` | Livrables **après charte** et validation finale (copies figées) |
