# Examples

This directory is for reproducible examples and benchmark artifacts.

Recommended structure:

```text
examples/
  product-site-benchmark/
    README.md
    prompt.md
    baseline/
    skill-assisted/
    screenshots/
    logs/
```

Each example should include enough context for another maintainer to understand:

- the task prompt
- which collection or skills were used
- what changed compared with a baseline run
- build, lint, test, accessibility, and browser QA output
- screenshots for desktop and mobile when frontend output is involved

Do not include private client code, private assets, credentials, or paid/private reference material.
