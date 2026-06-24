# DOD – 1.1 Encapsulateurs de Déploiement

**PBS :** Adapter l’application React web en logiciel bureau (Electron) et en application mobile (Capacitor) pour un déploiement multiplateforme.

---

## Comment valider chaque feature

### 1.1.1 Configuration Electron (Desktop)

**Cas d’erreur à gérer :**
- Build Electron échoué (dépendances, Node version) : procédure documentée ou script reproductible.
- Fenêtre blanche ou app non chargée : vérifier l’URL / le chemin du bundle et les logs.

**Feature validée si :** l’application s’ouvre en mode bureau sur au moins une cible (Windows ou Mac) ; un autre développeur peut lancer le build à partir de la doc.

---

### 1.1.2 Configuration Capacitor (Mobile)

**Cas d’erreur à gérer :**
- Projet natif non généré ou erreur de build : étapes de configuration documentées (SDK, clés, etc.).
- App qui ne charge pas ou erreur réseau dans le WebView : CORS, URL de l’API et permissions vérifiés.

**Feature validée si :** l’app tourne dans l’émulateur ou sur un appareil (iOS ou Android) à partir du même code React ; les appels API nécessaires fonctionnent.

---

### 1.1.3 Build et livraison

**Cas d’erreur à gérer :**
- Build d’une plateforme qui casse une autre : isolation des configs ou documentation des prérequis par plateforme.

**Feature validée si :** on peut produire, à partir du repo, un livrable Desktop et un livrable mobile (ou émulateur) ; les étapes sont documentées et reproductibles.
