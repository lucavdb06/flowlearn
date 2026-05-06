# DOD – 3.1 Serveur Principal et API Asynchrone

**PBS :** Mettre en place le serveur backend FastAPI qui expose les API (RAG, quiz, agents) et assure la communication avec la base de données et les services IA.

---

## Comment valider chaque feature

### 3.1.1 Structure du projet et configuration

**Cas d’erreur à gérer :**
- Base de données injoignable : message explicite, pas de crash au démarrage ; retry ou config documentée.
- Variables d’environnement manquantes : échec clair au démarrage avec indication des variables attendues.

**Feature validée si :** le serveur démarre, se connecte à la base, et un autre développeur peut le lancer en local à partir de la doc (env, commandes).

---

### 3.1.2 Endpoints d’ingestion et RAG

**Cas d’erreur à gérer :**
- Fichier invalide ou trop volumineux : rejet avec code 4xx et message clair.
- Erreur interne (RAG, DB) : réponse 5xx avec log, pas de fuite d’informations sensibles.

**Feature validée si :** les endpoints d’ingestion et de requête RAG sont appelables et renvoient des réponses conformes au contrat ; la doc API (OpenAPI) les décrit.

---

### 3.1.3 Endpoints quiz et prochaine question

**Cas d’erreur à gérer :**
- Paramètres manquants ou invalides : validation Pydantic, erreur 422 ou 400 explicite.
- Aucune question disponible : réponse structurée (liste vide ou message) plutôt qu’exception non gérée.

**Feature validée si :** les réponses sont au format JSON standardisé attendu par les jeux (2.3) ; les exemples de requêtes/réponses sont documentés ou testables (ex. Postman).

---

### 3.1.4 Robustesse et opération

**Cas d’erreur à gérer :**
- Timeout ou surcharge : comportement dégradé défini (retry, message), pas de crash en cascade.

**Feature validée si :** les erreurs courantes renvoient des codes HTTP et corps cohérents ; la documentation OpenAPI/Swagger est à jour et reflète les endpoints exposés.
