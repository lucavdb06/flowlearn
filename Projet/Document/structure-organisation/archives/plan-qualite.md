# FlowLearn — Plan qualité

> Source Markdown (archives). Les livrables de référence sont au format charte HTML dans leurs dossiers-sujets respectifs.

Processus de développement, tickets, tests, revues et livraisons.  
Complète la [DoD globale](../../mvp-pbs-dod/dod/dod-globale.html) et l’[organisation générale](../Organisation-Generale/organisation-general.html).

---

## 1. Objet

Définir les **règles communes** pour construire, vérifier et livrer FlowLearn : méthode, outils, configuration, tests et critères de passage en « Done ».

---

## 2. Méthode retenue

Modèle **hybride** (détaillé dans `organisation-general.md`) :

| Phase | Mode | Pilotage |
| --- | --- | --- |
| **MVP (construction)** | Prédictif | PBS + WBS, périmètre figé, gates planning |
| **Après MEP MVP** | Agile | Product Backlog, user stories, sprints |

| Élément | Choix FlowLearn |
| --- | --- |
| Priorisation MVP | Périmètre PBS/WBS + gates Go/No-Go ([planning](../../planning/flowlearn-gantt.html)) |
| Pilotage tâches | **GitHub Projects** (WBS → backlog) |
| Doc brouillon | **Notion** |
| Doc validée | **GitHub** (dépôt [flowlearn](https://github.com/lucavdb06/flowlearn)) |
| Communication | **Discord** |
| Décision finale | **Porteur de projet** (arbitrage scope, priorités, acceptation) |

---

## 3. Rôles qualité

| Rôle | Responsabilité qualité |
| --- | --- |
| **Porteur de projet** | Périmètre, priorités, acceptation fonctionnelle, cohérence livrables |
| **Pôle développement** | Code, tests, documentation technique, respect DoD par feature |
| **Pôle cybersécurité** | Revue sécurité sur PR, Security by Design, validation check cyber **bloquant** avant merge |
| **Équipe (pair)** | Code review technique (au moins 1 relecteur par PR) |

Répartition nominative : [OBS](../schema-obs/schema-obs.html) et [matrice RACI](../FlowLearn-Matrice-RACI/FlowLearn-Matrice-RACI.html).

---

## 4. Gestion des tickets

- Chaque tâche WBS / issue GitHub est liée à un **lot PBS** et à une **DoD** (globale + fichier `dod/` si applicable).
- Un ticket contient au minimum : contexte, résultat attendu, critères d’acceptation, responsable, priorité.
- **Aucun ticket en Done** sans DoD validée (voir processus §7).
- Blocage > 24–48 h : signalé en réunion hebdo ou point ad-hoc.

Colonnes GitHub Projects suggérées : `Backlog` → `À faire` → `En cours` → `Review` → `Done`.

---

## 5. Gestion de configuration

| Sujet | Règle |
| --- | --- |
| **Branches** | `main` protégée ; `feature/<module>-<sujet>` ; correctifs `fix/<sujet>` |
| **Commits** | [Conventional Commits](https://www.conventionalcommits.org/) : `feat`, `fix`, `docs`, `test`, `refactor`, `chore` |
| **Pull requests** | 1 relecture minimum, CI verte, description + preuve de test |
| **Secrets** | Jamais dans le dépôt ; variables d’environnement / GitHub Secrets |
| **Documentation** | README / docs mis à jour si API, installation ou comportement change |

---

## 6. Stratégie de tests

| Niveau | Cible | Moment |
| --- | --- | --- |
| **Unitaires** | Services, logique métier, composants critiques | Chaque PR |
| **Intégration** | API, modules RAG, flux jeu ↔ backend | PR concernée |
| **E2E** | Parcours MVP (auth, quiz, ingestion) | Avant gate / démo |
| **Sécurité** | Revue manuelle + bonnes pratiques (OWASP) | PR + gate cybersécurité |
| **Régression** | Pas de casse de l’existant | CI GitHub Actions |

Détail par feature : fichiers dans [`mvp-pbs-dod/dod/`](../../mvp-pbs-dod/dod/).

---

## 7. Processus de livraison (résumé)

Aligné sur la [DoD globale](../../mvp-pbs-dod/dod/dod-globale.html) :

1. Développement sur branche `feature/…`
2. Tests locaux + tests automatisés
3. **Pull Request** → déclenchement CI (GitHub Actions)
4. **Revue cybersécurité** (check bloquant)
5. **Code review** technique (pair)
6. **Validation porteur / tech lead** si besoin
7. Merge sur `main` → statut **Done** sur GitHub Projects

---

## 8. Qualité documentaire

| Étape | Lieu |
| --- | --- |
| Brouillon, retouches équipe | Notion |
| Source Markdown (historique) | Sous-dossier `archives/` du dossier-sujet concerné |
| Version de référence (charte) | Fichier `.html` à la racine du dossier-sujet (`Projet/Document/<sujet>/`) |
| Mise en forme charte | CSS partagée `charte-graphique/archives/flowlearn-document.css` |
| Dépôt officiel | GitHub (Single Source of Truth) |

---

## 9. Liens utiles

- [Description fonctionnelle](FlowLearn-Description-Fonctionnelle.html)
- [Planning & gates](../../planning/flowlearn-gantt.html)
- [Gestion des risques](../../risques/gestion-des-risques.html)
- [Livret d’accueil](../../livret-accueil/livret-accueil.html)
