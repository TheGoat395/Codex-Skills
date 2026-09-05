---
name: web-design-direction-system
description: "Resolve shared design intent and guidance."
---

# Web Design Direction System

Use this as the high-level router before detailed build, redesign, or polish work.

## Design Guidance Contract

When a project has repeated design decisions, a named design system, or a recurring review failure, read [the design guidance evidence loop](references/design-guidance-evidence-loop-guide.md) before changing the standard. Start with the reader's job and the strongest supported answer, then choose the smallest destination that can enforce the decision: guidance, a component primitive, a deterministic check, an exemplar, or an evaluation case.

Do not turn one screenshot, one reviewer preference, or one shipped implementation into a universal rule. Record scope, rationale, evidence, exceptions, and a bad/good example. Keep unresolved decisions visible instead of hiding them inside CSS or component code.

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

Motion should serve sequence, focus, depth, state, continuity, narrative, artistic expression or deliberate delight. Remove motion that lacks a purpose in the actual brief.

Prefer one memorable motion idea over many identical entrance effects. Always define reduced-motion behavior. Never hide content behind animation that may fail in a paused tab, slow browser, or headless QA run.

## Evidence Loop

For a repeated design correction, freeze a representative prompt, inputs, viewport, model, and skill version. Save one baseline without the proposed guidance, then compare first-attempt treatment output under the same conditions. Review the pair against a written rubric, keep a small holdout case, and encode only corrections that generalize.

Separate retrieval from application: confirm that the right skill or reference loaded before judging whether the rule was followed. Keep deterministic checks for observable mechanics and keep product judgment in scoped prose. Feed repeated production corrections back into a pending review record rather than editing the standard automatically.

## Preflight Before Handoff

Check:

- design lane matches the brief
- optional dials support the chosen direction without overriding the brief
- generic output has been removed
- typography is readable and not cramped
- color contrast is acceptable for body, muted, and placeholder text
- mobile composition has deliberate hierarchy
- states exist for hover, focus, loading, error, empty, disabled where relevant
- motion has purpose and reduced-motion fallback
- no unsupported claims were added
- final summary says what was changed and what was not verified

Read the evidence-loop reference when a change updates a shared design standard, evaluation protocol, or recurring correction pattern.

## Scope and evidence

Own the shared direction record. Preserve explicit user direction and adequate existing context; blueprint, style director and build gate consume the same spec. Dials are optional internal tools and need not appear in a deliverable.
