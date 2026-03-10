# Schéma global PBS + DOD — DopaLearn MVP

Grand schéma : **PBS** en tête, puis une zone par section avec des **petits carrés jaunes** (livrables / DOD).

```mermaid
flowchart TB
  PBS["DopaLearn MVP — PBS globale"]

  PBS --- S1
  PBS --- S2
  PBS --- S3
  PBS --- S4
  PBS --- S5

  subgraph S1["1. Conteneur Multiplateforme"]
    direction LR
    s1_1[1.1 Encapsulateurs]
    s1_dod[dod-1.1]
  end

  subgraph S2["2. Jeux et Expériences"]
    direction LR
    s2_1[2.1 API RAG jeux]
    s2_d1[dod-2.1]
    s2_2[2.2 API externe]
    s2_d2[dod-2.2]
    s2_3[2.3 Archero Vampire]
    s2_d3[dod-2.3]
  end

  subgraph S3["3. Intelligence Centrale et Module RAG"]
    direction LR
    s3_1[3.1 FastAPI]
    s3_d1[dod-3.1]
    s3_2[3.2 Base vectorielle]
    s3_d2[dod-3.2]
    s3_3[3.3 Ingestion RAG]
    s3_d3[dod-3.3]
    s3_4[3.4 Orchestrateur]
    s3_d4[dod-3.4]
    s3_5[3.5 Générateurs LLM]
    s3_d5[dod-3.5]
  end

  subgraph S4["4. Algorithmes de Personnalisation"]
    direction LR
    s4_1[4.1 Sélection questions]
    s4_d1[dod-4.1]
    s4_2[4.2 Rétention]
    s4_d2[dod-4.2]
  end

  subgraph S5["5. Sécurité et Gouvernance"]
    direction LR
    s5_1[5.1 Coffre-fort RGPD]
    s5_d1[dod-5.1]
  end

  classDef yellow fill:#ffeb3b,stroke:#f57f17,color:#000
  class s1_dod,s2_d1,s2_d2,s2_d3,s3_d1,s3_d2,s3_d3,s3_d4,s3_d5,s4_d1,s4_d2,s5_d1 yellow
```

**Légende :** les carrés jaunes correspondent aux fichiers DOD de chaque livrable (voir dossiers `dod/` par section).
