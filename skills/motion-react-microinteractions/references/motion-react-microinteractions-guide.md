# Motion React Microinteractions Guide

## Lens

Microinteractions are state communication. They should be quiet, fast, and consistent.

## Rules

- Use CSS transitions for simple color, shadow, and transform state changes.
- Use Motion for component lifecycle, layout transitions, gesture states, and scroll values.
- Centralize common transitions and easings.
- Design hover, active, focus-visible, disabled, loading, and empty states.

## Useful Patterns

- Button: slight translate or background sweep, clear focus ring, icon movement.
- Card: media scale or reveal, not whole-card wobble.
- Menu: opacity plus y or clip reveal with focus management.
- Tabs: layout indicator and content crossfade.

## Avoid

- Animating layout properties that cause jank.
- Huge hover lifts on dense product UI.
- Missing reduced-motion handling.

## Acceptance Criteria

- Interactive elements communicate state clearly.
- Motion is visible but not noisy.

## Shared Requirements

- Inspect before coding: structure, framework, homepage or main entry file, styling system, JavaScript or interaction system, assets, and build commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, or fix.
- Use existing project conventions first. Explain major new dependencies before adding them.
- Never ship generic visual work: no default card grids, placeholder copy, weak type, random gradients, stock-like media, or template heroes.
- Build version 1, inspect the rendered result, improve spacing, type, hierarchy, motion, media, hover states, and responsiveness, then run checks again.
- Run available lint, build, and test commands when possible. Report commands, changed files, and any untested areas honestly.
- Check desktop and mobile. Respect accessibility, semantic markup, focus states, and reduced-motion preferences.
