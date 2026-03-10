# DOD – 4.2 Algorithme de Rétention (Moteur de ciblage / Hook)

**PBS :** Système de scoring basé sur les KPIs récoltés. Le but de l'algorithme est de cibler le profil utilisateur pour maximiser son taux de rétention sur l'application.

---

## Comment valider chaque feature

### 4.2.1 Modèle de données pour les KPIs

**Cas d'erreur à gérer :**
- Événement incomplet (timestamp manquant, type non supporté) : rejet ou normalisation avec log.
- Volume excessif (spam d'événements) : politique de rétention ou d'agrégation définie.

**Feature validée si :** pour une session de test, les événements (réponses, abandons, durée) sont stockés et consultables ; un moyen simple (requêtes ou outil) permet de visualiser les KPIs de base par utilisateur.

---

### 4.2.2 Moteur de scoring utilisateur

**Cas d'erreur à gérer :**
- KPIs manquants ou partiels : score retombe sur des valeurs par défaut, pas de crash.
- Profil utilisateur inexistant (nouveau user) : score initial défini, pas de division par zéro.

**Feature validée si :** pour plusieurs profils simulés (bon élève, en difficulté, abandons), le score correspond qualitativement aux attentes ; le moteur de sélection (4.1) peut consommer ce score (types et formats compatibles).

---

### 4.2.3 Adaptation de l'expérience (boucle Hook éthique)

**Cas d'erreur à gérer :**
- Score aberrant (hors plage) : clamp ou normalisation avant décision de difficulté.
- Changement de difficulté trop fréquent (effet yo-yo) : règles de lissage ou fenêtres temporelles.

**Feature validée si :** en test, après bonnes réponses la difficulté augmente de manière observable, après échecs elle baisse ou la cadence se calme ; les règles sont documentées et validées (pas de comportement manipulatoire).

---

### 4.2.4 API / Contrat de données avec le jeu

**Cas d'erreur à gérer :**
- Événements au mauvais format : rejet clair, logs, pas de crash ni blocage dans la boucle de jeu.
- Latence ou indisponibilité du service : le jeu continue avec paramètres par défaut, l'utilisateur n'est pas bloqué.

**Feature validée si :** le jeu peut envoyer des événements à l'API et recevoir un ACK en scénario normal ; exemples de payloads JSON testés et partagés ; évolutions de contrat versionnées (v1, v2…) pour ne pas casser les intégrations.
