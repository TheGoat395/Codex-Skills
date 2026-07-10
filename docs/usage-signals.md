# Usage Signals

This document explains which public actions help future users and reviewers understand whether the project is useful.

## Most Useful Public Signals

| Signal | Why It Matters |
|---|---|
| Clone the repository | Shows direct interest in inspecting or installing the project. |
| Download the latest release | Shows interest in the packaged public release artifact. |
| Open a Showcase issue | Adds visible proof that the skills were used on a real workflow. |
| Open a Skill Request issue | Shows demand for a specific capability or workflow gap. |
| Open a Bug Report issue | Helps improve installer, docs, safety, or skill behavior. |
| Submit a benchmark PR | Adds controlled evidence of value. |
| Submit a focused improvement PR | Shows community contribution beyond passive interest. |
| Submit an adapter improvement | Shows the library is useful beyond one agent environment. |

## Clone-Based Install

```bash
git clone https://github.com/TheGoat395/Codex-Skills.git
cd Codex-Skills
python3 scripts/install_skills.py --dry-run
python3 scripts/install_skills.py
```

## Release-Based Install

Download the latest release archive:

```text
https://github.com/TheGoat395/Codex-Skills/releases/latest
```

Extract it, then run:

```bash
python3 scripts/install_skills.py --dry-run
python3 scripts/install_skills.py
```

## Showcase Submission

Use the Showcase issue template when a workflow produces a useful result. Include:

- project type
- skills or collections used
- what changed
- screenshots, links, or local preview notes
- any limitations or follow-up work

## Benchmark Submission

For stronger evidence, submit a benchmark using `examples/benchmarks/measured-premium-website-template/`.

Useful benchmark submissions include:

- same prompt for baseline and skill-assisted runs
- saved baseline output
- saved skill-assisted output
- screenshots or recordings
- build/lint/test/browser QA notes
- scoring table from `BENCHMARKS.md`
- honest limitations

## GitHub Analytics Snapshot

This is an owner-only GitHub Insights snapshot recorded on 2026-07-10. It is a dated observation, not a lifetime guarantee.

### Public Repository Surface

| Metric | Value |
|---|---:|
| Public skills | 70 |
| Curated collections | 8 |
| Showcase demos | 9 demos plus 9 demo archives |
| Stars | 104 |
| Public forks | 46 |
| Network count | 46 |
| Subscribers | 0 |
| Open issues | 0 |
| Pull requests | 1 total, merged |
| Contributors | 1 GitHub contributor |
| Commits | 61 |
| Releases | 3: `v0.1.0`, `v0.1.1`, `v0.1.2` |
| Release asset downloads | 7 total: 6, 1, and 0 |
| License | MIT |
| Topics | 15 |

### Traffic, June 26-July 9

| Metric | Value |
|---|---:|
| Clones | 796 |
| Unique cloners | 119 |
| Views | 111 |
| Unique visitors | 49 |

Daily clone events were `17, 17, 8, 7, 25, 182, 136, 77, 47, 32, 150, 6, 10, 82` across the 14-day window. Daily unique cloners were `4, 2, 3, 1, 5, 36, 31, 13, 14, 11, 11, 6, 7, 4`. Referrers were GitHub: 79 views / 37 unique, Yandex: 6 / 1, and Perplexity: 1 / 1.

The native dashboard does not expose a lifetime clone total. Adding the non-overlapping June 21-July 4 window (1,018 clone events) to July 5-9 (280) gives an approximate 1,298 clone events since the repository launch. This is a derived clone-event estimate, not 1,298 unique people. The available windows support an upper bound of about 308 distinct cloner observations, not a claim of more than 400 unique cloners.

### Activity and Automation

| Dashboard | Snapshot |
|---|---|
| Actions runs | 10 total, 10 successful, 0 failed |
| Actions usage | 10 minutes, 10 job runs, one job per run |
| Actions performance | 6s average runtime, 2s average queue, 0% failure rate |
| Pulse, July 3-July 10 | 1 commit, 1 release, 14 files changed, 486 additions, 2 deletions |
| Active work in Pulse window | 0 active PRs, 0 active issues, 0 new/closed issues |
| Contributors dashboard | 61 commits, 65,798 additions, 49,903 deletions |
| Weekly commit activity | 49 commits in week of June 21, 12 in week of June 28, 0 in week of July 5 |
| Code frequency | June 21: +64,367/-480; June 28: +1,431/-49,423; July 5: 0/0 |

### Security and Dependency Baseline

At the time of the snapshot, the security policy and advisories were enabled, the dependency graph was enabled with two Actions dependencies, Discussions were disabled, Dependabot alerts were disabled, private vulnerability reporting was disabled, secret scanning was disabled, and code scanning still needed setup. Discussions remain intentionally disabled because they are not required for the current contribution flow.

## Adapter Feedback

Users of Claude Code, Cursor, and Gemini CLI can help by opening issues or PRs with:

- which adapter they used
- what project type they tested it on
- what worked clearly
- what wording was confusing
- what tool-specific setup should be improved
