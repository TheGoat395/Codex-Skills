# Color Material Lighting Direction Guide

## Purpose

Make palette, surface, and lighting choices support the site concept and readability.

## Use When

- Starting or redesigning a visual system.
- The site looks flat, random, too purple, too beige, too dark, or too template-like.
- The prompt includes luxury, cinematic, Vercel-like, Linear-like, Raycast-like, or Squarespace-polished.

## Do Not Use When

- The task requires no color/material refinement. A strict palette stays locked while semantic surfaces, contrast and lighting roles may still be refined.
- The task does not touch visual design.

## Discovery Questions

- What is the emotional temperature: cool precision, warm hospitality, dark cinematic, bright commerce, quiet editorial?
- What colors are brand constraints versus optional accents?
- What surfaces are needed: page, panels, media frames, inputs, nav, footer, overlays?
- What contrast requirements apply to body, labels, buttons, and muted text?

## Decision Tree

- If product/devtool, use restrained neutrals plus sharp accent and real UI contrast.
- If luxury/lifestyle, use material colors derived from imagery and brand context.
- If cinematic, define light source, depth, and readable foregrounds.
- If business/Squarespace-like, use approachable contrast and conversion clarity.

## Implementation Rules

- Define role-based tokens: bg, surface, surface-2, ink, muted, border, accent, focus, danger, success.
- Use gradients only as light/material/energy, not decoration by default.
- Avoid one-hue domination unless monochrome is the concept.
- Body text must have accessible contrast; muted text cannot be illegible.
- Surfaces should have hierarchy: page, panel, interactive, overlay.

## Useful Patterns

- Vercel precision: black/white/gray with minimal accent and crisp borders.
- Linear depth: dark surfaces, subtle luminous edges, meaningful gradients.
- Raycast energy: dark command surface, red/action accents, clean states.
- Luxury material: muted neutrals, textured imagery, material accent, calm contrast.

## Anti-Patterns

- Gold plus black as automatic luxury.
- Purple-blue gradient as automatic modern.
- Glassmorphism everywhere.
- Low-contrast gray body copy.
- Random hex values instead of tokens.

## QA Checklist

- Check contrast for body, muted text, buttons, labels, inputs.
- Scan CSS for one-note hue domination and random one-off colors.
- Check dark sections for readability and visual purpose.

## Acceptance Criteria

- Color roles are reusable and concept-aligned.
- The palette supports hierarchy and does not feel random.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.
