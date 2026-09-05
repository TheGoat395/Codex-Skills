# Accessibility Performance Polish Guide

## Purpose

Keep high-end websites usable, readable, fast, and stable.

## Use When

- Before final delivery of a polished site.
- When adding motion, media, forms, custom controls, canvas/WebGL, or heavy visuals.
- When a design looks good but may be hard to use.

## Do Not Use When

- No UI exists or the task is backend-only.
- A separate strict accessibility audit is requested, which should be treated more formally.

## Discovery Questions

- Can all interactive controls be reached and understood by keyboard/screen reader?
- Do text and controls have sufficient contrast?
- Are images/videos/canvas optimized and accessible?
- Do animations respect reduced motion and avoid jank?

## Decision Tree

- If custom controls exist, check semantics and keyboard behavior.
- If images/video exist, check dimensions, loading, alt text, and mobile payload.
- If animation exists, check transforms/opacity, cleanup, and reduced-motion fallbacks.
- If WebGL/canvas exists, provide surrounding HTML context and fallbacks.

## Implementation Rules

- Use semantic landmarks, headings, buttons, links, labels, and lists.
- Use focus-visible styles and clear interactive states.
- Provide useful alt text for content images and empty alt/decorative treatment for decoration.
- Avoid huge unoptimized media and unnecessary heavy libraries.
- Design disabled/loading/error/empty states with readable text.

## Useful Patterns

- Button-like action uses button; navigation uses link.
- Motion fallback: instant state or crossfade.
- Large images: stable dimensions, responsive sizes, lazy below fold.
- Video hero: muted/playsinline, poster, controls or accessible fallback when needed.

## Anti-Patterns

- Divs with click handlers and no keyboard support.
- Canvas-only communication.
- Low-contrast muted text.
- Autoplay video that harms performance and readability.
- Animations of layout properties creating jank.

## QA Checklist

- Tab through key controls.
- Check contrast-sensitive text visually and with available tooling if possible.
- Check reduced-motion CSS/logic.
- Run build and inspect console/network issues.

## Acceptance Criteria

- The beautiful version is still usable and reasonably fast.
- Major a11y/performance tradeoffs are fixed or clearly reported.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.
