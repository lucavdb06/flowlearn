# WBS – 2.1 API RAG/IA → jeux

**PBS :** Récupérer des informations venant du cours pour alimenter la mécanique de gameplay du quiz (MVP).

---

## Features (WBS)

### 2.1.1 Exposition ou consommation de l’API RAG/IA
- Définir l’endpoint (ou le flux) qui renvoie du contenu pédagogique issu du cours (RAG/IA).
- S’assurer que le jeu peut appeler cette API (HTTP, format de réponse stable).

### 2.1.2 Transformation contenu cours → données quiz
- Mapper la sortie RAG/IA vers une structure exploitable par le jeu (ex. questions, réponses, difficulté).
- Définir les champs minimaux pour le MVP (texte question, réponses possibles, bonne réponse, niveau facile/difficile).

### 2.1.3 Intégration dans le moteur de jeu (Godot)
- Consommer l’API depuis GDScript/C# et injecter les questions dans la mécanique de quiz.
- Gérer le cas où l’API est indisponible ou renvoie peu de données (fallback ou message clair).
