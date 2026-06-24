# DOD – 3.3 Ingestion & RAG « Le Bibliothécaire »

**PBS :** Implémenter le module d'ingestion de documents (LlamaIndex) et le moteur de recherche RAG pour alimenter l'orchestrateur d'agents (3.4) et le générateur de quiz (3.5).

---

## Comment valider chaque feature

### 3.3.1 Pipeline d'ingestion (LlamaIndex)

**Cas d'erreur à gérer :**
- Fichier corrompu ou format non supporté : rejet propre avec message ou log, pas de crash.
- PDF sans texte extractible (images uniquement) : comportement défini (skip, OCR futur, ou message clair).
- Fichier trop volumineux : limite documentée et gérée (chunking ou rejet).

**Feature validée si :** au moins un type PDF et un type texte sont ingérés ; le chunking produit des segments cohérents (taille/overlap documentés) et les chunks sont tracés jusqu'au document source.

---

### 3.3.2 Indexation et écriture dans la base vectorielle

**Cas d'erreur à gérer :**
- Échec du modèle d'embedding (API down, quota) : retry, file d'attente ou échec explicite sans perte de données partielles incohérentes.
- Conflit ou doublon (ré-ingestion) : stratégie claire (upsert, remplacement par document, ou versioning) et appliquée de façon déterministe.

**Feature validée si :** chaque chunk ingéré possède un embedding et est persisté dans la base avec ses métadonnées ; une ré-ingestion (totale ou partielle) est testée et ne laisse pas la base dans un état incohérent.

---

### 3.3.3 Moteur de recherche RAG (retrieval)

**Cas d'erreur à gérer :**
- Base vide ou aucune similarité au-dessus du seuil : retour structuré (liste vide ou message explicite), pas d'exception non gérée.
- Requête mal formée ou embedding indisponible : validation en entrée, erreur 4xx ou message clair côté consommateur.

**Feature validée si :** une requête (texte ou embedding) renvoie les N chunks les plus pertinents dans un format stable (JSON/Pydantic) ; le contrat est documenté et un consommateur (ex. orchestrateur 3.4 ou générateur de quiz 3.5) peut l'utiliser sans ambiguïté. Les critères PBS « indexation réussie dans Supabase/PostgreSQL, recherche pertinent » sont satisfaits.
