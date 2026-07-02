# Measured Benchmark Template: Premium Website Workflow

This template is for a controlled baseline-vs-skill-assisted benchmark. It is intentionally empty of results until a real run is completed.

## Status

- Type: measured benchmark template
- Result status: pending measured run
- Evidence level: scaffold only

## Test Prompt

```text
Create a polished local website, landing page, hero section, or portfolio from the same prompt, reference, spec, or rough direction in both runs.
```

Record the exact prompt here before running the benchmark.

## Baseline Run

Run Codex without installing or invoking this skill library.

Record:

- date
- model/environment
- prompt used
- project files generated or changed
- screenshots or recording path
- commands run
- build/lint/test/browser QA notes
- known issues

## Skill-Assisted Run

Run the same task using the selected Codex Premium Website Skills collection.

Recommended starting collection:

```bash
python3 scripts/install_skills.py --collection taste-and-build-gates
```

Record:

- date
- model/environment
- selected collection or skills
- prompt used
- project files generated or changed
- screenshots or recording path
- commands run
- build/lint/test/browser QA notes
- known issues

## Scoring Table

Use the rubric in `BENCHMARKS.md`.

| Category | Baseline Score | Skill-Assisted Score | Notes |
|---|---:|---:|---|
| Visual direction | TBD | TBD | TBD |
| Content quality | TBD | TBD | TBD |
| Frontend implementation | TBD | TBD | TBD |
| Motion and interaction | TBD | TBD | TBD |
| Accessibility | TBD | TBD | TBD |
| QA and handoff | TBD | TBD | TBD |

## Evidence Checklist

- [ ] Same prompt used for both runs
- [ ] Baseline output saved
- [ ] Skill-assisted output saved
- [ ] Desktop screenshot saved
- [ ] Mobile screenshot saved
- [ ] Build/lint/test output recorded when available
- [ ] Browser QA notes recorded when frontend output is involved
- [ ] Accessibility notes recorded
- [ ] Known limitations documented

## Honest Limitations

Document anything that could affect comparison quality:

- different model version
- different starting repo state
- manual edits between runs
- missing screenshots
- failed commands
- unverified browser behavior
- subjective scoring calls

## Summary

Write the final comparison only after the measured run exists. Do not replace this section with projected results.
