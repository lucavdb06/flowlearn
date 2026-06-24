# Organisation Générale du Projet (Modèle Opérationnel)

## 1. Introduction et Objectif du Document

Ce document définit le cadre opérationnel, les méthodes de travail et les règles de gouvernance du projet. Il constitue le socle de référence pour assurer la cohésion de l'équipe, la clarté des responsabilités et la fluidité des processus de travail tout au long du cycle de vie du produit.

## 2. Approche Méthodologique (Modèle Hybride)

Le projet adopte une stratégie en deux temps pour concilier rigueur de livraison et flexibilité d'innovation.

**Justification de l'approche :**
Le choix d'un modèle hybride répond à deux besoins critiques :

1. **Sécuriser le lancement (Phase 1) :** L'approche prédictive garantit le respect de la deadline sur le MVP et la production d’un PBS et d’un WBS en limitant les changements de périmètre.
2. **Maximiser l’expérience utilisateurs (Phase 2) :** L'approche Agile permet ensuite de pivoter ou d'ajuster le produit en fonction des retours réels des utilisateurs, évitant de développer des fonctionnalités inutiles.

### 2.1. Phase 1 : Construction du MVP (Mode Prédictif)

- **Objectif :** Livraison d'un produit minimum viable fonctionnel à date fixe.
- **Pilotage :** Basé sur le **PBS (Product Breakdown Structure)** pour définir les composants du MVP et le **WBS (Work Breakdown Structure)** pour les tâches de réalisation.
- **Validation :** Respect strict des spécifications et de l'architecture définies en amont.

### 2.2. Phase 2 : Évolution et Run (Mode Agile)

- **Objectif :** Amélioration continue basée sur les retours utilisateurs.
- **Pilotage :** Utilisation d'un **Product Backlog** et de **User Stories**. Le Backlog centralise les évolutions du produit (faisant office de PBS/WBS dynamique).

### 2.3. Le Pivot (La Transition)

- Le passage du mode WBS au mode Agile s'effectue dès la validation de la **Mise en Production (MEP)** du MVP et  la **Phase Review**

## 3. Instances de Gouvernance (Les Rituels)

Tableau récapitulatif des réunions et comités.

| Instance | Fréquence | Participants | Objectif | Traçabilité / Historique |
| --- | --- | --- | --- | --- |
| **Réunion d'Équipe (Hebdo)** | Hebdomadaire | Toute l'équipe | **Phase 1 (Dev) :** Démo des fonctionnalités implémentées.  **Phase 2 (Cyber) :** Partage des failles trouvées et compte-rendu de Code Review.  **Global :** Brainstorming et résolution de blocages. | **Enregistrement Vidéo** |
| **Point Ad-hoc / Technique** | À la demande | Membres concernés, Porteur de projet | Lever un verrou technique complexe ou approfondir un point spécifique du projet. | **Enregistrement Vidéo** |
| **Comité de Pilotage** | Mensuel | Porteur de projet, Toute l'équipe | Contrôle de l'avancement (deadlines). Redistribution des tâches pour optimiser la charge de travail et éviter les retards. | **Prise de notes uniquement** |
| **Phase Review** | Fin de phase | Toute l'équipe | Faire le point sur l'organisation, partager les apprentissages et organiser la transition (ex: passage à l'Agile). | **Enregistrement Vidéo** |

## 4. Rôles et Responsabilités

*Note : Se référer au schéma OBS pour l'attribution nominative des rôles.*

- **Porteur de Projet:** Responsable de la vision stratégique, de la définition des besoins (Backlog), ainsi que du pilotage opérationnel (PBS, WBS, planning).
- **Pôle Cybersécurité (2 personnes) :** Garant de la robustesse du système. Responsable de l'analyse des risques et du "Security by Design". Assure une revue de code régulière pour identifier et renforcer les failles.
- **Équipe de Développement (Multidisciplinaire) :** Responsable de la conception et de la réalisation technique (IA, Web, Infrastructure). Elle assure la qualité du code et la performance des modèles, respect des bonne pratique de code

## 5. Fiches de Poste et Justification des Affectations

*Note : Les affectations sont justifiées à partir de la **Carte des compétences** de l'équipe (niveaux auto-déclarés et validés collectivement : Notions / Opérationnel / Avancé / Expert) et alignées avec l'OBS et la matrice RACI. La logique retenue est d'affecter chaque rôle clé au membre présentant le niveau le plus élevé sur les compétences critiques associées, tout en assurant une redondance entre membres.*

### 5.1. Luca Vanden-Brande — Porteur de Projet / Développeur IA

- **Missions principales :** Porter la vision produit et technique, définir le cadrage (PBS, WBS, Backlog), piloter le planning et arbitrer les choix structurants. Contribue au développement des composants IA et à l'architecture du système.
- **Responsabilités / périmètre :** Décision stratégique et technique finale, validation des livrables, conception de l'architecture logicielle, responsabilité finale en cas de bug critique.
- **Compétences clés requises :** Gestion de projet, architecture logicielle, IA / LLM / RAG, base de données.
- **Livrables attendus :** Documents de cadrage, PBS / WBS / Backlog, architecture cible, contribution au code IA, MVP validé.
- **Justification de l'affectation :** Seul membre **Opérationnel** en gestion de projet (niveau le plus élevé de l'équipe) et **Avancé** en architecture logicielle (niveau le plus élevé), il est le mieux positionné pour le pilotage et les arbitrages d'architecture. Son niveau **Avancé** en IA/LLM/RAG et base de données lui permet de rester contributeur technique crédible et de garder la cohérence entre vision et réalisation.

