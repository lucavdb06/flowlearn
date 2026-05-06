# WBS – 3.4 Orchestrateur d’Agents IA

**PBS :** Mettre en place le cerveau central qui pilote les flux IA (RAG → génération quiz, sélection de questions, etc.) avec validation des entrées/sorties via PydanticAI (et LangGraph pour les flux complexes).

---

## Features (WBS)

### 3.4.1 Schémas et validation (Pydantic)
- Définir les modèles Pydantic des entrées et sorties des agents (question, contexte RAG, quiz, réponse utilisateur, etc.).
- S’assurer que toutes les sorties LLM passent par une validation stricte pour éviter les hallucinations bloquantes ou formats invalides.

### 3.4.2 Agent(s) de génération de quiz
- Implémenter un agent qui consomme le contexte RAG (chunks) et appelle le générateur LLM (3.5) pour produire des questions QCM.
- Valider la sortie (nombre de questions, champs obligatoires, bonne réponse cohérente) et renvoyer un format stable pour le jeu.

### 3.4.3 Intégration avec le RAG et la sélection (4.1)
- Brancher l’orchestrateur sur le moteur de recherche RAG (3.3.3) pour récupérer le contexte pertinent.
- Utiliser l’algorithme de sélection (4.1) pour décider quelle question/thème proposer, puis déclencher la génération ou le retour de question existante.

### 3.4.4 Flux complexes (LangGraph, si besoin)
- Pour les parcours à plusieurs étapes (correction, re-génération, boucles de réflexion), utiliser LangGraph pour orchestrer les états et les transitions.
- Documenter les flux et les conditions de sortie pour faciliter la maintenance.
