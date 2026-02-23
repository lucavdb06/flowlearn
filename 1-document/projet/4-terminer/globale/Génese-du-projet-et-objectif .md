status : terminer

# Document de Genèse et Objectifs : DopaLearn

**Projet :** FlowLearn

## 1. Genèse du Projet

### 1.1. Le Constat (Le Problème)

Le projet naît d'une observation de la psychologie cognitive moderne : la "friction de l'apprentissage".
L'apprentissage traditionnel est perçu comme une activité à haute charge mentale, souvent incompatible avec les moments de fatigue ou les micro-pauses (temps d'attente, transports). À l'inverse, les mécanismes de "doomscrolling" (TikTok, Instagram) exploitent la libération de dopamine pour créer une addiction sans effort.

**Le problème identifié :** La connaissance est souvent stockée de manière statique, dispersée et pénible à consulter ou à importer. Le passage de la prise de notes à la révision constitue une rupture de flux (friction) qui décourage l'utilisateur sur la durée et le pousse à abandonner les applications de révision classiques.

### 1.2. La Vision (La Solution)

DopaLearn a pour ambition de **détourner les mécaniques addictives** au profit de l'éducation en créant un environnement qui diminue toutes les frictions au maximum. Le projet exploite la puissance des mécanismes de dopamine pour servir l'apprentissage, et non pour maximiser des revenus publicitaires.

- **Construction de son cours (Zéro Saisie) :** L'idée est de supprimer l'effort de préparation. Le système interagit avec l'utilisateur pendant ses phases de jeu ou de scroll ("Qu'as-tu appris aujourd'hui ?"). La base de connaissances se construit ainsi de manière organique et conversationnelle, sans obliger l'utilisateur à ressaisir ses notes ou à importer manuellement des PDF (bien que l'import externe reste possible).
- **Révision par le Gameplay :** Proposer des expériences où la révision est une mécanique de gameplay du jeu. Le succès du joueur dépend de sa connaissance : une bonne réponse génère des bonus immédiats, tandis qu'une erreur entraîne des malus, ancrant ainsi la mémorisation par l'enjeu ludique.

**Modèle Économique & Diffusion :** DopaLearn est conçu comme une application SaaS (Web-App) avec une dimension **Open Source**. Le business model repose sur :

1. **B2C :** Des abonnements premium pour les particuliers.
2. **B2B :** Des solutions de formation personnalisées pour les entreprises afin d'optimiser la montée en compétences interne.

**Le concept clé :** Une plateforme "Tout-en-un" où l'utilisateur construit sa base de connaissances par l'interaction pour la transformer instantanément en un flux de stimuli addictifs (jeux, scroll, audio).

## 2. Objectifs du Projet

### 2.1. Objectifs Stratégiques (Business & Produit)

1. **Réduire la friction cognitive (Entrée & Sortie) :** Faciliter la construction/révision du cours via l'IA pendant l'utilisation pour éviter la phase pénible de préparation.
2. **Modularité et Open Source :** Créer une "brique commune" (noyau) open source permettant à la communauté de développer et de brancher de nouvelles expériences de jeu.
3. **Souveraineté des données :** À terme, disposer de modèles d'IA spécialisés pour diminuer leur taille et leur coût, tout en garantissant la confidentialité des données.

### 2.2. Objectifs Opérationnels (SMART)

- **S (Spécifique) :** Livrer un MVP comprenant l'interface d'interaction pour la construction de cours, le noyau central (Serveur MCP) et au moins deux modes d'apprentissage (histoire interactive et Gaming avec système de bonus/malus).
- **M (Mesurable) :** Valider le modèle B2B par un premier prototype de "parcours de formation en entreprise".
- **A (Atteignable) :** S'appuyer sur des modèles LLM open-source ou européen existants ou des APIs standards comme mistral pour valider la preuve de concept sans nécessiter de R&D lourde sur l'optimisation des modèles en phase 1.
- **R (Pertinent) :** Valider l'attractivité d'une WebApp capable de rivaliser avec les réseaux sociaux sur le temps de cerveau disponible, tout en assurant une architecture compatible avec un futur portage en application mobile pour profiter des avancées technologiques sur les LLM qui peuvent tourner en local et leur performance (les architecture hardware A.R.M).
- **T (Temporel) :** Lancer la première itération publique fonctionnelle (v0.1) incluant le noyau et le système de récompenses pour octobre 2026.

## 3. Cibles et Valeur Ajoutée

### 3.1. Public Cible (Personas)

- **L'Étudiant :** Il possède la matière première (ses cours) mais subit une trop grande résistance psychologique pour s'y plonger après une journée chargée. Il est la victime principale du "piège du scroll" (TikTok, Instagram) : même avec une intention initiale de réviser, la surcharge en dopamine générée par les réseaux sociaux court-circuite sa volonté, rendant l'effort d'étude insurmontable. Il cherche à détourner ce réflexe pour rentabiliser ses micro-pauses sans augmenter sa fatigue mentale.
- **Le Professionnel en Auto-formation :** Il doit maintenir ses compétences à jour dans un environnement mouvant. Il a besoin d'un outil qui s'intègre à son flux de travail quotidien sans imposer de sessions de révision lourdes et formelles.
- **Le Profil Hyperactif ("Dopamine Seeker") :** Il a une volonté sincère de progresser dans la vie, mais son besoin constant de stimulation le rend extrêmement vulnérable aux boucles addictives. Une fois captivé par le scroll infini, il n'arrive plus à s'en détacher, ce qui génère une frustration profonde. Il cherche désespérément une alternative capable de satisfaire son besoin de dopamine tout en servant ses ambitions de croissance personnelle.

### 3.2. Proposition de Valeur Unique (UVP)

> "DopaLearn : Votre temps est précieux, ne le laissez plus être une marchandise pour les algorithmes. Là où les réseaux sociaux agissent comme une drogue numérique pour vous saturer de vide et de publicités, DopaLearn transforme vos moments de repos en micro-activités constructives. L'algorithme est à votre services Pas l'inverse.

## 4. Indicateurs de Succès (KPIs)

- **Indice de Rétention Comparative :** Capacité de l'application à maintenir un taux d'utilisation quotidien (DAU/MAU) se rapprochant des standards des réseaux sociaux (TikTok/Instagram) sur les segments de temps ciblés.
- **Taux de complétion des cours :** Pourcentage de connaissances maîtrisées suite aux interactions ludiques.
- **Engagement B2B :** Nombre d'entreprises adoptant la solution pour leurs formations internes.
- **Activité Open Source :** Nombre de contributeurs et de plugins tiers développés sur la brique commune.
