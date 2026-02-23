# Work Breakdown Structure (WBS) — DopaLearn MVP

---

## Introduction

Ce document décompose le projet en *lots de travaux* (Work Packages) et en tâches actionnables. Il est directement calqué sur le PBS (Product Breakdown Structure) v0.1 et tient compte de la stack technologique (React, FastAPI, Godot, LlamaIndex, PydanticAI, ESP32).

---

## 1. Phase d'Initialisation & Architecture (Fondations)

**Objectif :** Mettre en place l'environnement de travail et définir les règles de communication entre les briques.

| Tâche  | Description                                                                                          | Responsable                        |
|--------|------------------------------------------------------------------------------------------------------|------------------------------------|
| T1.1   | **Initialiser les dépôts et l'environnement CI/CD**<br>Configurer les repos Git (Backend, Frontend, Godot, IoT) et les pipelines de déploiement.                             | Équipe de Développement            |
| T1.2   | **Déployer l'infrastructure de base de données**<br>Configurer PostgreSQL / Supabase et activer l'extension pgvector pour le stockage vectoriel.                            | Équipe de Développement            |
| T1.3   | **Définir le Contrat de Données (Standardisation JSON)**<br>Rédiger et valider les schémas stricts (via Pydantic) qui serviront de norme de communication absolue entre l'IA, le Backend et Godot. *(Lien PBS 2.3)* | Porteur de Projet & Équipe de Développement |
| T1.4   | **Définir les règles de sécurité (Security by Design)**<br>Établir les protocoles de chiffrement, d'authentification et de gestion des tokens.                             | Pôle Cybersécurité                 |

---

## 2. Phase Backend & Intelligence Artificielle (Cerveau)

**Objectif :** Développer le moteur logique, le RAG et les API de service.

| Tâche  | Description                                                                                          | Responsable                        |
|--------|------------------------------------------------------------------------------------------------------|------------------------------------|
| T2.1   | **Développer l'API Asynchrone (FastAPI)**<br>Créer les routes (endpoints) principales pour l'authentification, l'ingestion de données et la communication avec le jeu. *(Lien PBS 3.1)* | Équipe de Développement            |
| T2.2   | **Implémenter le module RAG "Bibliothécaire"**<br>Intégrer LlamaIndex pour parser les documents (PDF/Texte), générer les embeddings et les stocker dans Supabase/pgvector. *(Lien PBS 3.3)* | Équipe de Développement            |
| T2.3   | **Développer les agents de génération (LLM)**<br>Configurer LiteLLM et développer les prompts système pour générer des QCM. *(Lien PBS 3.5)* | Équipe de Développement            |
| T2.4   | **Coder l'Orchestrateur PydanticAI**<br>Créer le flux de validation garantissant que la sortie de LiteLLM correspond exactement au standard JSON défini en T1.3. *(Lien PBS 3.4)* | Équipe de Développement            |
| T2.5   | **Développer l'Algorithme de Sélection**<br>Coder la logique de répétition espacée (type Anki) pour interroger la base vectorielle. *(Lien PBS 4.1)* | Équipe de Développement            |

---

## 3. Phase Frontend Web & Encapsulation Multiplateforme

**Objectif :** Créer l'interface permettant à l'utilisateur de gérer son profil et ses cours.

| Tâche  | Description                                                                                          | Responsable                        |
|--------|------------------------------------------------------------------------------------------------------|------------------------------------|
| T3.1   | **Développer l'Interface Principale (React)**<br>Maquetter et coder les écrans de connexion, le tableau de bord de progression, et l'interface d'import de documents.       | Équipe de Développement            |
| T3.2   | **Intégrer le Coffre-fort RGPD**<br>Implémenter la vue et la logique de gestion des données personnelles (export des données, bouton de suppression définitive du compte). *(Lien PBS 5.1)* | Équipe de Développement & Pôle Cybersécurité |
| T3.3   | **Configurer les Encapsulateurs Natifs**<br>Paramétrer Electron pour générer l'application Bureau (Mac/Win) et Capacitor pour l'application Mobile (iOS/Android). *(Lien PBS 1.1)* | Équipe de Développement            |

---

## 4. Phase Expériences Ludiques & Rétention (Moteur Godot)

**Objectif :** Développer le jeu qui va consommer les QCM générés par l'IA.

