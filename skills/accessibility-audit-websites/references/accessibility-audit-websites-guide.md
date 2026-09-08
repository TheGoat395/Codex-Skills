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

## Worked Checks

- Dialog: open it using the keyboard, identify the initial focus, traverse controls in both directions, and close it using its supported keyboard action. For a modal, background controls must not enter the tab sequence; closing should restore focus to the opener or a logical surviving control. Record the exact step where focus escapes or disappears.
- Form: submit an empty required field and then an invalid value. Check that the error identifies the field and correction, is programmatically associated with the control, and can be discovered without relying on color. Correct the value and confirm stale error state clears. Test failed submission without losing entered data.
- Icon control: inspect its accessible name, role and state, then activate it by keyboard. A visible tooltip does not by itself prove a usable accessible name. For a toggle, verify the exposed state changes with the visible state.
- Sticky header: tab through content after scrolling. Confirm each focused target remains visible rather than hidden beneath the header. Test enlarged text and a narrow viewport for clipped controls or an inaccessible off-screen action.
- Automated finding: reproduce it on the specified route and state, inspect the affected node, and distinguish a confirmed defect from a tool limitation. After a fix, repeat the failing manual step and the relevant scan, not only the default page load.

For contrast, target-size or other numerical conformance claims, identify the applicable WCAG version, level, criterion and exceptions from the official source below. Record the measured value and method; do not substitute a visual impression or an unrelated threshold.

## QA Checklist

- Run available automated tools if present.
- Manually test keyboard navigation.
- Inspect accessible names/labels.
- Check motion/media alternatives.

## Acceptance Criteria

- Core content and actions are accessible by keyboard and assistive tech patterns.
- Forms and controls are named and understandable.
- Known accessibility gaps are fixed or reported.
- Each finding names the route/state, reproduction steps, expected versus observed behavior, impact and retest result. Record browser and assistive technology used; an accessibility-tree inspection is not a screen-reader test.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
