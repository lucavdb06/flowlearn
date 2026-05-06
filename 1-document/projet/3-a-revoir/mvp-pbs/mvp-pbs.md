# Product Breakdown Structure (PBS) — DopaLearn MVP

---

## 1. Arborescence hiérarchique du produit

**Produit :** DopaLearn MVP (v0.1)

### 1. Conteneur Multiplateforme (Frontend Web & Mobile)

- **1.1 Encapsulateurs de Déploiement**  
  _Electron (Desktop), Capacitor (Mobile)_

---

### 2. Jeux et Expériences

#### A. SDK Jeux (Moteur Godot)

- **2.1 api Rag/ia -> jeux**
  - Récupérer des informations venant du cours pour alimenter la mécanique de gameplay du quiz (MVP).

- **2.2 api jeux -> externe**
  - permettre si une bonne ou mauvaise d'avoir des conséquence même en dehors du jeux (exemple avec une esp32)

#### B. mecanique de gameplay

- **1.0 mécanique : quizz simple (Minimum viable)**
  - mécanique intégrable dans les jeux
  - quiz comme mécanique principale (les questions servent de mécaniques de gameplay et de récompenses).

  | N°  | Fonctionalités                             | Validation                                                                             |
  | --- | ------------------------------------------ | -------------------------------------------------------------------------------------- |
  | 1   | Lancement du jeu                           | Nouvelle session avec le score réinitialisé à 0.                                       |
  | 2   | Chargement d'une questions et des réponses | Charge une question et des réponses valide.                                            |
  | 3   | Affichage de la question et des réponses   | La question et les réponses s'affiche correctement.                                    |
  | 4   | Sélection de la réponse                    | Le joueur ne peut selectionner qu'une seule réponse.                                   |
  | 5   | Validation de la réponse                   | Vérifie si la réponse est correcte. Incrémente le score si elle est bonne.             |
  | 6   | Passage à la prochaine question            | Efface la question et les réponses. Charge une nouvelle question → Fonctionalité N°`2` |
  | 7   | Fin de jeu                                 | Affiche le score total.                                                                |

#### C. jeux :

- **3.3 type de jeux :"Archero" ou "vampire survivor"**
  - jeux de survie casual

  | N° | Fonctionalités | Validation
  | - | - | -
  | 1 | Lancement du jeu | Nouvelle session avec le score réinitialisé à 0. |
  | 2 | Chargement d'une questions et des réponses | Charge une question et des réponses valide.
  | 3 | Affichage de la question et des réponses | La question et les réponses s'affiche correctement.
  | 4 | Sélection de la réponse | Le joueur ne peut selectionner qu'une seule réponse.
  | 5 | Validation de la réponse | Vérifie si la réponse est correcte. Incrémente le score si elle est bonne.
  | 6 | Passage à la prochaine question | Efface la question et les réponses. Charge une nouvelle question → Fonctionalité N°`2`
  | 7 | Fin de jeu | Affiche le score total.


---

### 3. Intelligence Centrale & Module RAG (Backend & IA)

- **3.1 Serveur Principal et API Asynchrone**  
  _FastAPI_
- **3.2 Base de Connaissances Vectorielle**  
  _PostgreSQL / Supabase avec pgvector_
- **3.3 Ingestion & RAG "Le Bibliothécaire"**  
  _LlamaIndex : Import PDF/Textes et découpage_
- **3.4 Orchestrateur d'Agents IA**  
  _PydanticAI pour validation logique/reflexion simple (LangGraph pour boucles complexes)_
- **3.5 Générateurs LLM via Adaptateur**  
  _LiteLLM : Générateur de quiz QCM_

---

### 4. Algorithmes de Personnalisation

**4.1 Algorithme de Sélection des Questions**  
 Méthode de répétition espacée type Anki (globale) ou sélection manuelle d'un thème choisi par l'utilisateur.

- **4.2 algorithme de rétention**  
   Système de scoring basé sur les KPIs récoltés. Le but de l'algorithme est de cibler le profil utilisateur pour maximiser son taux de rétention sur l'application.
  wbs :

---

### 5. Sécurité, Gouvernance & Données

- **5.1 Coffre-fort & Protection RGPD**  
  Protection des données personnelles (RGPD), sécurisation des données d'apprentissage.

---

## 2. Rôles et Dictionnaire du PBS

### 2.1 Rôles et Responsabilités

La conception et la réalisation du MVP s'articulent autour de **3 rôles clés** :

- **Porteur de Projet :** Responsable de la vision stratégique, de la définition des besoins (Backlog), du pilotage opérationnel (PBS, WBS, planning).
- **Pôle Cybersécurité (2 personnes) :** Garant de la robustesse du système. Responsable de l'analyse des risques et du _Security by Design_. Assure une revue de code régulière pour identifier et renforcer les failles.
- **Équipe de Développement (Multidisciplinaire) :** Responsable de la conception et de la réalisation technique (IA, Web, Infrastructure). Assume la qualité du code, la performance des modèles et le respect des bonnes pratiques de code.

