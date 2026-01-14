## 🔧 GLOBAL TAILWIND CONFIGURATION STRATEGY

*Instruction to AI:* Before generating components, define these values in `tailwind.config.js` based on the project's "Vibe".

* **Colors:** Define `primary`, `secondary`, `accent`, `neutral`, `base-100` (surface), `info`, `success`, `warning`, `error`.
* **Border Radius:** Define generic `rounded-btn`, `rounded-box` (cards), `rounded-badge`.
* **Typography:** Define a `font-sans` (UI) and `font-display` (Headings) if needed.
* **Animation:** Define `keyframes` for skeletons and loaders in `extend`.

C'est la brique manquante essentielle. En Design System, on appelle cela les **"Foundations"** ou les **"Design Tokens"**.

Sans cela, l'IA va improviser des couleurs et des tailles de texte à chaque génération, et ton site ressemblera à un patchwork. Il faut définir des règles strictes.

Voici le bloc **"0. FOUNDATIONS"** à placer tout au début de ton fichier `MASTER_UI_SPECS.md`. Il dicte à l'IA comment configurer le fichier `tailwind.config.js`.

---

# 0. DESIGN TOKENS (FOUNDATIONS)

**Context:** These definitions must populate the `@theme` section of `<style type="text/tailwindcss">`.

## A. COLORS (SEMANTIC PALETTE)

*Instruction to AI:* Do not use hardcoded hex values in components (e.g., `bg-[#ff0000]`). Always use semantic names mapped in the config.

| Token Name | Usage | Tailwind Map |
| --- | --- | --- |
| **Primary** | Main Brand Action (Buttons, Links, Active States). | `--color-primary` |
| **Secondary** | Complementary elements, less prominent actions. | `--color-secondary` |
| **Accent** | Highlights, badges, visual pops (often distinct/bright). | `--color-accent` |
| **Neutral** | Text, gray backgrounds, borders. (Dark & Light shades). | `--color-neutral` |
| **Base (Surface)** | Backgrounds of pages and cards (White, Off-white, Dark). | `--color-base-100` (Page), `--color-base-200` (Secondary bg), `--color-base-300` (Borders). |
| **Feedback** | Status messages. | `--color-info`, `--color-success`, `--color-warning`, `--color-error`. |

**🎨 Special Rule for Text Contrast:**
For every color X, define an `on-X` (or `X-content`) color for text readability.

* *Example:* If `primary` is Dark Blue, `primary-content` must be White.

## B. TYPOGRAPHY (SCALE & HIERARCHY)

*Instruction to AI:* Use a 2-font stack maximum.

| Token Name | Usage | Tailwind Map |
| --- | --- | --- |
| **Font Display** | Headings (H1-H3), Hero Titles. Impactful. | `--font-display` (e.g., Montserrat, Oswald). |
| **Font Body** | Paragraphs, UI Labels, Inputs. Readable. | `--font-sans` (e.g., Inter, Roboto). |
| **Font Mono** | **CRITICAL:** Timer, Results, Data Tables, Codes. | `--font-mono` (e.g., Fira Code, JetBrains Mono). |

**📏 Typescale Strategy:**

* **H1 (Page Title):** `text-4xl md:text-5xl font-bold`
* **H2 (Section Title):** `text-3xl font-bold`
* **H3 (Card Title):** `text-xl font-semibold`
* **Body:** `text-base` (16px) standard, `text-sm` for UI density.
* **Caption/Label:** `text-xs uppercase tracking-wide`.

**⚠️ Numeric Constraint:**
For sports results (Times, Rankings), ALWAYS apply `font-variant-numeric: tabular-nums` (Tailwind class: `tabular-nums`) to ensure numbers align vertically.

## C. SPACING & RADIUS (THE "VIBE")

*Instruction to AI:* Adjust these global values based on the requested "Mood".

**1. Border Radius (`rounded-*`)**

