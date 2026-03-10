# Architecture des documents

## Définition

### Flux documentaire

`projet` : contient une arborescence de dossiers qui représente le flux de création d'un document. Les dossiers `2-en-cours` et `3-relecture` forment une boucle tant que la relecture n'est pas validée.

```txt
├── 1-document
│   ├── architecture.md
│   ├── projet/
│   │   ├── 1-a-faire/            // structure du document pas encore définie
│   │   ├── 2-en-cours/           // travail en cours (todo défini dans le document)
│   │   │   ├── budget/
│   │   │   │   └── budget-previsionnel.md
│   │   │   ├── communication/
│   │   │   │   └── plan-de-communication.md
│   │   │   ├── dod/
│   │   │   │   ├── algorithmes-personnalisation/
│   │   │   │   │   ├── dod-4.1-selection-questions.md
│   │   │   │   │   └── dod-4.2-algorithme-retention.md
│   │   │   │   ├── backend-ia/
│   │   │   │   │   ├── dod-3.1-serveur-fastapi.md
│   │   │   │   │   ├── dod-3.2-base-vectorielle.md
│   │   │   │   │   ├── dod-3.3-ingestion-rag.md
│   │   │   │   │   ├── dod-3.4-orchestrateur-agents.md
│   │   │   │   │   └── dod-3.5-generateurs-llm.md
│   │   │   │   ├── conteneur-multiplateforme/
│   │   │   │   │   └── dod-1.1-encapsulateurs.md
│   │   │   │   ├── jeux-et-experience/
│   │   │   │   │   ├── dod-2.1-api-rag-ia-jeux.md
│   │   │   │   │   ├── dod-2.2-api-jeux-externe.md
│   │   │   │   │   └── dod-2.3-archero-vampire-survivors.md
│   │   │   │   └── securite/
│   │   │   │       └── dod-5.1-securite-rgpd.md
│   │   │   ├── livret-accueil/
│   │   │   │   └── livret-accueil.md
│   │   │   ├── obs/
│   │   │   │   └── schema-obs.md
│   │   │   ├── organisation/
│   │   │   │   └── organisation-generale.md
│   │   │   ├── risques/
│   │   │   │   └── gestion-des-risques.md
│   │   │   ├── schemas/
│   │   │   │   └── schema-wbs-global.md
│   │   │   ├── technos/
│   │   │   │   └── technos.md
│   │   │   └── wbs/
│   │   │       ├── algorithmes-personnalisation/
│   │   │       │   ├── mvp-wbs-algorithme-programmation.md
│   │   │       │   ├── wbs-4.1-selection-questions.md
│   │   │       │   └── wbs-4.2-algorithme-retention.md
│   │   │       ├── backend-ia/
│   │   │       │   ├── wbs-3.1-serveur-fastapi.md
│   │   │       │   ├── wbs-3.2-base-vectorielle.md
│   │   │       │   ├── wbs-3.3-ingestion-rag.md
│   │   │       │   ├── wbs-3.4-orchestrateur-agents.md
│   │   │       │   └── wbs-3.5-generateurs-llm.md
│   │   │       ├── conteneur-multiplateforme/
│   │   │       │   └── wbs-1.1-encapsulateurs.md
│   │   │       ├── jeux-et-experience/
│   │   │       │   ├── wbs-2.1-api-rag-ia-jeux.md
│   │   │       │   ├── wbs-2.2-api-jeux-externe.md
│   │   │       │   └── wbs-2.3-archero-vampire-survivors.md
│   │   │       └── securite/
│   │   │           └── wbs-5.1-securite-rgpd.md
│   │   ├── 3-relecture/           // réunion pour faire relire au groupe
│   │   └── 4-terminer/            // document à ne plus toucher
│   └── techno.md
└── README.md
```

### Légende des dossiers `2-en-cours`

| Dossier | Contenu |
| --- | --- |
| `budget/` | Budget prévisionnel du projet |
| `communication/` | Plan de communication (B2C, B2B, gouvernance) |
| `dod/` | Definition of Done par feature (organisé par catégorie PBS) |
| `livret-accueil/` | Livret d'intégration pour les nouveaux membres |
| `obs/` | Schéma OBS (structure organisationnelle) |
| `organisation/` | Organisation générale (méthodologie, rituels, rôles) |
| `risques/` | Gestion des risques (registre, matrice, mitigation) |
| `schemas/` | Schémas visuels WBS global (Mermaid) |
| `technos/` | Stack technologique (Backend, Frontend, IA, IoT) |
| `wbs/` | Work Breakdown Structure par feature (organisé par catégorie PBS) |
