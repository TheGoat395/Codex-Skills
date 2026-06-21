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
- Viktor-style means precise motion, smooth scroll choreography, layered reveals, and non-template composition, unless the user provides exact references.

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

- Check that every adjective used in the plan has at least three concrete implementation consequences.
- Remove any adjective that does not affect the actual design.
- Use the definitions to guide polish edits.

## Acceptance Criteria

- The design vocabulary can be used as a checklist during implementation.
- The final page visibly embodies the defined terms.

## Shared Website Requirements

- Inspect before coding: project structure, framework, homepage/main entry, styling system, interaction/motion system, assets, and available commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, fix, continue, or similar.
- Use existing project conventions first; explain major dependencies before adding them.
- Default to premium modern quality without generic SaaS/agency/template patterns.
- Prefer real, generated, or art-directed visuals when the subject benefits from images, video, product UI, or spatial media.
- Build version 1, inspect the rendered result, improve visual quality, then run available checks again.
- Check desktop and mobile. Keep text readable, avoid overlaps, respect focus states and reduced motion.
- Report files changed, commands run, visual checks completed, and anything not tested.
