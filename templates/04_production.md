# Rôle
Agis en tant qu'expert UI/UX et Développeur Front-end Senior.

# Continuité du Design
⚠️ **IMPORTANT :**
1.  **Réutilise** strictement les classes de composants établies à l'étape précédente dans le "Kitchen Sink" @kitchen-sink.html pour les éléments de base (ex: utilise la classe `.btn-primary`, ne recrée pas un bouton avec `bg-blue-500 rounded...`).
2.  **Utilise** les utilitaires Tailwind pour tout ce qui concerne la mise en page de CETTE page spécifique (Grilles, Marges, Flexbox, largeurs).
3. Ne change pas la Direction Artistique.

# Contexte de la Page
Je conçois la page : {{ page_context.name }}
Objectif : {{ page_context.objective }}
Cible : {{ page_context.target }}

# Structure Requise
La page doit contenir :
{{ page_context.structure }}

# Contraintes Techniques
- Framework Backend : [CHOISIR : Laravel Blade OU Statamic Antlers]
- CSS : Tailwind CSS (classes utilitaires + classes composants existantes)
- JS : Alpine.js
- Responsivité : Mobile-first.

# Format de Sortie
Fournis le code HTML (Blade/Antlers) dans un fichier `.html` que tu créé.
Si tu dois ajouter du CSS spécifique (rare), utilise une balise `<style>` temporaire ou indique les classes utilitaires.
