# Measured Run: Atlas

## Status

- Date: 2026-07-10
- Type: paired repository benchmark
- Task: the fixed Atlas prompt in [`PROMPT.md`](PROMPT.md)
- Repository source commit: `e7d28401d936055a34dbd6c22a54d308a6e99fed`
- Model reported by Codex CLI: `gpt-5.6-luna`
- Output constraint: exactly `index.html`, `styles.css`, and `script.js`
- Network assets: none
- OpenAI evaluation or endorsement: none

## Conditions

The baseline and skill-assisted runs used the same prompt, model family, output directory shape, and file constraint. The baseline had no Codex-Skills source available. The skill-assisted run could read this repository's public-core skill source for frontend direction, implementation, accessibility/performance, and handoff guidance.

## Scores

Scores use the 1-5 rubric in [`BENCHMARKS.md`](../../../../../BENCHMARKS.md). They are a single-run repository review, not a statistically powered study.

| Category | Baseline | Skill-assisted | Change | Evidence note |
|---|---:|---:|---:|---|
| Visual direction | 4/5 | 4/5 | 0 | Both are coherent and distinctive; the assisted run has a more developed editorial/technical system. |
| Content quality | 4/5 | 4/5 | 0 | Both include the requested information architecture and specific Atlas copy. |
| Frontend implementation | 3/5 | 4/5 | +1 | Assisted output has clearer structure, stronger responsive rules, and more explicit state hooks. |
| Motion and interaction | 3/5 | 4/5 | +1 | Both include navigation and copy interactions; assisted output includes Escape handling and more complete states. |
| Accessibility | 3/5 | 4/5 | +1 | Both include focus and reduced-motion support; assisted output adds more labels, landmarks, and live status detail. |
| QA and handoff | 2/5 | 3/5 | +1 | Both passed local checks; assisted output recorded more explicit checks and limitations. |
| **Total** | **19/30** | **23/30** | **+4** | **Skill-assisted result is 76.7% vs 63.3% on this rubric.** |

## Checks

Passed for both outputs:

- `node --check script.js`
- exact three-file output check
- required semantic landmarks and section checks
- three feature-item check
- installation interaction check
- mobile navigation interaction check
- visible focus style check
- reduced-motion support check
- no external URL, import, or network-asset check

The baseline output has two `:root` declarations in `styles.css`; that is recorded as a baseline code-quality limitation rather than edited away. The assisted output has one root token declaration.

## Limitations

- No Playwright or Puppeteer runtime was available, so no rendered desktop/mobile screenshot or browser-console result is claimed.
- The legacy `tidy` binary emits warnings for valid HTML5 and inline SVG elements; it was not used as a pass/fail gate.
- The assisted Atlas console contains fictional values such as `RUN 014` and `03 found` as visual copy for the fictional product. Those values are not benchmark measurements.
- The score is subjective and based on one task, one model run per condition, and source-level inspection.

## Reproduction

Run the same prompt twice with isolated directories. Keep the prompt, model, output constraint, checks, and scoring rubric unchanged. Add rendered browser evidence when the environment supports it.
