# WBS – 4.2 Algorithme de Rétention (Moteur de ciblage / Hook)

**PBS :** Système de scoring basé sur les KPIs récoltés. Le but de l'algorithme est de cibler le profil utilisateur pour maximiser son taux de rétention sur l'application.

---

## Features (WBS)

### 4.2.1 Modèle de données pour les KPIs
- Définir les KPIs à collecter (durée de session, nombre de questions, ratio bonnes/mauvaises réponses, abandons, événements jeu).
- Définir la structure de stockage (tables / agrégats par utilisateur, par session).

### 4.2.2 Moteur de scoring utilisateur
- Implémenter un score de profil (engagement, difficulté perçue, fatigue) à partir des KPIs.
- Mettre à jour le score selon les règles définies (bonnes réponses, temps passé, décrochage).

### 4.2.3 Adaptation de l'expérience (boucle Hook éthique)
- Faire en sorte que le scoring influence la difficulté des questions renvoyées (cf. 2.1 / 4.1).
- Définir les règles d'adaptation (augmenter / diminuer la difficulté, proposer des pauses) en respectant la charte éthique du projet.

### 4.2.4 API / Contrat de données avec le jeu
- Exposer un endpoint (ex. POST /session-event) pour recevoir les événements du jeu (format JSON unifié).
- Documenter le schéma des événements et des réponses (recommandations, paramètres pour 4.1).
