## 🔧 UI Specifications

# ⚠️ HYBRID STRATEGY RULES (CRITICAL)

To ensure maintainability and consistency, you must follow this **Hybrid Strategy**:

1.  **COMPONENTS (Atoms/Molecules):** MUST be defined in CSS using `@layer components` and `@apply`.
2.  **CUSTOM UTILITIES (Layout Helpers):** Global helpers like `.section-container` or `.section` MUST be defined using `@utility` (Tailwind v4 syntax).
3.  **LAYOUT (Organisms/Pages):** MUST use utility classes directly in HTML for specific grid/flex structures.
4.  **NAMING:** Use BEM-like naming for component children (e.g., `.card`, `.card-body`, `.card-title`).

---

# 0. DESIGN TOKENS (FOUNDATIONS)

**Context:** These definitions must populate the `@theme` section of `<style type="text/tailwindcss">`.

## A. COLORS (SEMANTIC PALETTE)
*WCAG Note:* Ensure `content` colors provide at least 4.5:1 contrast ratio against their background.

| Token Name | Usage | Tailwind Map |
| --- | --- | --- |
| **Primary** | Main Brand Action (CTA, Active States). | `--color-primary` |
| **Secondary** | Complementary, less prominent. | `--color-secondary` |
| **Accent** | Highlights, badges. | `--color-accent` |
| **Neutral** | Text, gray backgrounds, borders. | `--color-neutral` |
| **Base (Surface)** | Backgrounds (Level 1, 2, 3). | `--color-base-100`, `--color-base-200`, `--color-base-300`. |
| **Feedback** | Status messages. | `--color-info`, `--color-success`, `--color-warning`, `--color-error`. |

## B. TYPOGRAPHY
*Instruction:* Use a 2-font stack max.
* **Headings:** `--font-display` (Impactful).
* **Body:** `--font-sans` (Readable, High x-height).
* **Mono:** `--font-mono` (Code, Data).

## C. SPACING & RADIUS
* **Radius:** `--radius-btn`, `--radius-box`.
* **Spacing:** Defines the white space rhythm.

---

# 1. ATOMS (PRIMITIVES)

## 1.1 COMPONENT: BUTTON
**Class:** `.btn`
**Tailwind Logic:** Base styles via `@apply`. Variants via CSS classes.

### 🏛 HTML Structure
```html
<button class="btn btn-primary">
  <svg class="w-5 h-5">...</svg>
  <span>Action</span>
</button>
```

### 🎨 Tailwind Implementation Guide
*   **Base (`.btn`):** `@apply inline-flex items-center justify-center gap-2 px-6 py-3 rounded-[var(--radius-btn)] font-medium transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 disabled:opacity-50 disabled:pointer-events-none cursor-pointer border-none;`
*   **Variants:**
    *   `.btn-primary`: `@apply bg-[var(--color-primary)] text-[var(--color-primary-content)] hover:brightness-110;`
    *   `.btn-secondary`: `@apply bg-[var(--color-secondary)] text-[var(--color-secondary-content)];`
    *   `.btn-outline`: `@apply border-2 border-current bg-transparent hover:bg-[var(--color-base-content)] hover:text-[var(--color-base-100)];`
    *   `.btn-ghost`: `@apply bg-transparent hover:bg-[var(--color-base-200)];`
*   **Sizes:**
    *   `.btn-sm`: `@apply px-3 py-1.5 text-sm;`
    *   `.btn-lg`: `@apply px-8 py-4 text-lg;`

## 1.2 COMPONENT: BADGE
**Class:** `.badge`

### 🏛 HTML Structure
```html
<span class="badge badge-accent">New</span>
```

### 🎨 Tailwind Implementation Guide
*   **Base (`.badge`):** `@apply inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold uppercase tracking-wide border;`
*   **Variants:**
    *   `.badge-accent`: `@apply border-transparent bg-[var(--color-accent)] text-[var(--color-accent-content)];`
    *   `.badge-outline`: `@apply border-current bg-transparent text-current;`

## 1.3 COMPONENT: AVATAR
**Class:** `.avatar`

### 🏛 HTML Structure
```html
<img src="..." alt="User" class="avatar avatar-md" />
```

