# Section Layout Systems Guide

## Purpose

Match section layout to content shape instead of defaulting to cards.

## Use When

- A page has multiple sections and needs rhythm.
- Feature cards, bento grids, or repeated panels are becoming generic.
- The site needs editorial, premium, product, or Squarespace-like variety.

## Do Not Use When

- A truly repeated collection needs equal scannable items, such as products or articles.
- The design system intentionally uses cards and the task is not visual redesign.

## Discovery Questions

- What type of content is this section: sequence, comparison, proof, gallery, specs, story, catalog, CTA?
- Does this content need equal items or a more editorial hierarchy?
- What section pattern was used immediately before and after?

## Decision Tree

- If content compares options, use a table, split ledger, or side-by-side proof.
- If content tells process, use timeline, sticky steps, or numbered narrative.
- If content shows work, use gallery wall, case plate, or media strip.
- If content lists specs/features, use ledgers, annotated UI, or grouped rows.
- If content is emotional, use full-bleed media and prose, not cards.

## Implementation Rules

- Use distinct layout patterns where content roles need them; an intentional repeated rhythm is valid when it supports comparison and comprehension.
- Cards are allowed only when the repeated item shape earns them.
- Avoid nested cards and floating-card page sections.
- Use full-width bands, rules, ledgers, tables, sticky panels, media slabs, and asymmetry.
- Keep pattern variation coherent with tokens and type roles.

## Useful Patterns

- Ledger: label/value rows for capabilities, specs, services.
- Artifact plate: large image/UI with caption and context.
- Sticky story: fixed visual with changing text steps.
- Editorial spread: asymmetrical media and prose.
- Comparison matrix: pricing/features without plan-card sameness.

## Anti-Patterns

- Every section inside a rounded rectangle.
- Bento grids where all boxes are just cards.
- Stat strips with fake animated counters.
- Uniform section padding that obscures content hierarchy; intentional consistent rhythm is valid.

## QA Checklist

- List the section pattern for every major section and check for repetition.
- Check that layout improves content comprehension.
- Inspect mobile: transformed layouts should still feel composed.

## Acceptance Criteria

- Each section has a reason for its layout.
- The page has rhythm without chaos.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.
