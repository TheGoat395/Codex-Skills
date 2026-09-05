# Web Design Vocabulary Guide

## Purpose

Make subjective taste actionable so Codex does not hallucinate generic aesthetics.

## Use When

- The prompt relies on adjectives like premium, luxury, cinematic, modern, clean, polished, editorial, or bold.
- The user is frustrated because previous output looked generic.
- A skill or plan needs shared definitions before implementation.

## Do Not Use When

- The user has provided exact tokens, comps, and component specs.
- The task is mechanical and design language is irrelevant.

## Discovery Questions

- Which adjective is primary and which is secondary?
- Does the adjective describe audience perception, layout, motion, color, copy, or media?
- What common visual cliche should be avoided for this adjective?

## Decision Tree

- Map each taste word to type, layout, color, media, motion, copy, and QA.
- If two words conflict, choose primary/secondary hierarchy.
- Convert the definitions into acceptance criteria before building.
- During QA, reject visual choices that contradict the definitions.

## Implementation Rules

- Premium means exact spacing, complete states, sharp typography, credible content, and no defaults.
- Luxury means restraint, materiality, provenance, atmosphere, and confidence; not black/gold by default.
- Cinematic means scene progression, depth, full-bleed media, camera-like movement, and reveal rhythm; not just dark overlays.
- Modern means current, precise, fast, product-grade, interaction-aware, and visually disciplined; not empty minimalism.
- Squarespace-polished means elegant practical clarity, real business paths, image-forward sections, and complete conversion flows.
- Raycast/Linear/Vercel-polished means product realism, crisp copy, dense details, speed, and refined technical trust.
- For Viktor-style, inspect the exact supplied/current source and name observed traits; do not infer a universal creator formula from the name.

## Useful Patterns

- Define: Premium = typography scale, tokenized spacing, credible media, designed states, browser QA.
- Define: Editorial = strong type roles, asymmetry, captions, image pacing, article-like rhythm.
- Define: Minimal = fewer elements with stronger hierarchy, not weak contrast or empty space.
- Define: Bold = decisive composition and scale, not random color and oversized everything.

## Anti-Patterns

- Using taste words in final summaries without showing evidence.
- Equating luxury with beige, gold, black, or serif font only.
- Equating modern with a centered hero and three cards.
- Equating cinematic with unusable dark sections.

## QA Checklist

- Translate taste words into enough concrete choices to make the direction implementable; no arbitrary count.
- Remove any adjective that does not affect the actual design.
- Use the definitions to guide polish edits.

## Acceptance Criteria

- The design vocabulary can be used as a checklist during implementation.
- The final page visibly embodies the defined terms.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.