### 🎨 Tailwind Implementation Guide
*   **Base (`.avatar`):** `@apply rounded-full object-cover bg-[var(--color-base-300)];`
*   **Sizes:**
    *   `.avatar-sm`: `@apply h-8 w-8;`
    *   `.avatar-md`: `@apply h-12 w-12;`
    *   `.avatar-lg`: `@apply h-20 w-20;`

---

# 2. MOLECULES (COMPOUNDS)

## 2.1 COMPONENT: CARD
**Class:** `.card`
**Tailwind Logic:** Flex container with distinct internal spacing.

### 🏛 HTML Structure
```html
<article class="card">
  <figure class="card-image">
    <img src="..." alt="..." />
  </figure>
  <div class="card-body">
    <h3 class="card-title">Title</h3>
    <p class="card-text">Description goes here.</p>
    <div class="card-actions">
        <button class="btn btn-primary">Go</button>
    </div>
  </div>
</article>
```

### 🎨 Tailwind Implementation Guide
*   **Base (`.card`):** `@apply bg-[var(--color-base-100)] border border-[var(--color-base-200)] rounded-[var(--radius-box)] overflow-hidden shadow-sm hover:shadow-md transition-shadow flex flex-col;`
*   **Image (`.card-image`):** `@apply aspect-video overflow-hidden relative;`
    *   *Child Img:* `@apply w-full h-full object-cover transition-transform duration-500 hover:scale-105;`
*   **Body (`.card-body`):** `@apply p-6 flex flex-col gap-4;`
*   **Title (`.card-title`):** `@apply font-display text-xl font-bold;`

## 2.2 COMPONENT: ALERT
**Class:** `.alert`
**Usage:** Feedback messages.

### 🏛 HTML Structure
```html
<div role="alert" class="alert alert-info">
  <svg>...</svg>
  <span>Update available.</span>
</div>
```

### 🎨 Tailwind Implementation Guide
*   **Base (`.alert`):** `@apply flex items-center gap-4 p-4 rounded-[var(--radius-box)] text-sm font-medium;`
*   **Variants:**
    *   `.alert-info`: `@apply bg-[var(--color-info)]/10 text-[var(--color-info)];`
    *   `.alert-success`: `@apply bg-[var(--color-success)]/10 text-[var(--color-success)];`
    *   `.alert-error`: `@apply bg-[var(--color-error)]/10 text-[var(--color-error)];`

## 2.3 COMPONENT: FORM INPUTS
**Class:** `.input`, `.textarea`, `.select`, `.checkbox`

### 🏛 HTML Structure
```html
<div class="form-control">
  <label class="label" for="email">Email</label>
  <input type="email" id="email" class="input" />
</div>
```

### 🎨 Tailwind Implementation Guide
*   **Shared Base:** `@apply w-full rounded-md border border-[var(--color-base-300)] bg-[var(--color-base-100)] text-sm placeholder:text-[var(--color-neutral)]/50 focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] focus:border-transparent transition-all;`
*   **Input (`.input`):** `@apply h-10 px-3 py-2;`
*   **Textarea (`.textarea`):** `@apply min-h-[100px] px-3 py-2;`
*   **Select (`.select`):** `@apply h-10 pl-3 pr-10 appearance-none bg-no-repeat bg-[center_right_1rem];` (Add arrow via inline SVG or global background).
*   **Checkbox (`.checkbox`):** `@apply h-5 w-5 rounded border-2 border-[var(--color-neutral)] text-[var(--color-primary)] focus:ring-[var(--color-primary)];`
*   **Label (`.label`):** `@apply block text-sm font-medium mb-1.5;`

## 2.4 COMPONENT: ACCORDION
**Class:** `.accordion-item`

### 🏛 HTML Structure
```html
<details class="accordion-item group">
  <summary class="accordion-trigger">
    Question?
    <span class="icon group-open:rotate-180">▼</span>
  </summary>
  <div class="accordion-content">Answer.</div>
</details>
```

### 🎨 Tailwind Implementation Guide
*   **Item (`.accordion-item`):** `@apply border-b border-[var(--color-base-200)];`
*   **Trigger (`.accordion-trigger`):** `@apply flex w-full cursor-pointer list-none items-center justify-between py-4 font-medium transition-colors hover:text-[var(--color-primary)];`
*   **Content (`.accordion-content`):** `@apply pb-4 text-[var(--color-neutral)]/80;`

