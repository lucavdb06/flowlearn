# Charte Graphique — FlowLearn

> **FlowLearn** : Apprendre en jouant, retenir en s'amusant.
> Une plateforme EdTech qui utilise la gamification et l'IA pour un apprentissage personnalisé et engageant.

---

## 1. Concept & Philosophie

Le design de FlowLearn s'articule autour de deux métaphores :

| Métaphore | Symbolique | Couleur |
|-----------|-----------|---------|
| **Le cerveau** | Intelligence, apprentissage, dopamine, neurosciences | Rose / Magenta |
| **La rivière (flow)** | Fluidité, progression, état de flow, mouvement | Bleu / Cyan |

Le mariage de ces deux univers traduit l'idée centrale du projet : **un apprentissage fluide, stimulant et personnalisé**.

---

## 2. Palette de couleurs

### Couleurs principales

| Nom | Hex | RGB | Usage |
|-----|-----|-----|-------|
| **Flow Blue** | `#3B82F6` | 59, 130, 246 | Couleur primaire, CTA, liens, éléments interactifs |
| **Brain Pink** | `#EC4899` | 236, 72, 153 | Couleur secondaire, accents, gamification, récompenses |

### Couleurs complémentaires

| Nom | Hex | RGB | Usage |
|-----|-----|-----|-------|
| **Deep Ocean** | `#1E3A5F` | 30, 58, 95 | Titres, texte principal sur fond clair |
| **Soft Lavender** | `#8B5CF6` | 139, 92, 246 | Dégradés, éléments IA / intelligence |
| **Success Green** | `#10B981` | 16, 185, 129 | Validations, succès, progression |
| **Warning Amber** | `#F59E0B` | 245, 158, 11 | Alertes, badges, notifications |

### Neutres

| Nom | Hex | Usage |
|-----|-----|-------|
| **Slate 900** | `#0F172A` | Fond dark mode |
| **Slate 800** | `#1E293B` | Cards dark mode |
| **Slate 100** | `#F1F5F9` | Fond light mode |
| **White** | `#FFFFFF` | Cards light mode, surfaces |

### Dégradés signature

```css
/* Dégradé principal — utilisé pour le hero, les boutons premium */
background: linear-gradient(135deg, #3B82F6 0%, #EC4899 100%);

/* Dégradé IA — utilisé pour les éléments liés à l'intelligence artificielle */
background: linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%);

/* Dégradé cerveau — utilisé pour la gamification */
background: linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%);
```

---

## 3. Typographie

| Rôle | Police | Poids | Taille |
|------|--------|-------|--------|
| **Titres (H1-H2)** | **Inter** (ou Poppins) | Bold (700) | 32–48px |
| **Sous-titres (H3-H4)** | **Inter** | Semi-Bold (600) | 20–24px |
| **Corps de texte** | **Inter** | Regular (400) | 16px |
| **Petits textes / labels** | **Inter** | Medium (500) | 12–14px |
| **Code / technique** | **JetBrains Mono** | Regular (400) | 14px |

> **Inter** est une police sans-serif moderne, très lisible sur écran, gratuite et disponible sur Google Fonts.

### Hiérarchie typographique

```
H1 — 48px / Bold / Deep Ocean          → Titres de pages
H2 — 32px / Bold / Deep Ocean          → Sections principales
H3 — 24px / Semi-Bold / Slate 700      → Sous-sections
H4 — 20px / Semi-Bold / Slate 600      → Titres de cards
Body — 16px / Regular / Slate 600      → Texte courant
Small — 14px / Regular / Slate 500     → Labels, métadonnées
Caption — 12px / Medium / Slate 400    → Annotations, hints
```

---

## 4. Logo

### Concept

Le logo FlowLearn fusionne :
- **Un cerveau** stylisé (hémisphère, connexions neuronales)
- **Une rivière / vague** qui traverse ou entoure le cerveau (mouvement, flow)

### Déclinaisons

