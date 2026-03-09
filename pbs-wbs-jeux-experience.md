# PBS ↔ WBS — Jeux et Expérience

Schéma de navigation entre le **PBS global** (Product Breakdown Structure) et les **WBS** (Work Breakdown Structure) de la section *Jeux et Expériences*.

---

## Schéma Mermaid

```mermaid
flowchart TB
    subgraph PBS["📋 PBS Global"]
        PBS_ROOT["PBS — DopaLearn MVP<br/><i>Structure produit globale</i>"]
    end

    subgraph WBS_JEUX["🎮 WBS — Jeux et Expériences"]
        WBS_21["2.1 API RAG/IA → jeux<br/><i>Infos cours → gameplay quiz</i>"]
        WBS_22["2.2 API jeux → externe<br/><i>Conséquences hors jeu (ex. ESP32)</i>"]
        WBS_23["2.3 Archero / Vampire Survivors<br/><i>Type de jeux</i>"]
    end

    PBS_ROOT --> WBS_21
    PBS_ROOT --> WBS_22
    PBS_ROOT --> WBS_23

    click PBS_ROOT "./1-document/projet/3-relecture/mvp-pbs.md" _self
    click WBS_21 "./1-document/projet/2-en-cours/wbs/jeux-et-experience/wbs-2.1-api-rag-ia-jeux.md" _self
    click WBS_22 "./1-document/projet/2-en-cours/wbs/jeux-et-experience/wbs-2.2-api-jeux-externe.md" _self
    click WBS_23 "./1-document/projet/2-en-cours/wbs/jeux-et-experience/wbs-2.3-archero-vampire-survivors.md" _self
```

> **Note :** Dans les environnements qui supportent `click` (ex. GitHub, certains viewers), les boîtes sont cliquables. Sinon, utilisez les liens relatifs ci‑dessous.

---

## Liens relatifs (depuis la racine du projet)

| Élément | Fichier | Lien relatif |
|--------|---------|--------------|
| **PBS global** | MVP PBS | [mvp-pbs.md](./1-document/projet/3-relecture/mvp-pbs.md) |
| **2.1** API RAG/IA → jeux | WBS 2.1 | [wbs-2.1-api-rag-ia-jeux.md](./1-document/projet/2-en-cours/wbs/jeux-et-experience/wbs-2.1-api-rag-ia-jeux.md) |
| **2.2** API jeux → externe | WBS 2.2 | [wbs-2.2-api-jeux-externe.md](./1-document/projet/2-en-cours/wbs/jeux-et-experience/wbs-2.2-api-jeux-externe.md) |
| **2.3** Archero / Vampire Survivors | WBS 2.3 | [wbs-2.3-archero-vampire-survivors.md](./1-document/projet/2-en-cours/wbs/jeux-et-experience/wbs-2.3-archero-vampire-survivors.md) |

---

## Correspondance PBS → WBS (section 2)

D’après [mvp-pbs.md](./1-document/projet/3-relecture/mvp-pbs.md) :

| PBS (réf) | Intitulé | WBS associé |
|-----------|----------|-------------|
| **2.1** | api RAG/IA → jeux | [wbs-2.1-api-rag-ia-jeux.md](./1-document/projet/2-en-cours/wbs/jeux-et-experience/wbs-2.1-api-rag-ia-jeux.md) |
| **2.2** | api jeux → externe | [wbs-2.2-api-jeux-externe.md](./1-document/projet/2-en-cours/wbs/jeux-et-experience/wbs-2.2-api-jeux-externe.md) |
| **2.3** | Jeux type Archero / Vampire Survivors | [wbs-2.3-archero-vampire-survivors.md](./1-document/projet/2-en-cours/wbs/jeux-et-experience/wbs-2.3-archero-vampire-survivors.md) |
