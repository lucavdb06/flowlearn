# DOD – 3.2 Base de Connaissances Vectorielle

**PBS :** Mettre en place la base de connaissances vectorielle (PostgreSQL / Supabase + pgvector) pour stocker les documents, chunks et embeddings nécessaires au RAG.

---

## Comment valider chaque feature

### 3.2.1 Mise en place de la base vectorielle (PostgreSQL / Supabase pgvector)

**Cas d'erreur à gérer :**
- Connexion refusée ou timeout : message explicite, pas de crash ; retry ou configuration documentée.
- Extension pgvector absente : script ou procédure de migration documentée pour l'activer.

**Feature validée si :** la base est accessible depuis le backend, pgvector est opérationnel, et la connexion utilise des variables d'environnement (aucun secret en dur) ; un autre développeur peut reproduire l'environnement à partir de la doc.

---

### 3.2.2 Schéma de stockage des embeddings et métadonnées

**Cas d'erreur à gérer :**
- Données manquantes ou incohérentes (embedding NULL, document sans chunks) : contraintes ou validation à l'insertion pour éviter des états invalides.
- Évolution du schéma : migrations versionnées et documentées.

**Feature validée si :** le schéma est en place (tables documents, chunks, embeddings, métadonnées), documenté, et les champs nécessaires au RAG et au multi-utilisateur/RGPD sont identifiés ou prévus.
