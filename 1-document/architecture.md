# Architecture des documents

## Définition

### Flux documentaire

`projet` : contient une arborescence de dossiers qui représente le flux de création d'un document. Les dossiers `2-en-cours` et `3-relecture` forment une boucle tant que la relecture n'est pas validée.

```txt
├── 1-document
│   ├── architecture.md
│   └── projet/
│       ├── 1-a-faire/            // structure du document pas encore définie
│       ├── 2-en-cours/           // travail en cours (todo défini dans le document)
│       │   ├── budget-previsionnel.md
│       │   ├── plan-de-communication.md
│       │   ├── livret-accueil.md
│       │   ├── schema-obs.md
│       │   ├── gestion-des-risques.md
│       │   ├── technos.md
│       │   ├── dod/
│       │   │   ├── 1-conteneur-multiplateforme/
│       │   │   │   └── dod-1.1-encapsulateurs.md
│       │   │   ├── 2-jeux-et-experiences/
│       │   │   │   ├── dod-2.1-api-rag-ia-jeux.md
│       │   │   │   ├── dod-2.2-api-jeux-externe.md
│       │   │   │   └── dod-2.3-archero-vampire-survivors.md
│       │   │   ├── 3-intelligence-centrale-module-rag/
│       │   │   │   ├── dod-3.1-serveur-fastapi.md
│       │   │   │   ├── dod-3.2-base-vectorielle.md
│       │   │   │   ├── dod-3.3-ingestion-rag.md
│       │   │   │   ├── dod-3.4-orchestrateur-agents.md
│       │   │   │   └── dod-3.5-generateurs-llm.md
│       │   │   ├── 4-algorithmes-personnalisation/
│       │   │   │   ├── dod-4.1-selection-questions.md
│       │   │   │   └── dod-4.2-algorithme-retention.md
│       │   │   └── 5-securite-gouvernance-donnees/
│       │   │       └── Coffre-fort-&-Protection-rgpd.md
│       │   └── wbs/
│       │       ├── 1-conteneur-multiplateforme/
│       │       │   └── wbs-1.1-encapsulateurs.md
│       │       ├── 2-jeux-et-experiences/
│       │       │   ├── wbs-2.1-api-rag-ia-jeux.md
│       │       │   ├── wbs-2.2-api-jeux-externe.md
│       │       │   └── wbs-2.3-archero-vampire-survivors.md
│       │       ├── 3-intelligence-centrale-module-rag/
│       │       │   ├── wbs-3.1-serveur-fastapi.md
│       │       │   ├── wbs-3.2-base-vectorielle.md
│       │       │   ├── wbs-3.3-ingestion-rag.md
│       │       │   ├── wbs-3.4-orchestrateur-agents.md
│       │       │   └── wbs-3.5-generateurs-llm.md
│       │       ├── 4-algorithmes-personnalisation/
│       │       │   ├── mvp-wbs-algorithme-programmation.md
│       │       │   ├── wbs-4.1-selection-questions.md
│       │       │   └── wbs-4.2-algorithme-retention.md
│       │       └── 5-securite-gouvernance-donnees/
│       │           ├── Coffre-fort & Protection-rgpd.md
│       │           └── schema-wbs-global.md
│       ├── 3-relecture/           // réunion pour faire relire au groupe
│       └── 4-terminer/            // document à ne plus toucher
└── README.md
```

### Légende des dossiers `2-en-cours`

| Élément | Contenu |
| --- | --- |
| `budget-previsionnel.md` | Budget prévisionnel du projet |
| `plan-de-communication.md` | Plan de communication (B2C, B2B, gouvernance) |
| `livret-accueil.md` | Livret d'intégration pour les nouveaux membres |
| `schema-obs.md` | Schéma OBS (structure organisationnelle) |
| `gestion-des-risques.md` | Gestion des risques (registre, matrice, mitigation) |
| `technos.md` | Stack technologique (Backend, Frontend, IA, IoT) |
| `dod/` | Definition of Done par feature (organisé par catégorie PBS, via sous-dossiers numérotés 1→5) |
| `wbs/` | Work Breakdown Structure par feature (organisé par catégorie PBS, contient aussi `schema-wbs-global.md`) |
