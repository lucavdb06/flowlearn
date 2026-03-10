# DOD – 2.2 API jeux → externe

**PBS :** Permettre, selon une bonne ou mauvaise réponse, d’avoir des conséquences même en dehors du jeu (exemple avec une ESP32).

---

## Comment valider chaque feature

### 2.2.1 Conception du schéma JSON

**Cas d’erreur à gérer :**
- JSON invalide ou hors contrat : doc ou exemples doivent permettre de rejeter proprement côté récepteur.

**Feature validée si :** le schéma est écrit, documenté et un exemple valide est fourni ; un développeur Rust peut implémenter le parsing sans questions supplémentaires.

---

### 2.2.2 Implémentation de l’API côté jeu (Godot)

**Cas d’erreur à gérer :**
- Envoi échoué (réseau, récepteur down) : pas de crash, retry ou message ; pas d’envoi en double.

**Feature validée si :** chaque réponse du joueur génère un envoi JSON correct (réussite/échec + difficulté) et le récepteur reçoit les données attendues.

---

### 2.2.3 Interpréteur JSON côté Rust

**Cas d’erreur à gérer :**
- JSON invalide ou champs manquants : parsing échoue proprement (pas de panic), erreur ou valeur par défaut.
- Valeur « difficulté » inconnue : comportement par défaut défini (ex. 0 bonbon).

**Feature validée si :** Rust parse le JSON, valide les champs et applique les règles (1 bonbon / 2 bonbons / 0) selon difficulté et bonne/mauvaise réponse ; tests unitaires ou scénarios manuels le confirment.

---

### 2.2.4 Intégration ESP32 & moteur distributeur

**Cas d’erreur à gérer :**
- Sur-distribution : limite (ex. max par partie, timeout) pour éviter de délivrer trop de bonbons.
- Panne moteur, communication coupée : retry, log ou alerte, pas de blocage infini.

**Feature validée si :** une bonne réponse facile donne 1 M&M et une bonne réponse difficile 2 M&Ms, physiquement délivrés ; les garde-fous (sécurité, erreurs) sont en place et testés.
