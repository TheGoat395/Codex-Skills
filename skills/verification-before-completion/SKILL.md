---
name: verification-before-completion
description: Verify the evidence needed for a completion, fix, or passing claim before reporting it. Use the smallest fresh check that is decisive for the actual consequence; state exact coverage and limitations instead of running every possible test.
---

# Verification Before Completion

## Core principle

Evidence before claims. Verification should be fresh, decisive, and proportionate to the result being asserted.

## Lightweight gate

Before claiming that work is complete, fixed, passing, deployed, sent, published, or otherwise in a verified state:

1. Name the exact claim and its consequence.
2. Choose the smallest fresh check that can actually prove it.
3. Run the check and read the exit status, failures, and material output.
4. Report the result with exact coverage and anything not verified.

Do not replace a required runtime check with source inspection, a build with lint, or end-to-end evidence with an agent's success message. Do not run an entire test universe when a targeted regression plus the repository's required gate proves the claim.

## Match evidence to the claim

| Claim | Decisive evidence |
|---|---|
| Targeted bug fixed | Reproduce the original symptom or run its regression test |
| Tests pass | The named test command exits successfully with zero relevant failures |
| Build succeeds | The actual build command exits successfully |
| Visual issue fixed | Inspect the rendered affected state at relevant viewports |
| Requirements met | Check each material acceptance criterion against code, output, or runtime evidence |
| External state changed | Read back the exact account, message, deployment, or service state |
| Research complete | State sources searched, semantic coverage, exclusions, and unresolved limits |

## Coverage language

Use precise labels such as:

- source-inspected;
- structurally verified;
- targeted test passed;
- runtime-tested;
- visually inspected;
- external state confirmed;
- untested or blocked.

Never imply whole-system certification from a sample. Previous evidence may provide context, but a current completion claim needs current verification when the state could have changed.

## Delegated work

A subagent report is evidence about what the subagent observed, not automatic proof of completion. Inspect the relevant diff or artifact and run the smallest decisive verification before adopting its claim.

## Stop condition

Stop when the acceptance criteria are supported at the required confidence. Record residual limitations instead of adding ceremonial checks that cannot change the decision.
