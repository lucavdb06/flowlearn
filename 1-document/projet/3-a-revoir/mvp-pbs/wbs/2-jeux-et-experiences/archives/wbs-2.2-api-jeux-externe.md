# WBS – 2.2 API jeux → externe

**PBS :** Permettre, selon une bonne ou mauvaise réponse, d’avoir des conséquences même en dehors du jeu (exemple avec une ESP32).

---

## Features (WBS)

### 2.2.1 Conception du schéma JSON
- Définir la structure du JSON envoyé par le jeu (id_question, difficulté, bonne_réponse, etc.).
- Documenter le contrat d’API pour que le code Rust/ESP32 puisse l’interpréter sans ambiguïté.

### 2.2.2 Implémentation de l’API côté jeu (Godot)
- Développer en GDScript/C# une API qui envoie le JSON à chaque réponse de l’utilisateur.
- Gérer les cas de réussite/échec et la notion de difficulté (question facile vs difficile).

### 2.2.3 Interpréteur JSON côté Rust
- Écrire un module Rust qui reçoit le JSON, le valide et extrait les champs utiles.
- Mapper les règles pédagogiques vers des actions physiques :
  - Si l’utilisateur répond correctement à une question **facile** → déclencher l’envoi de **1 bonbon (1 M&M)**.
  - Si l’utilisateur répond correctement à une question **difficile** → déclencher l’envoi de **2 bonbons (2 M&Ms)**.

### 2.2.4 Intégration ESP32 & moteur distributeur
- Implémenter le protocole de communication entre Rust et l’ESP32 (série, Wi-Fi ou autre).
- Piloter le moteur du distributeur de M&Ms en fonction du nombre de bonbons à délivrer.
- Sécuriser le fonctionnement (éviter le sur-distribution, gérer les erreurs matérielles).
