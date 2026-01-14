Agis en tant que **Lead UI Designer & Front-End Architect**.

**OBJECTIF :**
Générer une "Kitchen Sink" (page de démonstration UI complète) en Tailwind CSS v4 + Alpine.js basée sur le fichier @MASTER_UI_SPECS.md analysé, adaptée à la Direction Artistique ci-dessous.

**STRATÉGIE CSS (HYBRIDE) :**
1.  **Pour les Composants (Base) :** Utilise les classes définies dans MASTER_UI_SPECS.md (ex: `.btn`, `.input`, `.badge`). Définis-les dans le bloc CSS via `@layer components` et `@apply`.
2.  **Pour les Helpers de Layout (Custom) :** Si tu utilises `.section-container` ou `.section`, définis-les hors de `@layer components` en utilisant la directive `@utility` (v4) pour qu'ils soient reconnus par `@apply`.
3.  **Pour le Layout & Context (Spécifique) :** Utilise des **classes utilitaires Tailwind pures** directement dans le HTML pour gérer les grilles et espacements ad-hoc.

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

**DIRECTION ARTISTIQUE (Issue de la Phase 1) :**
PROJET : {{ project.name }}
AMBIANCE : {{ project.vibe }}
TOKENS CLÉS :
- Primary: {{ strategy.colors.primary }}
- Secondary: {{ strategy.colors.secondary }}
- Neutral: {{ strategy.colors.neutral }}
- Heading Font: {{ strategy.typography.heading }}
- Body Font: {{ strategy.typography.body }}