### 2.2 Dictionnaire du PBS (Détails des Livrables)

| Réf | Nom du livrable           | Description / Périmètre                                                                                     | Critères d'acceptation (DOD)                                                      | Responsable                                 |
| --- | ------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------- |
| 1.1 | multiplatoforme           | Outils adaptant l'application React web en logiciel bureau (Electron) et mobile (Capacitor).                | Déploiement fonctionnel sur Mac, Windows, iOS et Android à partir du même code.   | Équipe de Développement                     |
| 2.1 | Algorithme de Rétention   | Logique de "Hook" éthique alternant questions simples/défis. Collecte des KPIs en jeu.                      | Les KPIs d'engagement sont trackés et formatés de manière unifiée pour le backend | Porteur de Projet (règles) & Éq. Dév (code) |
| 2.2 | Pont de Communication IoT | Connecteur Godot <> Hardware. Prépare le terrain pour de futurs périphériques physiques.                    | Format de sortie unifié et communication établie (ESP32, etc.)                    | Équipe de Développement                     |
| 2.3 | Standardisation JSON      | Contrat de données strict entre Backend IA (3.x) et Moteur Godot (2.x).                                     | Tous les flux QCM/Bonus respectent un schéma JSON unique sans exception.          | Équipe de Développement                     |
| 2.4 | Protocole IoT (ESP32)     | Protocole standardisé permettant d'ancrer des mécaniques de récompense physiques (bonbons, lumières, etc.). | Les récompenses virtuelles déclenchent des actions physiques fiables via l’ESP32  | Équipe de Développement                     |
| 2.5 | Expérience de Jeu 1       | Mini-jeu où le système RAG est la mécanique centrale ; répondre juste déclenche des actions en jeu.         | Boucle de gameplay stable, intégration fluide du format JSON standardisé          | Équipe de Développement                     |
| 3.3 | Module Ingestion RAG      | Analyse des documents importés (LlamaIndex), indexation vectorielle.                                        | Indexation réussie dans Supabase/PostgreSQL, recherche pertinent                  | Équipe de Développement                     |
| 3.4 | Orchestrateur Agents      | Cerveau central, gère les flux complexes et garantit des sorties fiables via PydanticAI.                    | Données LLM strictement typées ; pas d’hallucination bloquante                    | Équipe de Développement                     |
| 4.1 | Algorithme de Sélection   | Décide quelle question poser (Anki, Manuel, ou via algorithme de rétention).                                | L'utilisateur reçoit des questions pertinentes selon sa courbe de l'oubli         | Équipe de Développement                     |
| 4.2 | Moteur de Ciblage (Hook)  | Analyse les KPIs pour adapter l'expérience/utilisateur et maximiser l’utilité du temps passé.               | Le scoring influence directement la difficulté du jeu (cf. 2.1).                  | Équipe de Développement                     |
| 5.1 | Sécurité & RGPD           | Coffre-fort de données, architecture sécurisée.                                                             | Conformité légale, suppression de compte OK, failles auditées et corrigées        | Pôle Cybersécurité                          |

---

## 3. Spécificités Techniques & Qualité

- **Contrat de Données (JSON First) :**  
  La robustesse du produit repose sur le livrable 2.3 (Standardisation JSON). Tous les échanges entre les LLM (via LiteLLM/PydanticAI) et les expériences de jeu (Godot) doivent respecter des schémas Pydantic stricts, garantissant un format JSON immuable en entrée du moteur de jeu.

- **Infrastructure & Base de Données :**  
  _FastAPI_ (Python) pour des performances asynchrones élevées. Données textuelles et embeddings (RAG) sécurisés (RGPD) sur _PostgreSQL / Supabase_ avec _pgvector_.

- **Frontend & Interfaces :**  
  Le cœur applicatif centralisé sous _React_. Portabilité assurée par _Electron_ (Desktop) et _Capacitor_ (Mobile).

- **Intelligence Artificielle Modulaire :**
  - _LiteLLM :_ Interface agnostique pour interroger des modèles.
  - _PydanticAI :_ Validation logique et réflexions.
  - _LangGraph :_ Pour les cas complexes nécessitant des boucles de réflexion avancées.
  - _LlamaIndex :_ Moteur RAG ("Le Bibliothécaire").

- **Moteur de Jeu & IoT :**  
  Expériences ludiques sur _Godot Engine_ (GDScript pour la logique, C# en cas d'optimisation). Le pont de communication permet d'interfacer des objets connectés (_ESP32_) pour ancrer le système de récompense dans la réalité ou connecter l’IoT.

---