| Version | Usage |
|---------|-------|
| Logo complet (icône + texte) | Header, landing page, documents |
| Icône seule | Favicon, app mobile, avatar |
| Monochrome blanc | Fond sombre, overlays |
| Monochrome sombre | Fond clair, impressions |

### Zones d'exclusion

Laisser un espace minimum égal à la hauteur du "F" de FlowLearn autour du logo.

### Tailles minimales

- **Print** : 25mm de largeur minimum
- **Digital** : 80px de largeur minimum
- **Favicon** : 32x32px (version simplifiée)

---

## 5. Iconographie & Illustrations

### Style des icônes

- **Type** : Outline (trait) avec coins arrondis
- **Épaisseur du trait** : 1.5px – 2px
- **Taille de référence** : 24x24px
- **Bibliothèque recommandée** : [Lucide Icons](https://lucide.dev) ou [Phosphor Icons](https://phosphoricons.com)

### Style des illustrations

- Illustrations flat / semi-flat avec des dégradés doux
- Personnages simples et inclusifs
- Palette limitée aux couleurs de la charte

---

## 6. Composants UI

### Boutons

| Type | Style |
|------|-------|
| **Primaire** | Fond Flow Blue `#3B82F6`, texte blanc, border-radius 12px |
| **Secondaire** | Fond transparent, bordure Flow Blue, texte Flow Blue |
| **Accent** | Dégradé Blue → Pink, texte blanc |
| **Danger** | Fond `#EF4444`, texte blanc |

### Cards

- **Border-radius** : 16px
- **Shadow** : `0 4px 6px -1px rgba(0, 0, 0, 0.1)`
- **Padding** : 24px
- **Hover** : légère élévation (`translateY(-2px)`) + ombre renforcée

### Espacements (base 4px)

| Token | Valeur |
|-------|--------|
| `xs` | 4px |
| `sm` | 8px |
| `md` | 16px |
| `lg` | 24px |
| `xl` | 32px |
| `2xl` | 48px |
| `3xl` | 64px |

### Border-radius

| Usage | Valeur |
|-------|--------|
| Boutons | 12px |
| Cards | 16px |
| Inputs | 8px |
| Avatars | 50% (rond) |
| Tags / Badges | 9999px (pill) |

---

## 7. Règles d'utilisation

### A faire

- Utiliser les couleurs exactes définies dans la palette
- Respecter la hiérarchie typographique
- Maintenir un contraste suffisant (WCAG AA minimum)
- Utiliser les dégradés uniquement sur les éléments prévus

### A ne pas faire

- Déformer ou pivoter le logo
- Utiliser des couleurs hors palette sans validation
- Mélanger plus de 3 couleurs sur un même écran
- Utiliser des ombres portées trop prononcées

---

## 8. Figma

### Organisation du projet Figma

```
FlowLearn Design System/
├── 🎨 Foundations/
│   ├── Colors (palette + tokens)
│   ├── Typography (styles de texte)
│   ├── Spacing & Grid
│   └── Shadows & Effects
├── 🧩 Components/
│   ├── Buttons
│   ├── Inputs & Forms
│   ├── Cards
│   ├── Navigation
│   ├── Modals & Overlays
│   └── Badges & Tags
├── 📱 Screens/
│   ├── Landing Page
│   ├── Dashboard
│   ├── Quiz / Jeu
│   ├── Profil utilisateur
│   └── Admin
└── 🖼️ Assets/
    ├── Logo (toutes déclinaisons)
    ├── Icons
    └── Illustrations
```

### Lien Figma

> *A compléter une fois le projet Figma créé*
> `https://www.figma.com/file/...`

---

## 9. Accessibilité

- Ratio de contraste minimum **4.5:1** pour le texte courant (WCAG AA)
- Ratio de contraste minimum **3:1** pour les grands textes et éléments UI
- Tous les éléments interactifs doivent avoir un état `:focus` visible
- Les couleurs ne doivent jamais être le seul moyen de transmettre une information

---

*Document maintenu par l'équipe FlowLearn — Branche `charte-graphique`*
