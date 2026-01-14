# Conception Web UI assistée par IA

Ce document détaille la procédure standard pour générer le code Front-end des projets.

**Pré-requis :**

* Avoir le fichier `MASTER_UI_SPECS.md` à portée de main (tes specs HTML/CSS de base).
* Avoir défini le "Mood" du projet client.

---

## ÉTAPE 1 : L'Initialisation (Context Loading)

*Objectif : Charger les contraintes techniques strictes dans la mémoire de l'IA.*

**Action :** Copier-coller le prompt suivant en y joignant le contenu de ton fichier `MASTER_UI_SPECS.md`.

```markdown
Voici le fichier MASTER_UI_SPECS.md. C'est ta référence absolue pour la structure HTML et les noms de classes. Analyse-le et attends mon instruction suivante. Ne génère rien pour l'instant.

[COLLER LE CONTENU DE MASTER_UI_SPECS.MD ICI]

```

---

## ÉTAPE 2 : La Direction Artistique (The Kitchen Sink)

*Objectif : Créer le "Look & Feel", définir les tokens (couleurs, typos) et valider l'ambiance avec une page démo.*

**Action :** Copier-coller le prompt suivant. Remplis la section "DIRECTION ARTISTIQUE" avec les infos du client.

```markdown
Agis en tant que **Lead UI Designer & Front-End Architect**.

**OBJECTIF :**
Générer une "Kitchen Sink" (page de démonstration UI complète) en Tailwind CSS v4 + Alpine.js basée sur le fichier `MASTER_UI_SPECS.md` analysé précédemment, adaptée à la Direction Artistique ci-dessous.

**STRATÉGIE CSS (HYBRIDE) :**
1.  **Pour les Composants (Base) :** Utilise les classes définies dans `MASTER_UI_SPECS.md` (ex: `.btn`, `.input`, `.badge`). Définis-les dans le bloc CSS via `@layer components` et `@apply`.
2.  **Pour le Layout & Context (Custom) :** Utilise des **classes utilitaires Tailwind pures** directement dans le HTML pour gérer les grilles, le spacing (margin/padding), le positionnement et les largeurs spécifiques (ex: `grid-cols-3 gap-6 mt-10`).

**DIRECTIVES DE DESIGN (VIBE) :**
* Utilise la syntaxe CSS native de Tailwind v4 pour le thème.
* Traduis le "Mood" ci-dessous en variables CSS (`--color-primary`, `--font-sans`, etc.) à l'intérieur de la directive `@theme`.

**DIRECTIVES DE "REMIX" :**
1. **Design System (Tokens) :** Traduis les mots-clés émotionnels en variables CSS (Couleurs, Radius, Font-family) pour la config Tailwind v4.
2. **Liberté Structurelle :**
   - Respecte strictement la structure HTML interne des ATOMES (`.btn`, `.input`).
   - Sois CRÉATIF sur les COMPOSANTS COMPLEXES (Cartes, Heros). Utilise Flex/Grid/Z-index pour créer des layouts uniques qui collent au "Vibe".
3. **Interactivité :** Utilise **Alpine.js** (x-data, @click) pour toute interaction. Mobile-First obligatoire.

**FORMAT DE SORTIE :**
Un seul fichier HTML complet `kitchen-sink.html` contenant :
1. Script CDN Tailwind v4 : `<script src="https://unpkg.com/@tailwindcss/browser@4"></script>`
2.  `<style type="text/tailwindcss">`
    * `@theme { ... }` : Tes variables de couleurs/fonts.
    * `@layer components { ... }` : Tes classes `.btn`, `.card` basées sur `@apply`.
3. Script CDN Alpine.js : `<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3/dist/cdn.min.js"></script>`
4. `<body>` avec les sections : Typography, Buttons, Forms, Cards, Complex Patterns.

---

**DIRECTION ARTISTIQUE (MOOD) :**
PROJET : [Nom du Projet]
AMBIANCE : [ex: Corporate, Ludique, Luxe, Dark Mode, …]
COULEURS : [ex: Dominante Bleu Nuit, #ff0000, Accent Jaune Fluo, …]
FORMES : [ex: Arrondis généreux ou Angles vifs...]
TYPOGRAPHIE : [ex: Serif élégant pour les titres, Sans-serif clean pour le texte...]

```

*Une fois le résultat généré : Copie le code dans un fichier `kitchen-sink.html`, ouvre-le dans le navigateur et valide le design.*

---

## ÉTAPE 3 : La Production des Pages (Page Builder)

*Objectif : Générer le code spécifique d'une page (ex: Accueil, Contact) en réutilisant le design validé.*

**Action :** Utilise ce prompt pour chaque nouvelle page à créer.

```markdown
# Rôle
Agis en tant qu'expert UI/UX et Développeur Front-end Senior.

# Continuité du Design
⚠️ **IMPORTANT :**
1.  **Réutilise** strictement les classes de composants établies à l'étape précédente dans le "Kitchen Sink" @kitchen-sink.html pour les éléments de base (ex: utilise la classe `.btn-primary`, ne recrée pas un bouton avec `bg-blue-500 rounded...`).
2.  **Utilise** les utilitaires Tailwind pour tout ce qui concerne la mise en page de CETTE page spécifique (Grilles, Marges, Flexbox, largeurs).
3. Ne change pas la Direction Artistique.

# Contexte de la Page
Je conçois la page : [Page "A propos", Landing page, Page de contact, Dashboard]
Objectif : [ex: Présenter les 3 fonctionnalités clés, Convertir les visiteurs en clients, Présenter le projet]
Cible : [ex: Clients, prospects, grand public]

# Structure Requise
La page doit contenir :
1. [ex: Header]
2. [ex: Titre avec carte interactive en fond]
3. [ex: Liste des fonctionnalités (Cards)]
4. [ex: Footer]

# Contraintes Techniques
- Framework Backend : [CHOISIR : Laravel Blade OU Statamic Antlers]
- CSS : Tailwind CSS (classes utilitaires + classes composants existantes)
- JS : Alpine.js
- Responsivité : Mobile-first.

# Format de Sortie
Fournis le code HTML (Blade/Antlers) dans un fichier `.html` que tu créé.
Si tu dois ajouter du CSS spécifique (rare), utilise une balise `<style>` temporaire ou indique les classes utilitaires.

```
