# Next.js Server Client Boundaries Guide

## Purpose

Protect performance, security, and maintainability by keeping interactivity narrow and intentional.

## Use When

- A Next.js App Router file needs `use client`, browser APIs, event handlers, state, refs, effects, Motion, GSAP, Lenis, or DOM measurement.
- A component fetches data, uses secrets, accesses server-only APIs, or could avoid shipping JavaScript.
- The page feels sluggish or bundle-heavy after adding interactive features.

## Do Not Use When

- The project is not Next.js App Router.
- The task is pure CSS or copy with no component boundary decisions.
- The app intentionally uses another architecture and no migration is requested.

## Discovery Questions

- Which exact elements need client-side state, events, browser APIs, or animation runtime?
- Which data can be fetched on the server close to its source?
- Are props passed into client components serializable?
- Can providers, modals, menus, or animation wrappers sit deeper in the tree?

## Decision Tree

- Start with Server Components for pages, layouts, content, data, and static sections.
- Add `use client` only at the smallest component boundary that needs it.
- Pass server data into Client Components as serializable props.
- Use `children` slots to nest server-rendered content inside client shells such as modals.
- Move providers as deep as possible instead of wrapping the whole document.
- Start independent server data work together; do not introduce a fetch waterfall merely to preserve component nesting.

## Implementation Rules

- Never expose secrets, tokens, private endpoints, or server-only modules to client bundles.
- Keep animation and interaction components narrow; the whole page should not become a client component for one reveal.
- Prefer server-rendered content for SEO, perceived speed, and lower JavaScript cost.
- Check imports after adding `use client`; everything imported becomes part of the client graph.
- Minimize and deduplicate serialized props crossing into client components.
- Do not hold request-specific mutable state at module scope.
- Use client-only effects with cleanup for listeners, observers, timers, and animation instances.

## Useful Patterns

- Server page fetches case-study data, passes title/images to a small animated gallery client component.
- Server layout renders static nav and logo, while a client search/menu island handles interaction.
- Client modal accepts server-rendered `children` content rather than fetching everything again.

## Anti-Patterns

- Adding `use client` to `app/layout.tsx` without a very strong reason.
- Passing ordinary nonserializable functions, unsupported class instances or server-only data across the client boundary. Supported Server Function references are allowed by React serialization; preserve their server authorization and input validation.
- Importing server-only helpers into client files.
- Using Effects to copy server props into redundant state.

## QA Checklist

- Search for `use client` and verify each boundary is justified.
- Inspect bundle or build output if bundle size is a concern.
- Run lint/build to catch server/client import mistakes.
- Manually test interactive islands without breaking route rendering.

## Acceptance Criteria

- Interactive code is narrow, explicit, and cleaned up.
- Server-rendered content stays server-rendered where possible.
- The component boundary improves performance and does not hide generic design shortcuts.

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.

## Official Source Anchors

- Server and Client Components: https://nextjs.org/docs/app/getting-started/server-and-client-components
- React reference: https://react.dev/reference/react
- You Might Not Need an Effect: https://react.dev/learn/you-might-not-need-an-effect

Serialization reference: [React use client](https://react.dev/reference/rsc/use-client). Follow the installed React/framework contract rather than banning every function prop.
