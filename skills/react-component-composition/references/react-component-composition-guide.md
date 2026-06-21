# React Component Composition Guide

## Purpose

Make React code feel designed and maintainable without flattening everything into generic components.

## Use When

- A React or Next.js page is large, repeated, or hard to scan.
- A website needs reusable sections, UI primitives, cards, media blocks, nav, forms, galleries, or product modules.
- The user wants a site that can be refined without rewriting a single giant file.

## Do Not Use When

- The change is a small one-line fix where extracting components adds noise.
- A local design system already dictates exact component structure.
- The project is not React and no React components are involved.

## Discovery Questions

- What is repeated because it is a true component versus repeated because the page needs varied composition?
- Which props describe content, state, variants, or behavior?
- Should this component be a primitive, section, or page-specific composition?
- Is the component server-rendered, client-interactive, or framework-neutral?

## Decision Tree

- Keep page files as composition maps when sections are complex.
- Extract primitives only when they reduce real duplication or clarify state.
- Use `children` or slots for flexible layout without prop explosions.
- Keep domain-specific components named by what they mean, not how they look.
- In Next.js, keep server/client boundaries in mind while composing.

## Implementation Rules

- Prefer clear component names over abstraction theater.
- Keep variants finite and visible; do not create a do-everything component.
- Let layout components own layout and content components own domain meaning.
- Keep visual polish in reusable primitives only when those primitives will actually repeat.
- Do not genericize away the unique site direction.

## Useful Patterns

- `HeroScene`, `ProofStrip`, `ProjectIndex`, `FeatureNarrative`, `EditorialMediaBand` for site-level sections.
- `Button`, `IconButton`, `TextLink`, `MediaFrame`, `Metric`, `Tag` for repeated primitives.
- Slot-based `SectionShell` only when spacing and heading behavior are truly consistent.

## Anti-Patterns

- Extracting every div into a component.
- Leaving a 900-line page because component splitting feels optional.
- Generic `Card` components used for every content type.
- Boolean prop overload such as `big`, `small`, `dark`, `fancy`, `special`.

## QA Checklist

- Read the page file: it should reveal the page story.
- Check component props for clarity and unused variants.
- Run type/lint/build checks.
- Verify visual output still has varied composition after extraction.

## Acceptance Criteria

- Components are reusable where helpful and specific where the design needs specificity.
- The code supports polish passes without turning into prop soup.
- The page remains visually non-generic.

## Shared Website Requirements

- Inspect before coding: project structure, framework, router, homepage or main entry, styling system, JavaScript or motion system, assets, and available commands.
- Prefer the existing project stack and conventions before adding dependencies or moving architecture.
- For Next.js App Router projects, keep Server Components as the default and introduce Client Components only for interactivity, browser APIs, effects, or client-only libraries.
- For React work, keep components pure, derive render data during render, and use Effects only to synchronize with external systems.
- Default website output must still follow the premium visual baseline: strong type, real content, designed states, responsive polish, and no generic card-grid filler.
- Run available lint, build, test, and local browser checks when possible; report exactly what ran and what was not tested.
- Check desktop and mobile behavior when changing visible UI, especially overflow, focus, loading, empty, error, and reduced-motion states.

## Official Source Anchors

- React Learn: https://react.dev/learn
- React reference: https://react.dev/reference/react
- Server and Client Components: https://nextjs.org/docs/app/getting-started/server-and-client-components
