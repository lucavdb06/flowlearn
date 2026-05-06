# Architecture des documents

## Définition

### Flux documentaire

`projet` regroupe les livrables rédigés pour FlowLearn. Le travail actif est sous **`2-en-cours`** : les thèmes proches partagent un même sous-dossier (budget, planning, risques, MVP / PBS / DoD / WBS, etc.). Le dossier **`3-a-revoir`** sert uniquement de **mémo** (quoi relire en priorité vs rien à classer en « terminé » pour le moment).

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
│           ├── mvp-pbs/
│           │   ├── dod-globale.md
│           │   ├── mvp-definition.md
│           │   ├── mvp-pbs.md
│           │   ├── pbs-globale.md
│           │   ├── dod/            // Definition of Done par lot PBS
│           │   └── wbs/            // WBS + schema-wbs-global.md
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
│       └── 3-a-revoir/             // suivi : priorité de relecture (voir README)
│           └── README.md
└── README.md
```

### Légende des dossiers `2-en-cours`

| Dossier | Contenu |
| --- | --- |
| `budgetaire/` | Budget prévisionnel, enveloppes, contingence |
| `cadrage-projet/` | Genèse du projet, objectifs, périmètre |
| `charte-graphique/` | Identité visuelle, pages HTML de la charte |
| `mvp-pbs/` | MVP, PBS, DoD globale, arborescence PBS, dossiers `dod/` et `wbs/` |
| `plan-de-communication/` | Plan com (markdown + exports HTML) |
| `planning/` | Gantt, dépendances, gates, KPI |
| `risques/` | Registre des risques, matrices, plans de réponse |
| `stack-technique/` | Choix technos, variantes MVP techno |
| `structure-organisation/` | Organisation générale, schéma OBS |

### Dossier `3-a-revoir`

| Fichier | Contenu |
| --- | --- |
| `README.md` | Rappel du périmètre **PBS / WBS / DoD** à revoir ; section **Terminer** vide pour l’instant |
