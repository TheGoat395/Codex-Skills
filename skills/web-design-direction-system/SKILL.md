---
name: web-design-direction-system
description: Use for premium frontend, website, app UI, landing page, dashboard, redesign, image-to-code, or visual-polish work that needs clearer design intent, adjustable visual direction, motion discipline, less generic output, and a final preflight check before handoff.
---

# Web Design Direction System

Use this as the high-level router before detailed build, redesign, or polish work.

## Infer The Design Mode

Before choosing components or CSS, write a compact design read:

- product type: marketing site, product UI, dashboard, portfolio, service business, commerce, docs, app shell, or campaign
- user state: browsing, evaluating, comparing, buying, onboarding, operating, recovering, or managing
- brand posture: quiet, precise, editorial, luxurious, playful, industrial, technical, cinematic, utilitarian, or warm
- density need: sparse, normal, dense, or expert-dense
- motion need: none, small tactile, section choreography, scroll scene, spatial/canvas, or demo-like

Turn those choices into concrete layout, type, color, media, and motion decisions.

## Direction Dials

Set these dials from 1 to 10 before designing when the brief is open-ended:

- `layout_variance`: 1 centered conventional, 5 balanced asymmetry, 10 experimental composition
- `motion_depth`: 1 static with hover, 5 section transitions, 10 scroll/canvas/spatial choreography
- `surface_density`: 1 spacious editorial, 5 normal product page, 10 compact operator dashboard
- `brand_commitment`: 1 neutral system UI, 5 clear accent identity, 10 brand carried by color, material, and type

Defaults for premium public sites: 6 / 5 / 4 / 6. Defaults for product dashboards: 4 / 3 / 7 / 3. Defaults for campaign or portfolio sites: 8 / 7 / 4 / 8.

## Design Lanes

Pick one lane and stay coherent:

- `editorial`: strong type hierarchy, unusual grid, restrained UI chrome, image/copy rhythm
- `product-precise`: crisp controls, dense proof, neutral palette, exact states, product credibility
- `luxury-service`: quiet rhythm, tactile materials, high-quality imagery, short confident copy
- `cinematic`: large spatial scenes, scroll pacing, image/video depth, minimal but strong copy
- `industrial`: mechanical grid, hard contrast, exposed structure, deliberate tension
- `soft-premium`: calm color, generous whitespace, rounded tactile controls, controlled spring motion

If the repo already has a system, preserve its best parts and change only what is weak.

## Remove Generic Output

Rewrite these before shipping:

- centered hero with vague headline and three feature cards
- repeated bento or card grids without a reason for the grid
- random gradients, blobs, dots, glows, browser chrome, decorative lines, or stock-looking dashboards
- huge display words that do not carry meaning
- unsupported metrics, testimonials, awards, logos, screenshots, or proof
- body text too light to read
- every section using the same entrance animation
- mobile layouts that simply stack desktop sections
- vague CTAs where the action can be specific
- placeholder copy or placeholder code comments in final output

## Redesign Protocol

For existing projects:

1. Inspect the rendered UI or existing files before proposing direction.
2. Preserve working IA, routes, real copy, assets, and brand anchors unless they are the issue.
3. Identify the top three failures: hierarchy, spacing, type, color, states, motion, content, accessibility, or responsiveness.
4. Change the smallest set of files that fixes the visible problem.
5. Compare before and after behavior, not just code diffs.

## Image-To-Code Protocol

When the user supplies a reference image or generated comp:

1. Extract layout skeleton, type scale, spacing rhythm, color roles, surface materials, media crop rules, component vocabulary, and motion implications.
2. Separate what to match from what to reinterpret.
3. Preserve semantic HTML and responsive behavior instead of copying pixels blindly.
4. Implement real components and states, not a screenshot imitation.
5. Run visual QA against desktop and mobile after implementation.

## Motion Rules

Motion must explain sequence, focus, depth, state, or continuity. If it does not, remove it.

Prefer one memorable motion idea over many identical entrance effects. Always define reduced-motion behavior. Never hide content behind animation that may fail in a paused tab, slow browser, or headless QA run.

## Preflight Before Handoff

Check:

- design lane matches the brief
- dials are visible in the output
- generic output has been removed
- typography is readable and not cramped
- color contrast is acceptable for body, muted, and placeholder text
- mobile composition has deliberate hierarchy
- states exist for hover, focus, loading, error, empty, disabled where relevant
- motion has purpose and reduced-motion fallback
- no unsupported claims were added
- final summary says what was changed and what was not verified
