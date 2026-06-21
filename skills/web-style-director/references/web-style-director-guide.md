# Web Style Director Guide

## Purpose

Prevent generic builds by giving the site a clear visual lane before implementation.

## Use When

- The user asks for a beautiful, premium, modern, cinematic, luxury, editorial, or reference-driven website.
- A site has no strong design direction yet.
- The task is a redesign or new build where visual quality matters.

## Do Not Use When

- A strict existing brand/design system must be followed without reinterpretation.
- The user asks for a tiny component fix with no visual direction change.

## Discovery Questions

- What is the site category and audience?
- What should the user feel in the first 5 seconds?
- What is the visual protagonist: type, product UI, photography, video, 3D, data, or copy?
- Which reference family is primary: Squarespace, Raycast/Linear/Vercel, luxury editorial, portfolio, cinematic motion?

## Decision Tree

- If the product is software/devtool, bias toward product realism and precise UI proof.
- If the subject is physical/human/place/lifestyle, bias toward imagery, materiality, and editorial pacing.
- If the user says Squarespace-like, bias toward clear business flow and elegant practicality.
- If the user says Viktor-style, bias toward motion choreography and non-template first viewport.
- If references conflict, choose one primary style and one accent style.

## Implementation Rules

- Define type, color, media, layout grammar, motion language, and copy voice before coding.
- Use one primary lane and avoid mixing every influence.
- Make the first viewport a composition with a subject, not a content slot.
- Name what is being intentionally avoided.
- For open-ended work, write a short art direction paragraph before file edits.

## Useful Patterns

- Quiet luxury: restrained palette, high-quality imagery, wide spacing, material details, slow reveals.
- Cinematic editorial: full-bleed media, scroll scenes, strong crop, narrative section rhythm.
- Product precision: real UI, code, metrics, crisp copy, dense but calm layouts.
- Squarespace polish: clean nav, practical actions, real categories, elegant but approachable hierarchy.
- Studio/portfolio: authored type, curated work grid, strong project moments, minimal filler.

## Anti-Patterns

- A direction that only says modern, clean, sleek, or premium.
- Dark hero plus gradient as default cinematic.
- Using UI library defaults as identity.
- Hero text inside a decorative card for a visual-first landing page.

## QA Checklist

- Ask whether the implemented page visibly follows the chosen lane.
- Check whether the page could be mistaken for a generic SaaS template.
- Inspect first viewport, type hierarchy, media treatment, and motion consistency.

## Acceptance Criteria

- The style direction affects concrete CSS/component decisions.
- The site can be described in one specific sentence without generic adjectives.
- The final page has at least one memorable art-directed moment.

## Shared Website Requirements

- Inspect before coding: project structure, framework, homepage/main entry, styling system, interaction/motion system, assets, and available commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, fix, continue, or similar.
- Use existing project conventions first; explain major dependencies before adding them.
- Default to premium modern quality without generic SaaS/agency/template patterns.
- Prefer real, generated, or art-directed visuals when the subject benefits from images, video, product UI, or spatial media.
- Build version 1, inspect the rendered result, improve visual quality, then run available checks again.
- Check desktop and mobile. Keep text readable, avoid overlaps, respect focus states and reduced motion.
- Report files changed, commands run, visual checks completed, and anything not tested.
