## 🛠️ Infrastructure & Backend

- **FastAPI (Python) :** Serveur principal. Il expose les API, gère la logique métier et assure une communication rapide et asynchrone avec l'écosystème IA.
- **PostgreSQL / Supabase :** Base de données centrale. Stocke les utilisateurs, les logs et les vecteurs (via `pgvector`) nécessaires au RAG.

## 💻 Interfaces (Front-end)

- **React :** Base de code unique pour le développement de l'interface utilisateur web.
- **Electron :** Encapsule l'application React pour en faire un logiciel de bureau natif (Mac & Windows).
- **Capacitor :** Adapte l'application React pour un déploiement natif sur iOS et Android.

## 🧠 Intelligence Artificielle

- **LiteLLM (L'Adaptateur) :** Interface unique pour appeler n'importe quel modèle (OpenAI, Anthropic, Mistral). Il simplifie la gestion des clés et uniformise les formats de réponse.
- **PydanticAI (Le Cerveau Logique) :** Framework de contrôle. Il définit la logique des agents, valide les données entrantes/sortantes via le typage Python et garantit des résultats fiables et structurés.
- **LlamaIndex (Le Bibliothécaire) :** Expert de la donnée. Il indexe, découpe et recherche les informations dans tes documents (PDF, fichiers) pour alimenter le RAG.
- **LangGraph (L'Orchestrateur) :** Utilisé spécifiquement pour les agents complexes nécessitant des boucles de réflexion, des corrections d'erreurs et des processus longs.
- **CopilotKit :** Intégration front-end. Permet d'ajouter rapidement des composants d'IA conversationnelle (chat, aide à la saisie) directement dans l'interface React.

## 🕹️ Spécialisations (Jeux & IoT)

- **Godot Engine :** Moteur de jeu.
- _GDScript :_ Pour le prototypage rapide des mécaniques.
- _C# :_ Pour optimiser les performances sur les systèmes lourds.

- **ESP32 (IoT) :** Microcontrôleur pour le hardware.
- _Rust :_ Langage utilisé pour coder le firmware de manière sécurisée et ultra-performante.

---

**Veux-tu que je regroupe certains de ces éléments dans un tableau comparatif pour mieux visualiser les interactions ?**
