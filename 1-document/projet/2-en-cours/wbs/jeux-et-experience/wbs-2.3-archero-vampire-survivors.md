# WBS – 2.3 Type de jeu : style « Archero » / « Vampire Survivors »

**PBS :** Top-down, déplacement libre, vagues d’ennemis, récompenses (quiz → IoT possible).

---

## Features (WBS)

### 2.3.1 Déplacement du personnage

- Contrôles (clavier / manette / tactile) et collision avec la carte.

### 2.3.2 Apparition (spawn) des monstres

- Spawn aléatoire des ennemis sur la carte (zones ou points prédéfinis).

### 2.3.3 Variété des ennemis (3 types de monstres)

- Définir 3 types distincts (comportement, stats, apparence).
- Intégration dans le système de spawn et de récompenses/quiz si prévu.

### 2.3.4 Variété des armes (3 armes)

- Implémenter 3 armes différentes (portée, dégâts, cadence ou effet).
- Boucle de tir / compétence et feedback visuel.

### 2.3.5 Carte / niveau désigné

- Créer ou désigner une carte de jeu (arène, limites, obstacles).
- Intégration avec le spawn et le déplacement (zones jouables, respawn).

### 2.3.6 evolution de la difficulter :

- Augmenter le rythme ou la densité de spawn au fur du temps (courbe de difficulté).

### 2.3.6 Intégrer la mécanique de gameplay quiz (MVP)

- Déclencher le quiz à des moments clés du jeu (ex. après N ennemis éliminés, sur ramassage d’objet, niveau atteint).
- Afficher les questions issues de l’API RAG/IA (2.1) dans l’interface du jeu (HUD, pop-up ou overlay cohérent avec le style).
- Traiter la réponse (bonne / mauvaise) et l’utiliser comme mécanique de gameplay : bonus (dégâts, soin, buff), malus ou neutre selon le cas.
- Relayer le résultat (et la difficulté) vers l’API jeux → externe (2.2) pour les récompenses tangibles (ex. distribution M&Ms sur ESP32).
- S’assurer que le quiz reste une mécanique principale et fluide (pas une pause arbitraire), intégrable de la même façon dans d’autres jeux du SDK.
