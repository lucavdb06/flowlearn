# FlowLearn — Matrice RACI

> Version charte : [`FlowLearn-Matrice-RACI.html`](FlowLearn-Matrice-RACI.html)

Complète l’[OBS](schema-obs.md) et l’[organisation générale](organisation-general.md).

**Légende :** **R** = Réalise · **A** = Approuve (responsable final) · **C** = Consulté · **I** = Informé · **—** = non concerné

| Activité | Porteur de projet | Pôle Dev | Pôle Cyber |
| --- | --- | --- | --- |
| Vision produit & cadrage | **A/R** | C | I |
| Priorisation backlog / WBS | **A** | R | C |
| Arbitrage scope & planning | **A** | C | I |
| Conception PBS / specs fonctionnelles | **A** | **R** | C |
| Développement features MVP | I | **R** | C |
| Revue de code technique | C | **R** (pair) | C |
| Revue sécurité (PR) | I | C | **A/R** |
| Merge sur `main` | **A** | R | **A** (check cyber) |
| Tests automatisés / CI | I | **R** | C |
| Documentation technique (GitHub) | **A** | **R** | C |
| Documentation projet (Notion → Git) | **A/R** | C | I |
| Gestion des risques (registre) | **A** | C | **R** |
| Budget & achats outils | **A** | C | I |
| Plan de communication | **A** | C | I |
| Charte graphique / identité | **A** | C | I |
| Livret d’accueil & onboarding | **A/R** | C | C |
| Gates Go/No-Go (planning) | **A** | C | C |
| Incident sécurité / données | **A** | C | **R** |

---

## Rôles (rappel)

| Rôle | Membres (réf. livret) |
| --- | --- |
| **Porteur de projet** | Luca Vanden-Brande |
| **Pôle Dev** (chef : Quentin Dumas) | Nathan Plessis, Quentin Dumas, Daniel Okpe, César Lextraît (partiel) |
| **Pôle Cyber** (chef : Maxime Ruault) | Maxime Ruault, César Lextraît |

En cas d’absence du porteur, un dev senior désigné en réunion hebdo assure le **A** temporaire (à tracer en comité de pilotage).

---

## Règle d’or

Une seule personne **A** par activité. Le pôle cyber a un **A** bloquant sur la sécurité avant fusion ; le porteur de projet a l’**A** final sur le produit et le périmètre.