### 5.2. Nathan Plessis — Développeur IA / Big Data

- **Missions principales :** Concevoir et implémenter les composants IA et data (modèles, pipelines, intégrations LLM/RAG). Assure le rôle de remplaçant du porteur de projet en cas d'absence.
- **Responsabilités / périmètre :** Implémentation technique IA locale, qualité et tests du code IA, documentation technique, soutien au pilotage.
- **Compétences clés requises :** Python / FastAPI, IA / LLM / RAG, base de données, architecture logicielle.
- **Livrables attendus :** Code IA, endpoints FastAPI, scripts data, tests associés, documentation GitHub.
- **Justification de l'affectation :** Profil **Avancé** sur le cœur technique du produit (Python/FastAPI, IA/LLM/RAG, base de données), ce qui en fait un pilier du pôle Développement. Sa solidité transverse et sa proximité avec le périmètre du porteur justifient son rôle de **remplaçant prioritaire** du porteur de projet (cf. OBS).

### 5.3. Daniel Okpe — Développeur IA / Big Data

- **Missions principales :** Développer et optimiser les composants IA et data du produit en parallèle de Nathan et Luca, afin d'assurer la redondance des compétences critiques.
- **Responsabilités / périmètre :** Implémentation des modèles et pipelines, optimisation des performances, tests locaux, documentation IA.
- **Compétences clés requises :** Python / FastAPI, IA / LLM / RAG, base de données.
- **Livrables attendus :** Code IA, scripts, tests unitaires, documentation associée.
- **Justification de l'affectation :** Niveau **Avancé** sur l'ensemble du socle IA/data (Python/FastAPI, IA/LLM/RAG, base de données), identique à Nathan. Cette redondance est volontaire : elle garantit la continuité du développement IA même en cas d'indisponibilité d'un membre et permet de paralléliser les tâches critiques du WBS.

### 5.4. Maxime Ruault — Responsable Cybersécurité (Chef du Pôle Cyber)

