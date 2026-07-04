# Codex Premium Website Skills Context

Use this context when working on websites, landing pages, portfolios, product UI, frontend components, motion systems, accessibility, responsive QA, or final delivery.

## Core Behavior

- Inspect the project before changing code.
- Identify framework, entry files, styling system, interaction model, and available checks.
- Make a brief implementation plan before meaningful edits.
- Preserve existing project conventions unless a change clearly improves the result.
- Prefer project-local dependencies and avoid unnecessary global installs.

## Website Quality Standard

- Make the first viewport visually decisive.
- Use specific copy tied to the actual product, person, venue, or audience.
- Avoid generic AI website patterns: vague headlines, centered hero plus card grids, random gradients, decorative blobs, fake product UI, placeholder testimonials, unsupported metrics, and weak mobile stacking.
- Use typography, spacing, color, imagery, and layout as a coherent system.
- Use visual assets when the subject benefits from them.
- Keep text readable and prevent overflow across common mobile and desktop sizes.

## Frontend Implementation

- Use semantic markup and accessible controls.
- Check responsive behavior and avoid horizontal overflow.
- Add stable dimensions for toolbars, tiles, boards, cards, media, and counters.
- Use existing components and helpers before inventing new abstractions.
- Run available lint, build, and test commands when possible.

## Motion And Interaction

- Use motion to clarify state, sequence, depth, focus, or tactility.
- Respect reduced-motion preferences.
- Avoid animation on frequent or keyboard-initiated actions unless it is instant and functional.
- Prefer CSS for simple transitions, Motion for React state/layout animation, and GSAP for timeline-heavy or scroll-choreographed scenes.

## QA And Handoff

Before final delivery, report:

- files changed
- commands run
- checks passed
- checks not run
- responsive/browser inspection notes
- accessibility or reduced-motion notes
- known limitations
- recommended next steps

## Safety

- Preserve user work.
- Avoid destructive edits unless explicitly requested.
- Create or explain a rollback path before risky edits.
- Do not invent proof, testimonials, metrics, logos, or unsupported claims.