| Tâche  | Description                                                                                          | Responsable                        |
|--------|------------------------------------------------------------------------------------------------------|------------------------------------|
| T4.1   | **Intégrer le Pont de Communication HTTP/JSON**<br>Développer en GDScript/C# le client HTTP côté Godot pour récupérer les QCM du Backend FastAPI selon le standard JSON.     | Équipe de Développement            |
| T4.2   | **Développer l'Expérience de Jeu 1 (Mini-jeu)**<br>Concevoir la boucle de gameplay où les actions sont bloquées/débloquées par les questions du RAG. *(Lien PBS 2.5)*    | Équipe de Développement            |
| T4.3   | **Implémenter l'Algorithme de Rétention (Côté Client)**<br>Coder la logique de collecte des KPIs d'engagement (temps de réponse, taux de réussite) en jeu et les renvoyer au Backend. *(Lien PBS 2.1)* | Équipe de Développement            |
| T4.4   | **Concevoir le Moteur de Ciblage (Côté Serveur)**<br>Traiter les KPIs reçus de Godot pour ajuster la difficulté de manière dynamique. *(Lien PBS 4.2)*                    | Porteur de Projet (Définition) & Équipe de Développement (Code) |

---

## 5. Phase IoT et Mécaniques d'Ancrage Réel

**Objectif :** Lier les récompenses in-game à des actions dans le monde physique.

| Tâche  | Description                                                                                          | Responsable                        |
|--------|------------------------------------------------------------------------------------------------------|------------------------------------|
| T5.1   | **Développer le Système de Récompense (Host/Serveur)**<br>Créer la logique côté serveur (séparée de l'IoT) qui valide si une récompense physique doit être octroyée en fonction des succès du joueur. | Équipe de Développement            |
| T5.2   | **Développer le Firmware ESP32 (Rust/C++)**<br>Écrire le code embarqué de l'ESP32 pour écouter les requêtes sécurisées provenant du serveur "Host".                       | Équipe de Développement            |
| T5.3   | **Implémenter le Protocole de Communication IoT**<br>Mettre en place la communication bidirectionnelle sécurisée entre le Serveur Host, Godot, et l'ESP32 (ex: allumer une lampe ou activer un moteur de distribution). *(Lien PBS 2.4)* | Équipe de Développement & Pôle Cybersécurité |

---

## 6. Phase Tests, Sécurité & Déploiement

**Objectif :** Sécuriser, tester et livrer le produit final.

| Tâche  | Description                                                                                          | Responsable                        |
|--------|------------------------------------------------------------------------------------------------------|------------------------------------|
| T6.1   | **Réaliser la Revue de Code et les Tests d'Intrusion**<br>Auditer l'API, les failles d'injection LLM (prompt injection) et la sécurisation du flux IoT.                  | Pôle Cybersécurité                 |
| T6.2   | **Exécuter les Tests d'Intégration Bout-en-Bout (E2E)**<br>Tester le flux complet : Upload PDF → Extraction IA → Traduction QCM JSON → Affichage dans Godot → Validation Récompense ESP32. | Équipe de Développement            |
| T6.3   | **Déployer la v0.1 (MVP)**<br>Publier le Backend sur l'environnement de production, distribuer les builds Electron/Capacitor et figer la version open-source du noyau.   | Équipe de Développement            |

---

## Schéma Mermaid — Récapitulatif du WBS

```mermaid
flowchart TB
    WBS["WBS DopaLearn MVP"]

    subgraph P1["1. Initialisation & Architecture"]
        T1_1["T1.1 Repos & CI/CD"]
        T1_2["T1.2 BDD PostgreSQL / pgvector"]
        T1_3["T1.3 Contrat de Données JSON"]
        T1_4["T1.4 Security by Design"]
    end

    subgraph P2["2. Backend & IA"]
        T2_1["T2.1 API FastAPI"]
        T2_2["T2.2 RAG Bibliothécaire"]
        T2_3["T2.3 Agents LLM / QCM"]
        T2_4["T2.4 Orchestrateur PydanticAI"]
        T2_5["T2.5 Algorithme de Sélection"]
    end

    subgraph P3["3. Frontend Web"]
        T3_1["T3.1 Interface React"]
        T3_2["T3.2 Coffre-fort RGPD"]
        T3_3["T3.3 Electron / Capacitor"]
    end

    subgraph P4["4. Moteur Godot"]
        T4_1["T4.1 Pont HTTP/JSON"]
        T4_2["T4.2 Mini-jeu & gameplay"]
        T4_3["T4.3 KPIs & rétention client"]
        T4_4["T4.4 Moteur de ciblage serveur"]
    end

    subgraph P5["5. IoT & Ancrage Réel"]
        T5_1["T5.1 Système de récompense Host"]
        T5_2["T5.2 Firmware ESP32"]
        T5_3["T5.3 Protocole IoT sécurisé"]
    end

    subgraph P6["6. Tests & Déploiement"]
        T6_1["T6.1 Revue de code & intrusion"]
        T6_2["T6.2 Tests E2E"]
        T6_3["T6.3 Déploiement MVP v0.1"]
    end

    WBS --> P1
    WBS --> P2
    WBS --> P3
    WBS --> P4
    WBS --> P5
    WBS --> P6

    P1 --> P2
    P2 --> P3
    P3 --> P4
    P4 --> P5
    P5 --> P6
```

---