* **Playful/Friendly:** `rounded-box: 1rem` (16px), `rounded-btn: 9999px` (Pill).
* **Serious/Data:** `rounded-box: 0.25rem` (4px), `rounded-btn: 0.25rem`.
* **Brutalist:** `rounded-none` (0px).

**2. Shadow Depth (`shadow-*`)**

* **Flat Design:** No shadows, utilize borders (`border-2`).
* **Material/Corporate:** Soft shadows (`shadow-md`, `shadow-lg`).

**3. Section Spacing (`.section`)**

* **Compact:** `py-12` (48px) - For heavy data apps.
* **Comfortable:** `py-24` (96px) - For marketing/landing pages.

---

## 1. COMPONENT: BUTTON

**Class:** `.btn`
**Tailwind Logic:** Use `@apply` to compose base utilities. Use CSS Variables for dynamic colors to allow easy theming.

### 🏛 HTML Structure

```html
<button class="btn btn-primary" data-size="md" data-state="idle">
  <span class="loading loading-spinner hidden group-data-[state=loading]:inline-block"></span>
  <svg class="w-5 h-5" ...></svg>
  <span>Button Label</span>
</button>

```

### 🎨 Tailwind Implementation Guide

* **Base:** `inline-flex items-center justify-center gap-2 transition-all duration-200 cursor-pointer border-none outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none`.
* **Variants (Hierarchy):**
* `.btn-primary`: `@apply bg-primary text-primary-content hover:bg-primary/90`.
* `.btn-ghost`: `@apply bg-transparent hover:bg-base-200 text-current`.
* `.btn-outline`: `@apply border-2 border-current bg-transparent hover:bg-current hover:text-base-100`.


* **Sizes:** Map to `h-*`, `px-*`, and `text-*`.
* `sm`: `h-8 px-3 text-xs`
* `md`: `h-10 px-4 text-sm`
* `lg`: `h-12 px-6 text-base`



---

## 2. COMPONENT: TEXT INPUT

**Class:** `.input`
**Tailwind Logic:** Use `ring` utilities for focus states to avoid layout shifts.

### 🏛 HTML Structure

```html
<div class="form-control w-full">
  <label class="label">
    <span class="label-text">Email</span>
  </label>
  <div class="relative">
    <input type="text" placeholder="Type here" class="input input-bordered w-full" />
    <span class="absolute inset-y-0 right-3 flex items-center text-base-content/50">...</span>
  </div>
  <label class="label">
    <span class="label-text-alt text-error">Error message</span>
  </label>
</div>

```

### 🎨 Tailwind Implementation Guide

* **Base:** `w-full rounded-btn bg-base-100 text-base-content placeholder:text-base-content/40 outline-none transition-all`.
* **Variants:**
* `.input-bordered`: `@apply border border-base-300 focus:border-primary focus:ring-1 focus:ring-primary`.
* `.input-ghost`: `@apply bg-base-200/50 focus:bg-base-100`.
* `.input-error`: `@apply border-error focus:ring-error text-error`.



---

## 3. COMPONENT: SELECTION (Toggle/Checkbox)

**Class:** `.toggle` / `.checkbox`
**Tailwind Logic:** Pure CSS styling using `appearance-none` and checking state.

### 🏛 HTML Structure

```html
<label class="cursor-pointer flex items-center gap-3">
  <input type="checkbox" class="toggle toggle-primary" checked />
  <span class="label-text">Activate Mode</span>
</label>

```

### 🎨 Tailwind Implementation Guide

* **Toggle Base:** `appearance-none h-6 w-12 rounded-full bg-base-300 transition-colors duration-200 relative after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all checked:bg-primary checked:after:translate-x-6`.
* **Checkbox Base:** `appearance-none h-5 w-5 rounded border border-base-300 bg-base-100 checked:bg-primary checked:border-primary focus:ring-2 focus:ring-primary/50 relative checked:after:content-['✓'] checked:after:text-white checked:after:flex checked:after:justify-center checked:after:items-center checked:after:text-xs`.

