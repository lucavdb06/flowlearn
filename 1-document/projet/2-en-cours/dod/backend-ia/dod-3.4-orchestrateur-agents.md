# DOD – 3.4 Orchestrateur d’Agents IA

**PBS :** Mettre en place le cerveau central qui pilote les flux IA avec validation des entrées/sorties via PydanticAI (et LangGraph pour les flux complexes).

---

## Comment valider chaque feature

### 3.4.1 Schémas et validation (Pydantic)

**Cas d’erreur à gérer :**
- Sortie LLM invalide ou partielle : rejet par Pydantic, pas de propagation de données mal formées ; retry ou message explicite.
- Champs manquants ou types incorrects : validation à l’entrée et à la sortie, erreur structurée.

**Feature validée si :** toutes les données échangées avec les LLM sont typées (Pydantic) et documentées ; un test unitaire vérifie qu’une sortie invalide est rejetée.

---

### 3.4.2 Agent(s) de génération de quiz

**Cas d’erreur à gérer :**
- Contexte RAG vide ou insuffisant : comportement défini (message, question par défaut, ou erreur claire).
- Échec du LLM (timeout, quota) : retry ou erreur explicite sans état incohérent.

**Feature validée si :** à partir d’un contexte RAG valide, l’agent produit des questions QCM au format attendu ; les réponses sont validées par Pydantic et exploitables par le jeu (2.1).

---

### 3.4.3 Intégration avec le RAG et la sélection (4.1)

**Cas d’erreur à gérer :**
- RAG ou 4.1 indisponible : dégradation gracieuse (message, fallback) sans crash.
- Données incohérentes entre modules : validation aux frontières, logs pour le debug.

**Feature validée si :** une requête « prochaine question » ou « générer quiz » traverse bien RAG + sélection + génération ; le flux de bout en bout est testé (test d’intégration ou scénario manuel).

---

### 3.4.4 Flux complexes (LangGraph, si besoin)

**Cas d’erreur à gérer :**
- Boucle infinie ou état bloqué : garde-fous (nombre max d’étapes, timeout).
- Transition inattendue : états et conditions documentés, logs des décisions.

**Feature validée si :** les flux complexes (si implémentés) sont décrits (schéma ou doc) et un scénario de test valide un parcours complet sans blocage.
