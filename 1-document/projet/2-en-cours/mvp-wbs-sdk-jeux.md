### 2. Jeux et Expériences

#### A. SDK Jeux (Moteur Godot)

pbs :

- **2.1 API RAG/IA → jeux**
  - Récupérer des informations venant du cours pour alimenter la mécanique de gameplay du quiz (MVP).

wbs :

- 2.1.1 Exposition ou consommation de l’API RAG/IA
  - Définir l’endpoint (ou le flux) qui renvoie du contenu pédagogique issu du cours (RAG/IA).
  - dot : S’assurer que le jeu peut appeler cette API (HTTP, format de réponse stable).

- 2.1.2 Transformation contenu cours → données quiz
  - Mapper la sortie RAG/IA vers une structure exploitable par le jeu (ex. questions, réponses, difficulté).
  - Définir les champs minimaux pour le MVP (texte question, réponses possibles, bonne réponse, niveau facile/difficile).

- 2.1.3 Intégration dans le moteur de jeu (Godot)
  - Consommer l’API depuis GDScript/C# et injecter les questions dans la mécanique de quiz.
  - Gérer le cas où l’API est indisponible ou renvoie peu de données (fallback ou message clair).

**pbs :**

- **2.2 api jeux -> externe**
  - permettre si une bonne ou mauvaise d'avoir des conséquence même en dehors du jeux (exemple avec une esp32)

**wbs :**

- 2.2.1 Conception du schéma JSON
  - Définir la structure du JSON envoyé par le jeu (id_question, difficulté, bonne_réponse, etc.).
  - Documenter le contrat d’API pour que le code Rust/ESP32 puisse l’interpréter sans ambiguïté.

- 2.2.2 Implémentation de l’API côté jeu (Godot)
  - Développer en GDScript/C# une API qui envoie le JSON à chaque réponse de l’utilisateur.
  - Gérer les cas de réussite/échec et la notion de difficulté (question facile vs difficile).

- 2.2.3 Interpréteur JSON côté Rust
  - Écrire un module Rust qui reçoit le JSON, le valide et extrait les champs utiles.
  - Mapper les règles pédagogiques vers des actions physiques :
    - Si l’utilisateur répond correctement à une question **facile** → déclencher l’envoi de **1 bonbon (1 M&M)**.
    - Si l’utilisateur répond correctement à une question **difficile** → déclencher l’envoi de **2 bonbons (2 M&Ms)**.

- 2.2.4 Intégration ESP32 & moteur distributeur
  - Implémenter le protocole de communication entre Rust et l’ESP32 (série, Wi-Fi ou autre).
  - Piloter le moteur du distributeur de M&Ms en fonction du nombre de bonbons à délivrer.
  - Sécuriser le fonctionnement (éviter le sur-distribution, gérer les erreurs matérielles).

pbs :

#### C. jeux :

pbs :

- **2.3 Type de jeu : style « Archero » / « Vampire Survivors »**
  - Top-down, déplacement libre, vagues d’ennemis, récompenses (quiz → IoT possible).

wbs :

- 2.3.1 Déplacement du personnage
  - Contrôles (clavier / manette / tactile) et collision avec la carte.
  - Déplacement fluide et réactif (vitesse, orientation).

- 2.3.2 Apparition (spawn) des monstres
  - Spawn aléatoire des ennemis sur la carte (zones ou points prédéfinis).
  - Augmenter le rythme ou la densité de spawn au fur du temps (courbe de difficulté).

- 2.3.3 Variété des ennemis (3 types de monstres)
  - Définir 3 types distincts (comportement, stats, apparence).
  - Intégration dans le système de spawn et de récompenses/quiz si prévu.

- 2.3.4 Variété des armes (3 armes)
  - Implémenter 3 armes différentes (portée, dégâts, cadence ou effet).
  - Boucle de tir / compétence et feedback visuel.

- 2.3.5 Carte / niveau désigné
  - Créer ou désigner une carte de jeu (arène, limites, obstacles).
  - Intégration avec le spawn et le déplacement (zones jouables, respawn).

- 2.3.6 Intégrer la mécanique de gameplay quiz (MVP)
  - Déclencher le quiz à des moments clés du jeu (ex. après N ennemis éliminés, sur ramassage d’objet, niveau atteint).
  - Afficher les questions issues de l’API RAG/IA (2.1) dans l’interface du jeu (HUD, pop-up ou overlay cohérent avec le style).
  - Traiter la réponse (bonne / mauvaise) et l’utiliser comme mécanique de gameplay : bonus (dégâts, soin, buff), malus ou neutre selon le cas.
  - Relayer le résultat (et la difficulté) vers l’API jeux → externe (2.2) pour les récompenses tangibles (ex. distribution M&Ms sur ESP32).
  - S’assurer que le quiz reste une mécanique principale et fluide (pas une pause arbitraire), intégrable de la même façon dans d’autres jeux du SDK.
