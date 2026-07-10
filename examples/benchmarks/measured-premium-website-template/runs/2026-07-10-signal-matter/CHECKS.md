# Signal / Matter Checks

## Matched Controls

- Same fixed prompt for both conditions.
- Same Codex CLI version and `gpt-5.6-luna` model.
- Empty output directories before each run.
- Exactly three deliverable files per condition.
- Baseline used an isolated `CODEX_HOME` without installed skills.
- Skill-assisted run could read this repository's public skill source.

## Static Checks

- `node --check script.js` passed for both outputs.
- Required project names, sections, controls, and project entries are present.
- No external URL, package, font, image, video, API, or network dependency is used.
- No testimonials, customer logos, awards, adoption statistics, or business metrics are present.

## Browser Checks

Automated Chromium checks ran at:

- 1440x1000
- 1280x900
- 900x1100
- 390x844

The paired harness checked console errors, failed requests, horizontal overflow, canvas pixel diversity, mobile menu state, Escape closing, motion-toggle state, reduced-motion visibility, and first-viewport section cues. Results are saved in [`qa/results.json`](qa/results.json).

## Human Visual Review

Desktop and mobile screenshots were inspected for composition, typography, hierarchy, clipping, overlap, project differentiation, visual-field quality, and next-section visibility. Four final viewport screenshots are checked in under [`screenshots/`](screenshots/).
