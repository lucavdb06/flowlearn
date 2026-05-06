# FlowLearn

Projet **FlowLearn** : apprentissage par de courtes sessions ludiques, architecture modulaire (plugins / expériences) et socle IA (RAG, MCP).  
Ce dépôt concentre les **documents de projet**, la **charte graphique** (HTML) et quelques **démos** (`media/`).

**Dépôt équipe :** [github.com/lucavdb06/flowlearn](https://github.com/lucavdb06/flowlearn)

## Documentation projet

| Ressource | Rôle |
| --- | --- |
| [`1-document/architecture.md`](1-document/architecture.md) | Arborescence des livrables et légende des dossiers |
| [`1-document/projet/3-a-revoir/README.md`](1-document/projet/3-a-revoir/README.md) | Flux : **relecture** → **charte graphique** → **`4-termine/`** |
| [`1-document/projet/3-a-revoir/pbs-wbs-dod-a-revoir.md`](1-document/projet/3-a-revoir/pbs-wbs-dod-a-revoir.md) | Liste des fichiers PBS / WBS / DoD (sous `3-a-revoir/mvp-pbs/`) |

Résumé du flux documentaire :

1. **`2-en-cours/`** — travail courant : budget, planning, risques, charte, stack, cadrage, communication, organisation (OBS), livret, etc.
2. **`3-a-revoir/`** — fond **PBS / WBS / DoD** (`mvp-pbs/`) + processus de relecture décrit dans le README du dossier.
3. **`2-en-cours/charte-graphique/`** — mise en forme selon la charte (pages HTML).
4. **`4-termine/`** — copies **validées** après charte et accord équipe.

## Liens

[Notion — Esp FlowLearn](https://www.notion.so/Esp-FlowLearn-2e66aaec6a1c806eb6a6dc1e4966cc93?source=copy_link)

---

## Pitch produit (synthèse)

### 1. Constat : la friction de l’apprentissage

Nous avons tous ces moments dans la journée : quelques minutes d’attente, ou la fatigue le soir. Le réflexe, c’est souvent le téléphone et le scroll passif. Le problème n’est pas le sujet à apprendre, mais la **charge cognitive** et la **manière** dont le contenu est présenté.

**FlowLearn** part de ce constat.

### 2. Solution : détourner l’attention vers la révision

FlowLearn vise à remplacer une partie de ce scroll par de la **micro-révision active**, avec moins de friction qu’un cours classique.

Au centre : une **base de connaissances personnelle** et un **serveur MCP** (Model Context Protocol) qui orchestre l’injection des cours dans des **expériences ludiques** via une API.

### 3. Applications (« plugins »)

Grâce à une **brique commune** modulaire, le système ne se limite pas aux QCM. Exemples :

- **Scroll éducatif** : questions courtes, interface rapide ; en cas d’erreur, reformulation pour limiter l’overfitting.
- **Jeux à enjeux** : intégration de la révision dans des mécaniques de jeu (stress / récompense pour l’ancrage mémoriel).
- **Formats plus passifs** : génération de rythmes à partir des cours, histoires interactives branchées sur la base de savoir.

### 4. Technologie : local et modulaire

Un **LLM local** permet usage **hors-ligne**, faible latence et meilleure maîtrise des données. La communauté peut brancher de **nouveaux plugins** sur la brique commune (mobile, desktop, vocal, etc.).

### 5. Conclusion

FlowLearn ne demande pas d’« arrêter de jouer » : il cherche à faire en sorte qu’**une partie du temps d’attention** serve à **progresser**.
