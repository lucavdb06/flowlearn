# WBS – 1.1 Encapsulateurs de Déploiement

**PBS :** Adapter l’application React web en logiciel bureau (Electron) et en application mobile (Capacitor) pour un déploiement multiplateforme.

---

## Features (WBS)

### 1.1.1 Configuration Electron (Desktop)
- Intégrer Electron au projet React existant (build, scripts, configuration).
- Définir le point d’entrée et le chargement de l’app web dans la fenêtre bureau.
- Gérer le packaging pour Windows et Mac (installables ou exécutables).

### 1.1.2 Configuration Capacitor (Mobile)
- Intégrer Capacitor au projet React pour cibler iOS et Android.
- Configurer les projets natifs (Xcode, Android Studio) et les chemins de build.
- Vérifier que l’app web se charge correctement dans le WebView (URL, CORS, API).

### 1.1.3 Build et livraison
- Mettre en place les scripts ou pipelines de build pour chaque plateforme (web, Electron, Capacitor).
- Documenter les étapes pour produire un installable Desktop et un binaire ou APK/IPA mobile à partir du même code source.
