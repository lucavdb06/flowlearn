# Schéma WBS Global — DopaLearn MVP (v0.1)

---

## Vue d'ensemble (Mermaid)

```mermaid
mindmap
  root((DopaLearn MVP))
    1. Conteneur Multiplateforme
      1.1 Encapsulateurs
        1.1.1 Config Electron Desktop
        1.1.2 Config Capacitor Mobile
        1.1.3 Build & livraison
    2. Jeux & Expériences
      2.1 API RAG/IA → jeux
        2.1.1 Exposition API RAG
        2.1.2 Transformation cours → quiz
        2.1.3 Intégration Godot
      2.2 API jeux → externe
        2.2.1 Schéma JSON
        2.2.2 API côté jeu Godot
        2.2.3 Interpréteur Rust
        2.2.4 Intégration ESP32
      2.3 Jeu Archero / Vampire Survivors
        2.3.1 Déplacement personnage
        2.3.2 Spawn monstres
        2.3.3 3 types ennemis
        2.3.4 3 armes
        2.3.5 Carte / niveau
        2.3.6 Évolution difficulté
        2.3.7 Intégration quiz MVP
    3. Intelligence Centrale & RAG
      3.1 Serveur FastAPI
        3.1.1 Structure & config
        3.1.2 Endpoints ingestion/RAG
        3.1.3 Endpoints quiz
        3.1.4 Robustesse & doc API
      3.2 Base vectorielle pgvector
        3.2.1 Instance & extension
        3.2.2 Schéma stockage
      3.3 Ingestion RAG LlamaIndex
        3.3.1 Pipeline ingestion
        3.3.2 Indexation & embeddings
        3.3.3 Moteur recherche RAG
      3.4 Orchestrateur agents IA
        3.4.1 Schémas Pydantic
        3.4.2 Agent génération quiz
        3.4.3 Intégration RAG + 4.1
        3.4.4 Flux complexes LangGraph
      3.5 Générateurs LLM
        3.5.1 Config LiteLLM
        3.5.2 Générateur quiz QCM
        3.5.3 Histoires interactives
        3.5.4 Robustesse & coût
    4. Algorithmes Personnalisation
      4.1 Sélection des questions
        4.1.1 Modèle de données SRS
        4.1.2 Logique Anki
        4.1.3 Endpoint /next-question
      4.2 Algorithme de rétention
        4.2.1 Modèle KPIs
        4.2.2 Moteur scoring
        4.2.3 Adaptation Hook éthique
        4.2.4 API contrat jeu
    5. Sécurité & Données
      5.1 Coffre-fort & RGPD
        5.1.1 Politique données
        5.1.2 Accès & secrets
        5.1.3 Suppression & rétention
        5.1.4 Audit sécurité
```

---

## Vue tabulaire (PBS → WBS → fichiers)

