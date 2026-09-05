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

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.