---

## 5. COMPONENT: CARD

**Class:** `.card`
**Tailwind Logic:** Flex container with distinct internal spacing.

### 🏛 HTML Structure

```html
<div class="card bg-base-100 shadow-xl image-full"> <figure><img src="..." alt="" /></figure>
  <div class="card-body">
    <h2 class="card-title">Title</h2>
    <p>Content</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>

```

### 🎨 Tailwind Implementation Guide

* **Base:** `overflow-hidden flex flex-col relative`.
* **Body:** `.card-body` -> `@apply p-6 flex flex-col gap-2`.
* **Variants:**
* `image-full`: Logic to overlay text on image using `before:absolute before:inset-0 before:bg-black/50` on the figure or container.
* `card-side`: `lg:flex-row` (switch from col to row on large screens).



---

## 7. COMPONENT: ACCORDION

**Class:** `.collapse`
**Tailwind Logic:** Use the `group` class on the container and `group-open:` modifiers. NO JS REQUIRED.

### 🏛 HTML Structure

```html
<details class="group collapse bg-base-200 rounded-box">
  <summary class="collapse-title flex justify-between items-center cursor-pointer list-none font-medium">
    Question?
    <span class="transition-transform group-open:rotate-180">▼</span>
  </summary>
  <div class="collapse-content transition-all duration-300 max-h-0 overflow-hidden group-open:max-h-screen group-open:p-4">
    <p>Answer content...</p>
  </div>
</details>

```

---

## 8. COMPONENT: NAVBAR

**Class:** `.navbar`
**Tailwind Logic:** Flexbox alignment is key.

### 🏛 HTML Structure

```html
<div class="navbar bg-base-100 shadow-sm">
  <div class="flex-1">
    <a class="btn btn-ghost text-xl">daisyUI</a>
  </div>
  <div class="flex-none">
    <ul class="menu menu-horizontal px-1">
      <li><a>Link</a></li>
      <li>
        <details>
          <summary>Parent</summary>
          <ul class="p-2 bg-base-100 absolute"> <li><a>Submenu 1</a></li>
          </ul>
        </details>
      </li>
    </ul>
  </div>
</div>

```

---

## 10. COMPONENT: DATA TABLE

**Class:** `.table`

### 🏛 HTML Structure

```html
<div class="overflow-x-auto">
  <table class="table w-full">
    <thead>
      <tr class="bg-base-200">
        <th>ID</th>
        <th>Name</th>
        <th>Result</th>
      </tr>
    </thead>
    <tbody>
      <tr class="hover:bg-base-200/50 transition-colors">
        <th>1</th>
        <td>Michael</td>
        <td><span class="badge badge-success">Qualified</span></td>
      </tr>
    </tbody>
  </table>
</div>

```

### 🎨 Tailwind Implementation Guide

* **Base:** `text-left text-sm w-full`.
* **Cells:** `td, th` -> `@apply px-4 py-3 align-middle`.
* **Striped:** `tbody tr:nth-child(even)` -> `@apply bg-base-200/30`.

---

## 12. COMPONENT: ALERT

**Class:** `.alert`
**Tailwind Logic:** Grid layout allows easy icon + text + button alignment.

### 🏛 HTML Structure

```html
<div role="alert" class="alert alert-info">
  <svg class="stroke-current shrink-0 w-6 h-6" ...></svg>
  <div>
    <h3 class="font-bold">New message!</h3>
    <div class="text-xs">You have 1 unread email</div>
  </div>
  <button class="btn btn-sm">See</button>
</div>

```

### 🎨 Tailwind Implementation Guide

* **Base:** `grid grid-flow-col justify-items-start text-start items-center gap-4 p-4 rounded-box w-full`.
* **Variants:** Map `alert-info` to `bg-info/10 text-info border-info/20`.
