# WBS – 5.1 Coffre-fort & Protection RGPD

**PBS :** Assurer la protection des données personnelles et des données d’apprentissage (conformité RGPD) et sécuriser l’architecture (accès, secrets, audit).

---

## Features (WBS)

### 5.1.1 Politique de données et consentement
- Documenter les données collectées (comptes, cours, réponses, KPIs) et leurs finalités.
- Mettre en place les mécanismes de consentement et d’information utilisateur (mentions légales, politique de confidentialité).
- Prévoir les droits RGPD : accès, rectification, suppression, portabilité.

### 5.1.2 Sécurisation des accès et des secrets
- Aucun secret (clés API, mots de passe DB) en dur dans le code ; utilisation de variables d’environnement ou coffre (ex. secrets manager).
- Authentification et autorisation des utilisateurs (identification, rôles si besoin) pour l’accès aux données et aux API.
- Connexions base de données et APIs externes en HTTPS / connexions sécurisées.

### 5.1.3 Suppression et rétention des données
- Implémenter la suppression de compte et des données associées (documents, chunks, historique, KPIs) de manière complète et traçable.
- Définir une politique de rétention (durée de conservation des logs, des données d’apprentissage) et la documenter.

### 5.1.4 Audit et revue de sécurité
- Répondre aux points soulevés par le pôle cybersécurité (revue de code, bonnes pratiques).
- Corriger les vulnérabilités critiques identifiées avant mise en production ; documenter les décisions (ex. risques acceptés).
