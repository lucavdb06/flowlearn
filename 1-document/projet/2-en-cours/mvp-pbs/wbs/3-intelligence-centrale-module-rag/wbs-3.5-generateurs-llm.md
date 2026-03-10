# WBS – 3.5 Générateurs LLM via Adaptateur

**PBS :** Fournir une couche d’appel aux modèles LLM (via LiteLLM) pour la génération de quiz QCM et, si prévu, d’histoires interactives, avec sorties structurées et configurables.

---

## Features (WBS)

### 3.5.1 Configuration LiteLLM
- Configurer LiteLLM pour les providers utilisés (OpenAI, Anthropic, Mistral, ou modèle local).
- Gérer les clés API et paramètres (modèle par défaut, température, max_tokens) via variables d’environnement ou config.
- Documenter les modèles supportés et les limites (taille de contexte, coût).

### 3.5.2 Générateur de quiz QCM
- Implémenter un générateur qui, à partir d’un prompt et d’un contexte (chunks RAG), appelle le LLM et récupère une ou plusieurs questions au format attendu (JSON/Pydantic).
- Définir le prompt et les contraintes (nombre de réponses, présence d’une seule bonne réponse, difficulté).
- Valider et parser la sortie (Pydantic) ; gérer les échecs de parsing (retry ou erreur explicite).

### 3.5.3 Générateur d’histoires interactives (optionnel MVP)
- Si dans le périmètre : implémenter un générateur qui produit des passages d’histoire à partir du contexte cours et des choix utilisateur.
- Sortie structurée (texte, options de suite) pour l’orchestrateur ou le front.

### 3.5.4 Robustesse et coût
- Gestion des timeouts, quotas et erreurs API (retry avec backoff, message clair).
- Optionnel : logging des appels (modèle, tokens) pour suivi de coût ou usage.
