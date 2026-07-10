# Shared Benchmark Prompt: Signal / Matter

Build a polished, motion-led one-page homepage for a fictional independent spatial-audio label and installation studio named **SIGNAL / MATTER**.

The creative proposition is: **Sound is not background. It is architecture.** The page should feel like an award-caliber creative technology portfolio: editorial, experimental, precise, and immersive, while remaining legible and usable. It may draw on general patterns found in contemporary motion galleries and creative-developer portfolios, but it must be an original design with original copy and no copied brand assets or exact layouts.

## Deliverables and Constraints

- Create exactly three files: `index.html`, `styles.css`, and `script.js`.
- Use semantic HTML, modern CSS, and vanilla JavaScript only.
- Use no external packages, fonts, images, videos, APIs, or network requests.
- Create the primary visual as an original procedural canvas or DOM/CSS composition.
- The page must work from a local static server and remain meaningful if JavaScript fails.
- Do not add fake testimonials, customer logos, awards, usage statistics, or business metrics.

## First Viewport

- Make `SIGNAL / MATTER` an unmistakable first-viewport signal, not a tiny navigation label.
- Include the statement `Sound is not background. It is architecture.` and a concise supporting line.
- Show a procedural visual field that suggests wave interference, spatial coordinates, or an instrument panel without looking like a generic neon waveform.
- Include a clear `Explore the index` action and a secondary `Play the field` or motion-control action.
- Leave a visible hint of the next section on desktop and mobile.

## Page Structure

1. A restrained navigation with the wordmark, `Index`, `Method`, and `Contact`, plus a compact motion toggle.
2. The immersive hero described above.
3. A selected-work index with four original projects: `Tidal Memory`, `Room Tone 04`, `Afterimage Choir`, and `Fault Line FM`. Each item needs a year, discipline, one-sentence description, and a distinct visual or interaction state.
4. A sticky or staged method section built around three verbs: `Listen`, `Map`, `Materialize`.
5. A concise studio statement and a final contact call to action.
6. A real footer with location text, availability status, and copyright language appropriate to a fictional studio.

## Motion and Interaction

- Add a deliberate entrance sequence for the wordmark, headline, metadata, and visual field.
- Make the hero visual react subtly to pointer position and scroll without compromising readability.
- Add scroll progress or section-state feedback.
- Give work-index rows purposeful hover/focus states and a visual response, not simple opacity changes.
- Add a mobile navigation toggle with correct `aria-expanded` state and Escape-key closing.
- Add a working motion toggle that pauses nonessential animation and exposes its state accessibly.
- Respect `prefers-reduced-motion`; reduced-motion mode must keep the composition strong without animated entrances or continuous movement.
- Avoid janky layout animation: prefer transforms, opacity, and canvas drawing.

## Visual Direction

- Use a multi-tone palette built from carbon black, warm mineral white, signal coral, and one cool metallic accent. Avoid purple-blue gradients, beige luxury styling, glassmorphism, glowing orbs, and generic SaaS cards.
- Use system fonts with an editorial contrast between a precise sans-serif voice and a restrained serif accent.
- Use grid lines, calibrated labels, coordinates, or technical notation sparingly to support the spatial-audio concept.
- Keep radii at 8px or less and do not place cards inside cards.
- Prioritize asymmetric composition, strong type hierarchy, generous but controlled spacing, and professional mobile typography.

## Accessibility and Quality

- Include a skip link, logical headings, landmarks, visible focus styles, accessible button names, and live status text where state changes.
- Ensure text contrast remains strong and controls have stable hit areas.
- Prevent horizontal overflow and text clipping at 1440px, 1280px, 900px, and 390px widths.
- Run JavaScript syntax and local structure checks. If browser tooling is available, inspect desktop and mobile, test navigation and motion controls, check console/network errors, and report limitations honestly.

Return a short completion summary only after the three files are finished and checked.
