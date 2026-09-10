# Audit Checklist

Use this checklist when reviewing motion design in any UI code.

---

## Philosophy Check (Do First)

- [ ] **How often will users trigger this?** (Frequent = less/no animation — Emil's rule)
- [ ] **Is this keyboard-initiated?** (Immediate response and stable focus; useful brief feedback can remain)
- [ ] **Does this animation serve a purpose?** (orientation, feedback, continuity, narrative or approved artistic expression)
- [ ] **Will users notice this animation consciously?** (If yes for production UI, probably too much)
- [ ] **Have I tested this with `prefers-reduced-motion: reduce`?**
- [ ] **Does this feel natural after the 10th interaction?** (Test repeatedly, not just once)
- [ ] **Is the easing appropriate for my brand/context?**
- [ ] **Is the duration appropriate for context?** (Emil prefers under 300ms; Jakub/Jhey may use longer for polish or effect)

---

## Motion Gap Analysis (Check BEFORE Reviewing Existing Animations)

Conditional UI changes are candidates for inspection, not findings. Instant transitions may be correct; evaluate demonstrated feedback, comprehension, focus and continuity first.

- [ ] **Searched for conditional renders** — `{condition && <Component />}` patterns
- [ ] **Searched for ternary swaps** — `{condition ? <A /> : <B />}` patterns
- [ ] **Searched for dynamic inline styles** — `style={{ prop: dynamicValue }}` without transition
- [ ] **Each conditional render** uses an appropriate transition or justified instant state
- [ ] **Mode switches** (tabs, toggles) preserve comprehensible state and focus; animate content only when useful
- [ ] **Settings panels** with conditional controls preserve useful state feedback, with motion only where warranted
- [ ] **Expandable sections** preserve content flow using instant state, measured layout/FLIP or bounded size animation
- [ ] **Loading → Content** transitions communicate readiness without delaying access

---

## Enter/Exit States

- [ ] Enter treatment fits purpose; opacity-only and instant are valid, blur optional
- [ ] Exit animations are subtler than enters (smaller translateY, same blur/opacity)
- [ ] `animation-fill-mode: backwards` used for delayed sequences
- [ ] Elements don't flash before their delayed animation starts

---

## Easing & Timing

- [ ] Appropriate easing for context (not default `ease` everywhere)
- [ ] Built-in/custom easing fits continuity and context; custom curves are available when useful
- [ ] Spring, timed or instant feedback selected for the interaction
- [ ] Durations appropriate for context (Emil: under 300ms; others: whatever serves the design)
- [ ] Consistent timing values across related animations
- [ ] Transform-origin matches interaction source (dropdowns from trigger)

---

## Visual Polish

- [ ] Shadows instead of borders where background varies
- [ ] Gradients using oklch color space for smooth blending
- [ ] Blur used intentionally as a state signal

---

## Optical Alignment

- [ ] Buttons with icons have adjusted padding
- [ ] Asymmetric icons (play, arrows) are visually centered
- [ ] Text and icons feel balanced

---

## State Transitions

- [ ] Icon swaps preserve understandable state and accessible feedback; motion is optional
- [ ] Loading states communicate readiness without delaying content
- [ ] Hover/focus states respond immediately; any transition duration fits frequency and preference
- [ ] Button press has clear feedback; subtle scale is one option when appropriate
- [ ] Scale distance supports the intended effect without disorientation; 0.9+ is a restraint option

---

## Interaction Patterns (Emil's Rules)

- [ ] Tooltips: first delayed + animated, subsequent instant
- [ ] Animations are interruptible (can change mid-animation)
- [ ] Reveal method fits content flow; clip-path and bounded size/layout alternatives are measured
- [ ] High-frequency actions have minimal or no animation
- [ ] Keyboard shortcuts respond immediately and preserve focus

---

## Performance

- [ ] `will-change` used sparingly and specifically
- [ ] Prefer transform/opacity; measure rendering cost and justify layout/effect exceptions
- [ ] Tested on low-end devices
- [ ] No continuous animations without purpose
- [ ] Rapid reversal and cancellation preserve continuity; choose transitions or an animation API that supports the required retargeting
- [ ] Compare scoped custom properties and direct style updates when a trace shows drag-related invalidation cost
- [ ] Gesture completion considers direction, displacement and recent velocity; test slow drags, quick flicks and reversal

---

## Accessibility

- [ ] Respects `prefers-reduced-motion`
- [ ] No vestibular triggers (excessive zoom, spin, parallax)
- [ ] Looping animations can be paused
- [ ] Functional animations have non-motion alternatives

---

## Quick Reference: Severity Levels

**Critical:** demonstrated blocked actions/content, severe focus disruption, harmful unavoidable motion without equivalent reduced-motion access, or severe measured performance failure.

**Important:** observed comprehension, continuity, readability or repeated-interaction friction; include evidence and context, not a rule-name alone.

**Context-dependent candidates:** instant state, missing exit or blur, size/layout animation, durations over 300ms, default easing, strong press scale or high-frequency feedback. Any can be correct. Test the purpose and consequence before reporting a defect.

**Opportunities:** optical alignment, suitable color space, springs, tooltip patterns, expressive authored motion. Keep artistic alternatives available; do not turn optional polish into release blockers.
