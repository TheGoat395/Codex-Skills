# Motion React Patterns Guide

## Purpose

Use Motion when React state, component lifecycle, and declarative animation should stay aligned.

## Use When

- A React or Next.js UI needs polished component animation, reveal timing, hover/tap/focus states, or state-driven transitions.
- The existing project already uses Motion or a React-native animation API would be cleaner than imperative timelines.
- Motion should elevate product tactility without turning a site into animation soup.

## Do Not Use When

- A simple CSS transition handles the effect cleanly.
- The choreography is timeline-heavy, scroll-pinned, text-split, or SVG-path based and GSAP is a better fit.
- The project is not React and Motion for React is not appropriate.

## Discovery Questions

- Does the project already use Motion, CSS transitions, GSAP, or another animation library?
- Which UI state drives the animation: mount, hover, tap, focus, in-view, open, selected, loading, or route change?
- What should motion clarify for the user?
- What is the reduced-motion alternative?

## Decision Tree

- Use CSS first for trivial hover/focus color or opacity changes.
- Use Motion components when animation follows React state, props, or component lifecycle.
- Use variants for repeated child choreography and staggered groups.
- Use `useReducedMotion` or MotionConfig for motion-sensitive branches.
- Keep Motion islands scoped so server-rendered or static content stays lean.

## Implementation Rules

- Animate transform and opacity before layout-affecting properties.
- Keep durations short for tools and calmer for editorial scenes.
- Do not animate essential text in ways that delay comprehension.
- Avoid novelty motion on every element.
- Clean up imperative `useAnimate` sequences when components unmount.

## Useful Patterns

- Button tactility: slight y/scale/tint change on hover/tap with focus-visible styling.
- Content reveal: in-view opacity/y with a small stagger and no layout shift.
- State panel: selected card grows subtly while siblings calm down.
- Premium load-in: first viewport elements sequence by semantic priority.

## Anti-Patterns

- Using Motion for every CSS hover color.
- Animating large sections from far off-screen.
- Default spring bounce on luxury or serious product sites.
- No reduced-motion path.

## QA Checklist

- Test mouse, keyboard focus, touch, and reduced-motion behavior.
- Check mount/unmount and route navigation for stale animation state.
- Inspect mobile performance and layout shift.
- Run build/lint for import and client-boundary issues.

## Acceptance Criteria

- Motion is scoped, purposeful, and compatible with React state.
- The interaction feels premium without slowing comprehension.
- Reduced-motion users still get a complete experience.

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
- Motion AnimatePresence: https://motion.dev/docs/react-animate-presence
- Motion gestures: https://motion.dev/docs/react-gestures
- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
