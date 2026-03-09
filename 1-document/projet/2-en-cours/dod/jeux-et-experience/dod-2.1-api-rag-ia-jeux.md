# DOD – 2.1 API RAG/IA → jeux

**PBS :** Récupérer des informations venant du cours pour alimenter la mécanique de gameplay du quiz (MVP).

---

## Comment valider chaque feature

### 2.1.1 Exposition ou consommation de l’API RAG/IA

**Cas d’erreur à gérer :**
- Timeout ou réponse 5xx : le client ne plante pas, erreur exploitable (retry ou message).
- Réseau coupé ou pas de réponse : pas de crash, comportement défini.

**Feature validée si :** le jeu peut appeler l’API en HTTP et obtenir une réponse structurée ; le contrat (format) est documenté et stable.

---

### 2.1.2 Transformation contenu cours → données quiz

**Cas d’erreur à gérer :**
- Réponse vide ou champs manquants : comportement défini (ignorer, fallback, message).
- Champs mal typés ou inattendus : pas de crash, validation et repli propre.

**Feature validée si :** la sortie RAG/IA est transformée en structure quiz complète et le moteur de jeu l’utilise sans crash ; les champs minimaux MVP sont toujours présents ou gérés.

---

### 2.1.3 Intégration dans le moteur de jeu (Godot)

**Cas d’erreur à gérer :**
- API indisponible : message clair à l’utilisateur et/ou mode fallback (ex. questions par défaut), pas de crash.
- 0 ou très peu de questions : pas d’écran vide ni boucle infinie ; message, réessai ou fallback.

**Feature validée si :** le quiz en jeu utilise les questions venant de l’API ; en cas d’indisponibilité ou de peu de données, le comportement est prévisible et l’utilisateur est informé ou a un fallback.
