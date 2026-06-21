# Animation Easing Language Guide

## Purpose

Make motion feel consistent and intentional instead of random durations and bouncy defaults.

## Use When

- A site has many animations with inconsistent durations/easing.
- The user asks for luxury, cinematic, modern, snappy, soft, editorial, or product-grade motion.
- A motion system needs tokens or shared timing decisions.

## Do Not Use When

- The project has no animation or only one trivial CSS transition.
- A strict existing motion spec must be followed exactly.
- The task is purely technical cleanup with no timing changes.

## Discovery Questions

- What motion personality fits the site: calm, crisp, tactile, cinematic, playful, precise, restrained?
- Which interactions need instant feedback versus staged reveal?
- What durations and easings already exist?
- Which motion should be tokenized for reuse?

## Decision Tree

- Define motion personality before picking numbers.
- Use shorter durations for direct controls and longer ones for scene transitions.
- Use consistent easing families for similar interaction types.
- Use stagger to reveal semantic groups, not arbitrary lists.
- Document tokens if multiple components use them.

## Implementation Rules

- Avoid default bounce on serious, luxury, or precise product interfaces.
- Keep direct manipulation responsive.
- Stagger by reading order and importance.
- Do not stack delays until the page feels slow.
- Use reduced-motion equivalents that preserve state clarity.

## Useful Patterns

- Product precision: 120-220ms controls, crisp ease-out, subtle y/opacity.
- Luxury/editorial: 500-900ms scene reveals, slow ease, restrained distance.
- Cinematic scroll: timeline labels, overlapping beats, no dead scroll.
- Playful tool: slightly springy tap/drag, still controlled.

## Anti-Patterns

- Every animation using 1 second ease-in-out.
- Random delays on all sections.
- Motion tokens copied from another brand without mood fit.
- Bouncy springs on luxury typography.

## QA Checklist

- List all changed durations/easings and check consistency.
- Watch the page at normal scroll/click speed.
- Test reduced motion.
- Inspect whether motion slows core tasks.

## Acceptance Criteria

- Motion has a recognizable timing language.
- Controls feel fast and scenes feel composed.
- Timing values support the site's art direction.

## Shared Website Requirements

- Inspect before coding: framework, router, rendering mode, styling system, motion libraries, scroll setup, entry files, reduced-motion handling, and available verification commands.
- Use the existing project motion stack first. Add Motion, GSAP, Lenis, or other animation libraries only when the interaction requires them and explain why.
- Prefer CSS transitions for simple local state changes; use Motion for React-state, layout, gesture, and component transitions; use GSAP for timeline-heavy, scroll-pinned, SVG, text, or advanced choreography.
- Keep animation purposeful: clarify sequence, depth, focus, tactility, or product understanding. Do not use motion to hide weak layout or generic copy.
- Respect accessibility: reduced motion, keyboard access, focus management, no hover-only essential behavior, and no motion that blocks content.
- Protect performance: prefer transform and opacity, avoid layout thrashing, clean up timelines/listeners/observers, and test mobile.
- Run available lint, build, test, and local browser checks when possible; report exact commands and untested areas.

## Official Source Anchors

- Motion for React: https://motion.dev/docs/react
- GSAP docs: https://gsap.com/docs/v3/
- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
