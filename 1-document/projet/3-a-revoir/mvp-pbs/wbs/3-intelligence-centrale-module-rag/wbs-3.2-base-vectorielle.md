# WBS – 3.2 Base de Connaissances Vectorielle

**PBS :** Mettre en place la base de connaissances vectorielle (PostgreSQL / Supabase + pgvector) pour stocker les documents, chunks et embeddings nécessaires au RAG.

---

## Features (WBS)

### 3.2.1 Mise en place de la base vectorielle (PostgreSQL / Supabase pgvector)
- Créer ou configurer l'instance PostgreSQL / Supabase dédiée au RAG.
- Activer l'extension **pgvector** et vérifier son bon fonctionnement.
- Exposer une connexion sécurisée pour le backend FastAPI / LlamaIndex (variables d'environnement, pas de secrets en dur dans le code).

### 3.2.2 Schéma de stockage des embeddings et métadonnées
- Définir le schéma de base :
  - table des documents (source, type, propriétaire, thème),
  - table des chunks (texte, position, id_document),
  - colonne ou table d'**embeddings** (vecteur, modèle utilisé, date de génération).
- Prévoir le multi‑utilisateur / multi‑namespace (cours par utilisateur, RGPD : suppression et anonymisation possibles).
- Rédiger un court document de référence (diagramme ou description textuelle du schéma).
