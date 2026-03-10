# DOD – 3.5 Générateurs LLM via Adaptateur

**PBS :** Fournir une couche d’appel aux modèles LLM (via LiteLLM) pour la génération de quiz QCM et, si prévu, d’histoires interactives.

---

## Comment valider chaque feature

### 3.5.1 Configuration LiteLLM

**Cas d’erreur à gérer :**
- Clé API manquante ou invalide : erreur au démarrage ou au premier appel, message explicite.
- Provider indisponible : message ou fallback documenté (ex. autre modèle).

**Feature validée si :** au moins un provider (ex. OpenAI ou Mistral) est configuré et un appel de test renvoie une réponse ; la config est documentée (env, modèle utilisé).

---

### 3.5.2 Générateur de quiz QCM

**Cas d’erreur à gérer :**
- Réponse LLM non conforme au schéma attendu : parsing échoue, retry ou erreur structurée sans crash.
- Contexte trop long (dépassement de fenêtre) : troncature ou découpage documenté, pas d’erreur silencieuse.

**Feature validée si :** pour un contexte RAG donné, le générateur produit des questions QCM valides (format JSON/Pydantic) ; un test unitaire ou manuel valide un cas nominal et un cas de réponse invalide.

---

### 3.5.3 Générateur d’histoires interactives (optionnel MVP)

**Cas d’erreur à gérer :**
- Choix ou contexte incohérent : sortie par défaut ou message, pas de crash.

**Feature validée si :** si implémenté, une entrée (contexte + choix) produit une sortie structurée exploitable par l’orchestrateur ou le front ; le format est documenté.

---

### 3.5.4 Robustesse et coût

**Cas d’erreur à gérer :**
- Timeout ou 5xx du provider : retry limité puis erreur explicite.
- Quota dépassé : message clair pour l’opérateur ou l’utilisateur.

**Feature validée si :** les erreurs courantes (timeout, quota, clé invalide) sont gérées et ne provoquent pas de crash ; un log ou métrique permet de suivre l’usage si requis.