| PBS | Feature | Sous-features (WBS) | Fichier WBS | Fichier DOD |
|-----|---------|---------------------|-------------|-------------|
| **1. Conteneur** | 1.1 Encapsulateurs | 1.1.1 Electron, 1.1.2 Capacitor, 1.1.3 Build | `wbs/conteneur-multiplateforme/wbs-1.1-encapsulateurs.md` | `dod/conteneur-multiplateforme/dod-1.1-encapsulateurs.md` |
| **2. Jeux** | 2.1 API RAG → jeux | 2.1.1 Expo API, 2.1.2 Transformation, 2.1.3 Godot | `wbs/jeux-et-experience/wbs-2.1-api-rag-ia-jeux.md` | `dod/jeux-et-experience/dod-2.1-api-rag-ia-jeux.md` |
| | 2.2 API jeux → externe | 2.2.1 JSON, 2.2.2 Godot, 2.2.3 Rust, 2.2.4 ESP32 | `wbs/jeux-et-experience/wbs-2.2-api-jeux-externe.md` | `dod/jeux-et-experience/dod-2.2-api-jeux-externe.md` |
| | 2.3 Archero / VS | 2.3.1→2.3.7 (7 features) | `wbs/jeux-et-experience/wbs-2.3-archero-vampire-survivors.md` | `dod/jeux-et-experience/dod-2.3-archero-vampire-survivors.md` |
| **3. Backend IA** | 3.1 Serveur FastAPI | 3.1.1→3.1.4 | `wbs/backend-ia/wbs-3.1-serveur-fastapi.md` | `dod/backend-ia/dod-3.1-serveur-fastapi.md` |
| | 3.2 Base vectorielle | 3.2.1 Instance, 3.2.2 Schéma | `wbs/backend-ia/wbs-3.2-base-vectorielle.md` | `dod/backend-ia/dod-3.2-base-vectorielle.md` |
| | 3.3 Ingestion RAG | 3.3.1 Pipeline, 3.3.2 Indexation, 3.3.3 Retrieval | `wbs/backend-ia/wbs-3.3-ingestion-rag.md` | `dod/backend-ia/dod-3.3-ingestion-rag.md` |
| | 3.4 Orchestrateur IA | 3.4.1→3.4.4 | `wbs/backend-ia/wbs-3.4-orchestrateur-agents.md` | `dod/backend-ia/dod-3.4-orchestrateur-agents.md` |
| | 3.5 Générateurs LLM | 3.5.1→3.5.4 | `wbs/backend-ia/wbs-3.5-generateurs-llm.md` | `dod/backend-ia/dod-3.5-generateurs-llm.md` |
| **4. Algos** | 4.1 Sélection questions | 4.1.1 Data SRS, 4.1.2 Anki, 4.1.3 Endpoint | `wbs/algorithmes-personnalisation/wbs-4.1-selection-questions.md` | `dod/algorithmes-personnalisation/dod-4.1-selection-questions.md` |
| | 4.2 Rétention (Hook) | 4.2.1 KPIs, 4.2.2 Scoring, 4.2.3 Hook, 4.2.4 API | `wbs/algorithmes-personnalisation/wbs-4.2-algorithme-retention.md` | `dod/algorithmes-personnalisation/dod-4.2-algorithme-retention.md` |
| **5. Sécu** | 5.1 RGPD & Coffre | 5.1.1→5.1.4 | `wbs/securite/wbs-5.1-securite-rgpd.md` | `dod/securite/dod-5.1-securite-rgpd.md` |

---

## Flux de validation (DOD global)

```mermaid
flowchart LR
  A[Dev sur branche] --> B[Tests locaux]
  B --> C[PR GitHub]
  C --> D[CI / Tests auto]
  D --> E[Revue cyber + tech]
  E --> F[DOD spécifique feature validée]
  F --> G[Merge main]
  G --> H[Done sur GitHub Projects]
```

---

## Dépendances entre blocs

```mermaid
flowchart TB
  subgraph "Données & IA"
    DB["3.2 Base vectorielle"]
    ING["3.3 Ingestion RAG"]
    ORC["3.4 Orchestrateur"]
    GEN["3.5 Générateurs LLM"]
    API["3.1 Serveur FastAPI"]
  end

  subgraph "Algorithmes"
    SEL["4.1 Sélection questions"]
    RET["4.2 Rétention / Hook"]
  end

  subgraph "Jeux & Front"
    J1["2.1 API RAG → jeux"]
    J2["2.2 API jeux → ESP32"]
    J3["2.3 Jeu Archero/VS"]
    FRONT["1.1 Electron / Capacitor"]
  end

  subgraph "Transverse"
    SEC["5.1 Sécurité & RGPD"]
  end

  DB --> ING
  ING --> ORC
  ORC --> GEN
  GEN --> API
  SEL --> API
  RET --> SEL
  API --> J1
  J1 --> J3
  J2 --> J3
  API --> FRONT
  SEC -.-> DB
  SEC -.-> API
```
