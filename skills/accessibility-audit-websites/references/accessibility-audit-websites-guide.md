# Accessibility Audit Websites Guide

## Purpose

- Make sites usable for more people and prevent polished visuals from hiding broken interaction.

## Discovery Questions

- What interactive controls and forms exist?
- Can the page be navigated by keyboard?
- Are headings, labels, alt text, and landmarks meaningful?
- Does motion/media need reduced-motion or captions?

## Implementation Rules

- Do not rely only on automated audits.
- Prefer semantic HTML over ARIA patches.
- Make focus visible and logical.
- Label every form control.
- Ensure important information is not image/video-only.

## Useful Patterns

- Keyboard pass: tab order, menus, dialogs, forms, CTAs.
- Screen-reader structure pass: headings, landmarks, labels.
- Media pass: alt text, captions, reduced motion.
- Contrast/focus pass for controls and links.

## Anti-Patterns

- Icon buttons without accessible names.
- Placeholder-only form labels.
- Hover-only content.
- Focus outline removed without replacement.

## QA Checklist

- Run available automated tools if present.
- Manually test keyboard navigation.
- Inspect accessible names/labels.
- Check motion/media alternatives.

## Acceptance Criteria

- Core content and actions are accessible by keyboard and assistive tech patterns.
- Forms and controls are named and understandable.
- Known accessibility gaps are fixed or reported.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
