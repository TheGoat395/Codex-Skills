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

- Use at least three distinct layout patterns on long pages.
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
- Uniform section padding from top to bottom of the page.

## QA Checklist

- List the section pattern for every major section and check for repetition.
- Check that layout improves content comprehension.
- Inspect mobile: transformed layouts should still feel composed.

## Acceptance Criteria

- Each section has a reason for its layout.
- The page has rhythm without chaos.

## Shared Website Requirements

- Inspect before coding: project structure, framework, homepage/main entry, styling system, interaction/motion system, assets, and available commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, fix, continue, or similar.
- Use existing project conventions first; explain major dependencies before adding them.
- Default to premium modern quality without generic SaaS/agency/template patterns.
- Prefer real, generated, or art-directed visuals when the subject benefits from images, video, product UI, or spatial media.
- Build version 1, inspect the rendered result, improve visual quality, then run available checks again.
- Check desktop and mobile. Keep text readable, avoid overlaps, respect focus states and reduced motion.
- Report files changed, commands run, visual checks completed, and anything not tested.
