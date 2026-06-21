# Website Blueprint First Guide

## Purpose

Lock the plan before coding so the build does not drift into generic filler.

## Use When

- The user asks to create, redesign, or heavily rework a site.
- The brief includes strong taste goals but weak structure.
- The user wants to avoid previous bad outputs and start from a clean direction.

## Do Not Use When

- The user explicitly asks for a tiny implementation change.
- A full approved design spec already exists and only needs coding.

## Discovery Questions

- What is the exact repo/path and source of truth?
- What pages and sections are needed?
- What assets exist and which need generation or placeholders?
- What are the primary references and anti-references?
- What commands will verify the build?

## Decision Tree

- If the site category is unclear, classify it before writing a blueprint.
- If assets are missing, define asset slots and acceptable generation/search strategy.
- If the user asked to proceed, keep blueprint brief and immediately implement.
- If confirmation is required, stop after planned files and design contract.

## Implementation Rules

- Blueprint must include audience, offer, page map, section order, visual lane, type, color, media, motion, responsive behavior, and QA.
- Each section needs purpose, content, layout, asset need, and interaction/motion notes.
- Define what will not be built to avoid scope creep.
- For visual-first work, consider a generated image or mockup only when it clarifies the direction.

## Useful Patterns

- Homepage blueprint: hero, proof, offer/value, detail sections, conversion, footer.
- Product blueprint: product UI hero, workflow proof, use cases, integrations, pricing, docs/trust.
- Portfolio blueprint: selected work, case study rhythm, about, process, contact.
- Luxury blueprint: scene, material detail, story, gallery, offering, booking/purchase.

## Anti-Patterns

- Blueprints that list generic sections without visual instructions.
- Starting image generation before defining the page purpose.
- Building from old/bad context when the user requested a fresh start.

## QA Checklist

- Compare final page to blueprint section by section.
- Confirm visual lane, asset strategy, and motion model survived implementation.
- Report intentional deviations.

## Acceptance Criteria

- Another agent could build from the blueprint and land in the same direction.
- The user can approve/reject the direction before large edits.

## Shared Website Requirements

- Inspect before coding: project structure, framework, homepage/main entry, styling system, interaction/motion system, assets, and available commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, fix, continue, or similar.
- Use existing project conventions first; explain major dependencies before adding them.
- Default to premium modern quality without generic SaaS/agency/template patterns.
- Prefer real, generated, or art-directed visuals when the subject benefits from images, video, product UI, or spatial media.
- Build version 1, inspect the rendered result, improve visual quality, then run available checks again.
- Check desktop and mobile. Keep text readable, avoid overlaps, respect focus states and reduced motion.
- Report files changed, commands run, visual checks completed, and anything not tested.
