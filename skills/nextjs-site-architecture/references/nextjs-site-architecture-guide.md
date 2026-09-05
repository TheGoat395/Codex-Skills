# Next.js Site Architecture Guide

## Lens

Architecture should let the design stay consistent while keeping pages easy to refine.

## Rules

- Inspect existing Next.js version, app/pages router, src directory, styling, and scripts.
- Keep page files as composition once sections grow.
- Use next/font or project-approved font loading.
- Use next/image or appropriate image strategy for real assets.
- Keep client components limited to interactions that need the client.
- Start independent route data together and avoid nesting that creates accidental waterfalls.
- Keep serialized Server Component props narrow and avoid request-specific mutable module state.
- Give route loading, error, not-found, and retry states intentional behavior.
- Route deep React/Next performance implementation and measurement through `$performance-audit-websites`.

## Useful Patterns

- src/app/page.tsx for composition.
- src/components/sections for page sections.
- src/components/ui for primitives.
- src/lib/content.ts for structured copy and content.
- src/app/globals.css for tokens and base styles.

## Avoid

- Putting all page logic, content, and styling in one huge file.
- Making the whole app a client component unnecessarily.
- Ignoring metadata and accessible document structure.

## Acceptance Criteria

- The site structure supports iteration and polish.
- Server/client ownership and critical data-loading paths are intentional.
- Build commands pass or failures are reported honestly.

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.
