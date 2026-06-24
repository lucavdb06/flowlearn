# WBS – 4.1 Algorithme de Sélection des Questions

**PBS :** Décider quelle question poser via une méthode de répétition espacée type Anki (globale) ou une sélection manuelle d'un thème choisi par l'utilisateur.

---

## Features (WBS)

### 4.1.1 Modèle de données pour la sélection
- Définir les champs nécessaires (id_question, thème, date_dernière_revue, niveau_maîtrise, succès/échec, intervalle SRS).
- Stocker l'historique des réponses par utilisateur (lié à la base RAG / cours).
- Concevoir les tables ou schémas en base pour persister l'état SRS par utilisateur et par question.

### 4.1.2 Logique de répétition espacée (type Anki)
- Implémenter le calcul de la prochaine date de revue et de l'intervalle selon la performance (bonne/mauvaise réponse).
- Exposer une règle « prochaine question à revoir » (priorité aux cartes dues, puis nouvelles).
- Gérer le mode global (tous les cours) et le mode thème ciblé (sélection manuelle par l'utilisateur).

### 4.1.3 Endpoint / API « prochaine question »
- Exposer un endpoint (ex. GET /next-question) qui renvoie une question au format JSON standardisé (cf. 2.3).
- Intégrer l'algorithme de sélection avec la base RAG (choix du thème / des chunks pertinents).
- Gérer les cas sans question disponible (thème vide, aucune carte due) : réponse explicite ou fallback.
