# Creation Gotchas

These are context-dependent interpretive defaults, not designer-authored authority or universal aesthetic rules. Apply the actual user direction, purpose, frequency, accessible state and measured consequence; purposeful artistic expression remains available.

Use the applicable checks when writing motion. Verify rendered behavior, not only the generated source; unrelated patterns need no extra workflow.

---

## Motion that shouldn't exist

- **Don't animate just because you can.** Decorative motion added "for polish" is the default failure mode. Every animation needs a purpose — feedback, orientation, continuity, narrative, artistic expression or deliberate delight in the brief. If you can't name the purpose, remove it.
- **Keep high-frequency interactions immediate.** Prefer instant or brief feedback and test repeated use; do not remove useful state feedback merely because it is frequent.
- **Keep keyboard actions immediate.** Preserve focus and use brief preference-respecting feedback only when useful.
- **Don't add looping attention-seeking motion.** No pulsing dots, glowing status rings, breathing CTAs, throbbing indicators, or any looped scale/opacity pulse to draw the eye. They age badly, harm accessibility, and rarely serve the user. Use static treatment by default; a justified accessible status or approved expressive design can warrant a controlled pulse without requiring that exact word from the user.

## Wrong defaults

- **Avoid unintentional large scale entrances.** A 0.9+ start is restrained; deliberate emergence may use another range when the brief and access support it.
- **Choose easing deliberately.** Built-in easing, a custom curve or spring can be correct; evaluate the resulting continuity and feel.
- **Don't give enter and exit equal weight.** Exits should be subtler — smaller translate, the user's attention is already moving on.
- **Don't use one duration for everything.** Smaller elements animate faster. Match duration to element size and context.
- **Don't ignore `transform-origin`.** Dropdowns, popovers, and tooltips should expand from their trigger, not from center.

## Performance failures

- **Avoid unmeasured layout animation.** Prefer transform/opacity; bounded size animation and layout/FLIP can be appropriate when measured and needed for content flow.
- **Don't sprinkle `will-change` everywhere.** It's a targeted hint for elements about to animate, not a global fix.
- **Test interruptibility.** Plain CSS keyframes do not automatically retarget smoothly. Use state-driven transitions or an animation API that preserves the required continuity during rapid retriggering.

## Accessibility omissions

- **Don't ship motion without `prefers-reduced-motion`.** Every animation you generate needs a reduced-motion path. This is not optional and not a follow-up — include it in the same code.
- **Don't use vestibular triggers casually.** Large-scale zoom, spin, and parallax can cause genuine discomfort. Avoid unless the design explicitly calls for it, and gate them behind reduced-motion.

## Context blindness

- **Don't apply one designer's rules universally.** Emil's sub-300ms restraint is wrong for a kids' app; Jhey's elastic playfulness is wrong for a banking dashboard. Use the user direction and available context to choose weighting without ceremonial confirmation.
- **Don't ignore the existing codebase.** If the project already animates with 500ms springs, a new 150ms ease-out component will feel foreign. Match established conventions unless they are the thing being fixed.
