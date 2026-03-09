# DOD – 2.3 Type de jeu : style « Archero » / « Vampire Survivors »

**PBS :** Jeux de survie casual.

---

## Comment valider chaque feature

### 2.3.1 Déplacement du personnage

**Cas d’erreur à gérer :**
- Contrôles non répondants ou conflit clavier/manette/tactile : priorité définie, pas de blocage.
- Collision manquante : personnage ne doit pas sortir de la carte ou traverser les murs.

**Feature validée si :** le joueur peut se déplacer avec les contrôles prévus et les collisions avec la carte se comportent correctement.

---

### 2.3.2 Apparition (spawn) des monstres

**Cas d’erreur à gérer :**
- Spawn dans les murs ou hors carte : zones/spawn points validés pour éviter positions invalides.
- Trop de spawns (perf / lisibilité) : limite ou rythme plafonné si besoin.

**Feature validée si :** les monstres spawnent de façon cohérente dans les zones prévues et sont visibles/jouables.

---

### 2.3.3 Variété des ennemis (3 types de monstres)

**Cas d’erreur à gérer :**
- Type d’ennemi inconnu ou manquant : fallback ou type par défaut pour éviter crash.
- Stats incohérentes (PV ≤ 0, etc.) : validation des données ou valeurs par défaut.

**Feature validée si :** 3 types de monstres sont jouables, distincts et intégrés au spawn (et au quiz si applicable).

---

### 2.3.4 Variété des armes (3 armes)

**Cas d’erreur à gérer :**
- Arme inconnue ou non chargée : pas de crash, arme par défaut ou message.
- Tir sans cible / dégâts à 0 : comportement défini (feedback visuel ou sonore, pas de freeze).

**Feature validée si :** 3 armes sont utilisables, distinctes et donnent un feedback visuel et gameplay clair.

---

### 2.3.5 Carte / niveau désigné

**Cas d’erreur à gérer :**
- Carte non chargée ou corrompue : message d’erreur, pas de crash ; retry ou niveau fallback.
- Respawn dans un mur ou hors zone jouable : points de respawn validés.

**Feature validée si :** la carte est jouable, les limites et obstacles sont respectés par le déplacement et le spawn.

---

### 2.3.6 Évolution de la difficulté

**Cas d’erreur à gérer :**
- Difficulté qui n’évolue pas (bug timer/vague) : seuils ou courbe testables.
- Montée trop brutale : plafond ou limite pour rester jouable.

**Feature validée si :** la difficulté évolue de manière observable (spawn, dégâts, nombre d’ennemis, etc.) pendant une partie.

---

### 2.3.7 Intégrer la mécanique de gameplay quiz (MVP)

**Cas d’erreur à gérer :**
- API 2.1 indisponible ou sans questions : fallback (questions par défaut ou message), pas de blocage du jeu.
- API 2.2 indisponible (envoi résultat) : pas de crash ; retry, file d’attente ou message ; récompense tangible reportée ou indiquée.
- Réponse joueur non enregistrée ou doublon : un seul envoi par réponse, idempotence si besoin.

**Feature validée si :** le quiz se déclenche aux moments prévus, utilise l’API 2.1, affiche et traite les réponses avec des effets en jeu, et relaie vers 2.2 pour les récompenses ; l’ensemble reste fluide et réutilisable.
