### 4. Algorithmes de Personnalisation

- pbs :

**4.1 Algorithme de Sélection des Questions**  
 Méthode de répétition espacée type Anki (globale) ou sélection manuelle d'un thème choisi par l'utilisateur.

- wbs :
  - 4.1.1 Modèle de données pour la sélection
    - Définir les champs nécessaires (id_question, thème, date_dernière_revue, niveau_maîtrise, succès/échec, intervalle SRS).
    - Stocker l’historique des réponses par utilisateur (lié à la base RAG / cours).

  - 4.1.2 Logique de répétition espacée (type Anki)
    - Implémenter le calcul de la prochaine date de revue et de l’intervalle selon la performance (bonne/mauvaise réponse).
    - Exposer une règle « prochaine question à revoir » (priorité aux cartes dues, puis nouvelles).

pbs :

- **4.2 algorithme de rétention**  
   Système de scoring basé sur les KPIs récoltés. Le but de l'algorithme est de cibler le profil utilisateur pour maximiser son taux de rétention sur l'application.
  wbs :