- **Missions principales :** Garantir la sécurité du système dès la conception (Security by Design), piloter l'analyse des risques et la stratégie de sécurité. Arbitre des décisions côté Cybersécurité.
- **Responsabilités / périmètre :** Audit de code, validation cyber **bloquante** avant merge, analyse des risques, conformité RGPD, décision finale sur les sujets sécurité.
- **Compétences clés requises :** Cybersécurité (audit, pentest, RGPD, Security by Design).
- **Livrables attendus :** Avis et rapports d'audit sécurité, analyses de risques, validation cyber des Pull Requests.
- **Justification de l'affectation :** Unique profil **Expert** en cybersécurité de l'équipe (niveau le plus élevé). Cette expertise justifie pleinement son autorité de blocage sur les merges et son rôle de **chef de pôle Cyber** qui tranche en cas de désaccord sur les sujets de sécurité.

### 5.5. César Lextraît — Développeur / Auditeur Cybersécurité & DevOps

- **Missions principales :** Faire le pont entre le développement et la sécurité : revue de code orientée sécurité, tests de vulnérabilité et mise en place / maintien de la chaîne CI-CD.
- **Responsabilités / périmètre :** Revue de code sécurité, tests de vulnérabilité, recommandations correctives, automatisation du déploiement et du monitoring (DevOps).
- **Compétences clés requises :** Cybersécurité, DevOps / CI-CD, Python / FastAPI, base de données.
- **Livrables attendus :** Rapports d'analyse, correctifs proposés, validations cyber, pipelines GitHub Actions, configuration de déploiement.
- **Justification de l'affectation :** Niveau **Avancé** en cybersécurité (juste derrière Maxime), ce qui en fait le second membre du pôle Cyber et un renfort naturel pour les revues. Il est également le seul membre **Avancé** en DevOps / CI-CD (niveau le plus élevé), ce qui le désigne pour piloter la chaîne d'intégration et de déploiement — une position charnière entre les pôles Dev et Cyber.

### 5.6. Quentin Dumas — Développeur Jeux Vidéo & UI-UX (Chef du Pôle Dev)

- **Missions principales :** Concevoir l'expérience de jeu (mécaniques type Archero / Vampire Survivors sous Godot) et le design d'interface (UI-UX) du produit. Arbitre des décisions techniques côté Développement.
- **Responsabilités / périmètre :** Développement des mécaniques de jeu, conception et réalisation des interfaces, cohérence ergonomique du produit, décision finale sur les sujets techniques du pôle Dev.
- **Compétences clés requises :** Godot / jeux vidéo, React / Frontend & UI-UX.
- **Livrables attendus :** Prototypes et mécaniques de jeu (GDScript), maquettes et interfaces React, conteneur multiplateforme (WBS 1.1), gameplay Archero/VS (WBS 2.3).
- **Justification de l'affectation :** Seul profil **Expert** à la fois en Godot / jeux vidéo et en React / Frontend & UI-UX (niveaux les plus élevés de l'équipe). Il apporte des compétences que l'équipe initiale ne couvrait pas et qui sont directement liées à des blocs du WBS. Cette expertise, combinée à sa polyvalence côté développement, justifie son rôle de **chef de pôle Dev** qui tranche en cas de désaccord technique.

## 6. Environnement de Travail et Outils

Liste des outils validés pour le projet :

- **Gestion de tâches :** GitHub (via GitHub Projects) pour le suivi du WBS puis du Backlog.
- **Communication :** Discord.
- **Documentation :**
    - **Notion :** Espace collaboratif pour la rédaction, le brouillon et la retouche des documents en équipe.
    - **GitHub (Wiki/Dépôt) :** Référentiel officiel pour les versions finales et validées ("Single Source of Truth").
- **Dépôt de code :** GitHub.

## 7. Gestion de la Qualité (DOD)

Chaque livrable doit répondre à la **Definition of Done (DOD)** 

[DOD (Definition of Done) ](https://app.notion.com/p/DOD-Definition-of-Done-341cc9a55ae18124bf88e6f44b56766c?pvs=21)

## 8. Gestion du Changement

- Pendant le MVP : Toute demande de nouvelle fonctionnalité est stockée dans un "Bac à sable" pour être traitée lors de la phase Agile (Phase 2).
- Après le MVP : Les changements sont priorisés lors de la planification de chaque Sprint.