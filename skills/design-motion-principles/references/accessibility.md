# Accessibility

**This is not optional.** Motion can cause discomfort, nausea, or distraction for many users.

---

## Respect User Preferences

```css
/* Base state is complete. Adapt these selectors to the owning component. */
.motion-reveal { opacity: 1; transform: none; filter: none; }
.motion-panel[data-state="closed"] { display: none; }
.motion-panel[data-state="open"] { display: block; }

@media (prefers-reduced-motion: no-preference) {
  .motion-reveal { animation: motion-enter 180ms ease-out both; }
  @keyframes motion-enter {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: none; }
  }
}
@media (prefers-reduced-motion: reduce) {
  .motion-reveal {
    animation: none !important; /* resets delay as well as duration */
    transition: none !important;
    opacity: 1; transform: none; filter: none;
  }
  :root { scroll-behavior: auto; }
}
```

**What this does**: Keeps the reveal's settled state and the panel's functional open/closed state independent of motion. A global `0.01ms` duration reset cannot infer final states, clear every delay, or safely complete animation-event-driven application logic. Do not use it as proof of reduced-motion support. State, focus, announcements and action completion must come from application logic, not solely `animationend`/`transitionend`. Apply equivalent settled-state rules to each affected component and test delayed/looping/pinned/media paths as appropriate.

---

## Functional vs. Decorative Motion

| Type | Purpose | Reduced Motion Behavior |
|------|---------|------------------------|
| **Functional** | Indicates state changes, spatial relationships, orientation | May need alternative (instant state change, no transition) |
| **Decorative** | Pure delight, visual interest | Can be fully removed |

**The test**: Does removing this animation break the user's ability to understand what happened? If yes, it's functional.

---

## Motion Sensitivity Considerations

- Avoid large-scale motion (full-screen transitions, parallax)
- Avoid continuous or looping animations that can't be paused
- Provide pause controls for any ambient animation
- Be especially careful with vestibular triggers: zooming, spinning, parallax

---

## Implementation Checklist

- [ ] Tested with `prefers-reduced-motion: reduce` enabled
- [ ] No vestibular triggers (excessive zoom, spin, parallax)
- [ ] Looping animations can be paused
- [ ] Functional animations have non-motion alternatives
- [ ] Users can complete all tasks with animations disabled
