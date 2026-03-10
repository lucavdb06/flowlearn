# DOD – 4.1 Algorithme de Sélection des Questions

**PBS :** Décider quelle question poser via une méthode de répétition espacée type Anki (globale) ou une sélection manuelle d'un thème choisi par l'utilisateur.

---

## Comment valider chaque feature

### 4.1.1 Modèle de données pour la sélection

**Cas d'erreur à gérer :**
- Champs obligatoires manquants (id_question, id_user, thème, timestamps) : refus d'enregistrement ou valeurs par défaut explicites.
- Incohérences (date de dernière revue dans le futur, niveau de maîtrise invalide) : validation côté backend.

**Feature validée si :** les schémas/tables existent et sont documentés ; pour un utilisateur de test, l'historique des réponses est bien enregistré après chaque question ; une requête permet de retrouver les réponses d'un utilisateur sur un thème donné.

---

### 4.1.2 Logique de répétition espacée (type Anki)

**Cas d'erreur à gérer :**
- Aucune question « due » dans le SRS : bascule propre sur de nouvelles cartes ou autre mode, pas de boucle infinie.
- Données manquantes pour calculer l'intervalle (première réponse) : comportement par défaut documenté.

**Feature validée si :** sur un jeu de test, une suite de réponses fait évoluer les intervalles comme prévu ; les cartes en retard sont proposées avant les nouvelles ; la logique fonctionne en mode global et en mode thème ciblé.

---

### 4.1.3 Endpoint / API « prochaine question »

**Cas d'erreur à gérer :**
- Aucun contenu pour le thème demandé : réponse explicite (code/message), fallback possible côté client.
- Erreur interne (DB, RAG) : erreur propre (5xx + log), pas de crash côté jeu.

**Feature validée si :** l'endpoint renvoie un JSON valide respectant le contrat (question, réponses, bonne réponse, métadonnées) ; en enchaînant les appels, pas de répétition abusive et prise en compte de l'historique ; exemples de requêtes/réponses documentés.
