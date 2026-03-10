# WBS – 3.1 Serveur Principal et API Asynchrone

**PBS :** Mettre en place le serveur backend FastAPI qui expose les API (RAG, quiz, agents) et assure la communication avec la base de données et les services IA.

---

## Features (WBS)

### 3.1.1 Structure du projet et configuration
- Définir l’architecture des modules (routes, services, modèles Pydantic).
- Configurer FastAPI (CORS, variables d’environnement, logs).
- Brancher la connexion à la base PostgreSQL / Supabase (session, pool).

### 3.1.2 Endpoints d’ingestion et RAG
- Exposer un endpoint d’ingestion (ex. POST /ingest) pour l’upload ou l’envoi de documents (délégation au module 3.3).
- Exposer un endpoint de requête RAG (ex. GET ou POST /query) qui renvoie des chunks pertinents (utilisation du moteur 3.3.3).

### 3.1.3 Endpoints quiz et prochaine question
- Exposer un endpoint pour la génération de quiz (ex. POST /quiz) et un pour la prochaine question (ex. GET /next-question), en s’appuyant sur 3.4 / 3.5 et 4.1.
- Retourner des réponses au format JSON standardisé (cf. contrat 2.3).

### 3.1.4 Robustesse et opération
- Gestion des erreurs (4xx/5xx), validation des entrées (Pydantic), logs structurés.
- Documentation des API (OpenAPI/Swagger) à jour et accessible.
