# Editorial Typography Systems Guide

## Purpose

Make typography carry hierarchy, mood, and polish without breaking responsive layouts.

## Use When

- The site needs strong visual quality or feels default.
- Headings, labels, body copy, or buttons lack hierarchy.
- A homepage, portfolio, product site, luxury site, or editorial page is being built.

## Do Not Use When

- The project has a strict existing type system and the task does not include redesign.
- The user is asking only for backend or data work.

## Discovery Questions

- What type roles are needed: display, heading, body, caption, label, mono/code?
- Is the mood editorial, technical, luxury, warm, severe, playful, or business-ready?
- What is the longest heading/button/nav label on mobile?

## Decision Tree

- If software/devtool, bias toward precise sans plus optional mono.
- If luxury/editorial, consider serif/sans contrast or elegant display face.
- If Squarespace-like business, choose approachable readable type with clear hierarchy.
- If content-heavy, prioritize line length and body readability over dramatic display.

## Implementation Rules

- Define type roles before assigning sizes.
- Use clamp with sensible min/max, not viewport-width font scaling.
- Cap body line length around 65 to 75 characters.
- Use text-wrap balance for headings and pretty wrapping for prose when supported.
- Default letter spacing to zero; use tracking sparingly for labels.
- Treat -0.04em as a cautious starting threshold; approved display typography may exceed it after optical, readability, wrapping and mobile checks.

## Useful Patterns

- Vercel-like: precise sans, strong weights, restrained mono detail.
- Luxury: high-contrast display or elegant serif paired with quiet sans body.
- Portfolio: expressive display with calm readable project descriptions.
- Squarespace polish: friendly type scale, generous line-height, legible forms.

## Anti-Patterns

- Huge hero type that breaks mobile.
- Weak gray body text for elegance.
- Three unrelated fonts.
- All sections using the same heading size.
- Buttons with clipped or wrapped labels.

## QA Checklist

- Check h1/h2/body/caption/button roles on desktop and mobile.
- Inspect longest labels and headings.
- Check contrast and line length.
- Verify no text overlaps media or controls.

## Acceptance Criteria

- Hierarchy is visible without reading every word.
- Text feels intentional and remains usable on mobile.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.
