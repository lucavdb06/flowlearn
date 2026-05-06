# WBS – 3.3 Ingestion & RAG « Le Bibliothécaire »

**PBS :** Implémenter le module d'ingestion de documents (LlamaIndex) et le moteur de recherche RAG pour alimenter l'orchestrateur d'agents (3.4) et le générateur de quiz (3.5).

---

## Features (WBS)

### 3.3.1 Pipeline d'ingestion (LlamaIndex)
- Implémenter l'**import** de documents de cours (PDF, texte brut, éventuellement Markdown) :
  - parsing, nettoyage (encodage, pages vides, en‑têtes/pieds de page),
  - extraction de texte exploitable.
- Définir et implémenter la stratégie de **découpage (chunking)** :
  - taille des chunks, overlap,
  - respect des frontières sémantiques (phrases / paragraphes) pour un RAG pertinent.
- Gérer les erreurs d'ingestion (fichier corrompu, type non supporté) avec des messages clairs.

### 3.3.2 Indexation et écriture dans la base vectorielle
- Générer les **embeddings** pour chaque chunk via le modèle choisi (configurable via LiteLLM ou autre service).
- Insérer les chunks, leurs embeddings et métadonnées associées dans PostgreSQL / Supabase.
- Gérer :
  - la ré‑ingestion d'un document mis à jour (remplacement / versioning),
  - la suppression propre d'un document (et de tous ses chunks/embeddings liés).

### 3.3.3 Moteur de recherche RAG (retrieval)
- Implémenter une API ou service interne de **recherche par similarité** :
  - à partir d'une question ou d'un thème (texte → embedding),
  - récupérer les N chunks les plus pertinents (filtrage par utilisateur / thème si nécessaire).
- Retourner un format stable (JSON ou modèles Pydantic) pour :
  - l'orchestrateur d'agents (3.4),
  - le générateur de quiz (3.5),
  - éventuellement d'autres consommateurs (chat, historique interactif).
- Documenter le contrat (endpoints, paramètres, exemples de réponses) pour les équipes qui consomment le RAG.
