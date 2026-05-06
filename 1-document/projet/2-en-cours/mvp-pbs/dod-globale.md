# Definition of Done (DOD) - Contrat de Qualité (globale)

Ce document définit les critères obligatoires à remplir avant qu'un élément (tâche WBS ou User Story) ne soit considéré comme "Terminé" (Done).

## 1. Socle Commun (Applicable à tout le projet)

Peu importe la phase, aucun code ne peut être validé sans ces 4 piliers :

- **Code Review Technique :** Le code a été relu par au moins un autre développeur (Peer Review).
- **Documentation :** Le code est commenté et la documentation technique est mise à jour sur le github.
- **Absence de Régressions :** La nouvelle fonctionnalité ne casse pas l'existant.
- **Push Final :** Le code est mergé sur la branche principale de **GitHub** et les fichiers "propres" sont sur le Wiki.

## 2. DOD Spécifique - Phase 1 (Construction du MVP)

_Cadre : Approche prédictive / WBS_

Pour cette phase, la rigueur est maximale pour garantir la sécurité du lancement.

| Critère                 | Responsable       | Description                                                                                                                                                                                                           |
| ----------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Audit Cybersécurité** | Pôle Sécurité     | La revue de code spécifique aux failles a été effectuée et les vulnérabilités critiques sont corrigées.                                                                                                               |
| **Conformité Specs**    | Porteur de projet | La tâche répond exactement au besoin décrit dans le cahier des charges initial.                                                                                                                                       |
| **Tests Automatisés**   | Équipe Dev        | En l'absence de serveur dédié, le composant doit être fonctionnel sur les machines locales des développeurs et valider l'intégralité des tests automatisés sur GitHub (Actions). La portabilité du code est vérifiée. |
|                         |                   |                                                                                                                                                                                                                       |

## 3. DOD Spécifique - Phase 2 (Évolutions Agile)

_Cadre : Approche itérative / Sprints_

Ici, on ajoute des critères de validation par l'usage.

| Critère                   | Responsable   | Description                                                                                 |
| ------------------------- | ------------- | ------------------------------------------------------------------------------------------- |
| **Validation User Story** | Product Owner | La fonctionnalité répond aux critères d'acceptation de la User Story.                       |
| **Tests Utilisateurs**    | Équipe        | La fonctionnalité a été testée par au moins un utilisateur "test" et est jugée ergonomique. |
| **Tests Automatisés**     | Équipe Dev    | Les tests unitaires et d'intégration sont écrits et passent avec succès.                    |

## 4. Processus de Validation

1. **Développement :** Le développeur réalise la tâche sur une branche isolée.
2. **Validation locale et Tests :** Le développeur vérifie le bon fonctionnement de son code en local et exécute les tests unitaires pour s'assurer que l'intégralité des tests passe sans régression.
3. **Ouverture de Pull Request (PR) :** Le développeur soumet son code sur GitHub. Ce dépôt déclenche les tests automatisés (GitHub Actions) pour valider l'intégrité du code.
4. **Cyber Security Review :** Le pôle cybersécurité intervient sur la PR pour analyser les failles potentielles.
5. **Validation du Check Cyber :** Une fois la revue effectuée et les corrections validées, le responsable cyber valide le "check" de sécurité sur GitHub. Cette étape est bloquante pour la fusion.
6. **Revue Finale (Tech Lead / Porteur de projet) :** Une dernière relecture est effectuée par le responsable technique ou le porteur de projet pour valider la cohérence globale et la qualité du code avant le merge final.
7. **Changement de statut :** Après validation de tous les checks (Cyber + Tech Review), le code est fusionné et la tâche passe de "In Progress" à "Done" sur **GitHub Projects**.

# Notes correction :

- pour chaque fonctionalité crée un process pour validé la feature.
- exemple du logging
- plus micro la on est en dod macro
- “nos test”
