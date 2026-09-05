# React State And Effects Discipline Guide

## Purpose

Keep React interfaces predictable, fast, and easier to polish by avoiding unnecessary state and effect chains.

## Use When

- A component uses `useEffect` to transform props, derive data, or handle events.
- State is duplicated, contradictory, stale, or reset in surprising ways.
- The UI has complex interaction state such as filters, tabs, modals, forms, accordions, or animations.

## Do Not Use When

- A tiny static component has no state or effects.
- An external library requires a specific effect lifecycle and it is already correct.
- The task is purely CSS with no React logic.

## Discovery Questions

- Can this value be calculated from props or state during render?
- Is this logic caused by a user event, an external system, or rendering?
- Can state be simplified, normalized, or moved up/down?
- What cleanup is required for subscriptions, observers, timers, animation, or DOM APIs?

## Decision Tree

- If data is derived, calculate it during render or memoize only when expensive.
- If logic is caused by a click/input/submit, keep it in the event handler.
- If the component synchronizes with browser DOM, network, storage, or a non-React widget, use an Effect with cleanup.
- If many state variables change together, consider a reducer or single state object.
- If state is shared by siblings, lift it to the closest common owner.

## Implementation Rules

- Do not mirror props in state unless the user is intentionally editing a draft copy.
- Avoid Effects that only set other React state.
- Keep dependency arrays honest; fix architecture rather than suppressing lints.
- Use refs for mutable instance values that should not trigger renders.
- Clean up listeners, observers, intervals, timeouts, GSAP timelines, and external instances.

## Useful Patterns

- Filter lists by deriving `visibleItems` from `items` and `query` during render.
- Submit forms in submit handlers, not effects watching `submitted`.
- Use an effect to subscribe to resize, media query, intersection observer, or third-party widgets with cleanup.

## Anti-Patterns

- Effect chains where one effect sets state that triggers another effect.
- Disabling hook lint rules to silence stale closure warnings.
- Storing both `selectedId` and `selectedItem` when one derives from the other.
- Using context for local component state that only two children need.

## QA Checklist

- Search changed files for `useEffect`, `useMemo`, `useCallback`, and duplicated state.
- Test repeated open/close, filter, route navigation, and unmount/remount flows.
- Run lint to catch hook dependency issues.
- Check that visual states do not flicker because of effect-driven render loops.

## Acceptance Criteria

- State has a single source of truth.
- Effects are limited to external synchronization and are cleaned up.
- The component is easier to reason about and still supports the intended polish.

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.

## Official Source Anchors

- React reference: https://react.dev/reference/react
- You Might Not Need an Effect: https://react.dev/learn/you-might-not-need-an-effect

## Async response ownership

Older asynchronous work must not overwrite the result for the current input or route. Use cancellation where supported and/or request identity/ignore handling tied to the current request; aborting alone does not prove a server-side effect was undone. Test out-of-order resolution after rapid input changes, navigation and unmount. Keep derived data in render and event-triggered work in handlers; do not introduce a reducer, effect or global store solely for this check.
