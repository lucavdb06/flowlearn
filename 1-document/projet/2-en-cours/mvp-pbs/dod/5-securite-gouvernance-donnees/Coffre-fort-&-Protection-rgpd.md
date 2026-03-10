# DOD – 5.1 Coffre-fort & Protection RGPD

**PBS :** Assurer la protection des données personnelles et des données d’apprentissage (conformité RGPD) et sécuriser l’architecture.

---

## Comment valider chaque feature

### 5.1.1 Politique de données et consentement

**Cas d’erreur à gérer :**
- Utilisateur non informé ou consentement non tracé : processus d’inscription et mentions à jour.
- Demande d’exercice de droits (accès, suppression) non traitée : processus documenté et testé.

**Feature validée si :** une politique de confidentialité (ou équivalent) décrit les données et finalités ; les droits RGPD sont documentés et un parcours de suppression de compte existe (au moins en doc ou en backlog priorisé).

---

### 5.1.2 Sécurisation des accès et des secrets

**Cas d’erreur à gérer :**
- Secret exposé dans le code ou les logs : revue et suppression ; utilisation exclusive d’env ou coffre.
- Accès non authentifié à des données personnelles : contrôle d’accès sur les endpoints et les données sensibles.

**Feature validée si :** aucun secret en dur ; les accès aux API et aux données utilisateur sont protégés (auth, HTTPS) ; la revue sécurité a validé les points critiques ou les corrections sont planifiées.

---

### 5.1.3 Suppression et rétention des données

**Cas d’erreur à gérer :**
- Suppression partielle (données orphelines) : procédure de suppression en cascade ou listée, testée.
- Logs ou backups contenant des données personnelles au-delà de la rétention : politique documentée et appliquée.

**Feature validée si :** la suppression de compte supprime ou anonymise les données associées (compte, documents, historique, KPIs) de manière vérifiable ; la politique de rétention est documentée.

---

### 5.1.4 Audit et revue de sécurité

**Cas d’erreur à gérer :**
- Vulnérabilité critique non traitée : correction ou plan de remédiation validé par le pôle sécurité.

**Feature validée si :** la revue de code sécurité (pôle cybersécurité) a été effectuée ; les vulnérabilités critiques sont corrigées ou documentées (risque accepté) ; le livrable est aligné avec les critères du dictionnaire PBS (conformité légale, suppression de compte OK, failles auditées).