---

# 3. ORGANISMS (SECTIONS)

For Organisms, prioritize **semantic layout**. You may use internal Layout Utilities (`@utility section-container`, `@utility section`) defined here.

## 3.1 LAYOUT UTILITIES
**CRITICAL (Tailwind v4):** These must be defined using the `@utility` directive so they can be discovered by `@apply`.
*   `@utility section`: { @apply py-20 md:py-32; }
*   `@utility section-container`: { @apply w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8; }

## 3.2 COMPONENT: NAVBAR
**Class:** `.navbar`

### 🏛 HTML Structure
```html
<header class="navbar">
  <div class="section-container navbar-inner">
    <a href="/" class="brand">Logo</a>
    <nav class="nav-desktop">...</nav>
    <button class="md:hidden">Burger</button>
  </div>
</header>
```

### 🎨 Tailwind Implementation Guide
*   **Base (`.navbar`):** `@apply sticky top-0 z-50 w-full border-b border-[var(--color-base-200)] bg-[var(--color-base-100)]/90 backdrop-blur supports-[backdrop-filter]:bg-[var(--color-base-100)]/60;`
*   **Inner (`.navbar-inner`):** `@apply flex h-16 items-center justify-between;`
*   **Brand (`.brand`):** `@apply text-xl font-bold font-display tracking-tight hover:opacity-80;`
*   **Nav Desktop (`.nav-desktop`):** `@apply hidden md:flex items-center gap-8 text-sm font-medium;`

## 3.3 COMPONENT: HERO
**Class:** `.hero`

### 🏛 HTML Structure
```html
<section class="hero">
  <div class="hero-content">
    <div class="hero-text">
        <h1 class="hero-title">Values</h1>
        <p class="hero-desc">Subtitle.</p>
        <div class="flex gap-4">...CTAs...</div>
    </div>
    <div class="hero-visual">...Img...</div>
  </div>
</section>
```

### 🎨 Tailwind Implementation Guide
*   **Base (`.hero`):** `@apply section relative overflow-hidden bg-[var(--color-base-100)];`
*   **Content (`.hero-content`):** `@apply grid md:grid-cols-2 gap-12 items-center;`
*   **Title (`.hero-title`):** `@apply text-4xl md:text-6xl font-bold font-display tracking-tight text-[var(--color-base-content)];`
*   **Desc (`.hero-desc`):** `@apply mt-6 text-lg text-[var(--color-neutral)] opacity-90 max-w-lg leading-relaxed;`

## 3.4 COMPONENT: FOOTER
**Class:** `.footer`

### 🏛 HTML Structure
```html
<footer class="footer">
  <div class="footer-content">
     <!-- Grid Columns defined in HTML via utilities: grid-cols-2 md:grid-cols-4 -->
  </div>
</footer>
```

### 🎨 Tailwind Implementation Guide
*   **Base (`.footer`):** `@apply bg-[var(--color-base-200)] text-[var(--color-base-content)] py-12 border-t border-[var(--color-base-300)];`
*   **Content (`.footer-content`):** `@apply section-container grid grid-cols-2 md:grid-cols-4 gap-10;`
*   **Title (`.footer-title`):** `@apply font-bold text-xs uppercase tracking-wider opacity-60 mb-4 block;`
*   **Link (`.footer-link`):** `@apply block text-sm hover:underline hover:text-[var(--color-primary)] py-1 opacity-80 hover:opacity-100 transition-opacity;`

## 3.5 COMPONENT: LIST LAYOUT
**Class:** `.list-group`

### 🏛 HTML Structure
```html
<div class="list-group">
  <div class="list-item">...</div>
</div>
```

### 🎨 Tailwind Implementation Guide
*   **Group (`.list-group`):** `@apply flex flex-col divide-y divide-[var(--color-base-200)] border border-[var(--color-base-200)] rounded-[var(--radius-box)] overflow-hidden;`
*   **Item (`.list-item`):** `@apply p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-[var(--color-base-100)] hover:bg-[var(--color-base-200)]/50 transition-colors;`
