# Workflow: Audit Mode

Review existing motion design and report evidence-weighted findings using relevant interpretive lenses. Reconnaissance first, then a full audit, then a structured report. Never apply rules blindly.

## Required Reading

Read as you reach each step (not all upfront):
1. `references/audit-checklist.md` — your systematic guide (STEP 2)
2. The weighted designer file(s) — `emil-kowalski.md`, `jakub-krehel.md`, `jhey-tompkins.md` (STEP 2)
3. `references/accessibility.md` — mandatory every audit (STEP 2)
4. `references/anti-checklist.md` — the quality gate: AI-generated motion anti-pattern categories and motion issues to flag (STEP 2)
5. `references/output-format.md` — the report template, HTML mode + terminal mode (STEP 3)
6. `references/demo-shell.html` — the demo-card template for HTML-mode per-finding demos (STEP 3)

---

## STEP 1: Context Reconnaissance (DO THIS FIRST)

Before auditing any code, understand the project context.

### Gather Context

Check these sources:
1. **Applicable AGENTS.md/project guidance (CLAUDE.md only when applicable)** — Any explicit context about the project's purpose or design intent
2. **package.json** — What type of app? (Next.js marketing site vs Electron productivity app vs mobile PWA)
3. **Existing animations** — Search for `motion`, `animate`, `transition`, `@keyframes`. What durations are used? What patterns exist?
4. **Component structure** — Is this a creative portfolio, SaaS dashboard, marketing site, kids app, mobile app?

### Motion Gap Analysis (CRITICAL - Don't Skip)

After finding existing animations, search for state transitions as candidates. An instant state is not automatically defective; first assess intent, frequency, focus, reduced-motion behavior and observed comprehension.

**Search for conditional renders without AnimatePresence:**
```bash
# Find conditional renders: {condition && <Component />}
rg -n '&&' <affected-source-path> -g '*.tsx' -g '*.jsx'

# Find ternary UI swaps: {condition ? <A /> : <B />}
rg -n '\?\s*<' <affected-source-path> -g '*.tsx' -g '*.jsx'
```

**For each conditional render found, check:**
- Is it wrapped in `<AnimatePresence>`?
- Does the component inside have enter/exit animations?
- If NO to both, inspect the actual transition; report a finding only when missing feedback/continuity causes an observed problem. Instant, opacity-only and other implementations may be correct.

**Common motion gap patterns:**
- `{isOpen && <Modal />}` — Modal appears/disappears instantly
- `{mode === "a" && <ControlsA />}` — Controls swap without transition
- `{isLoading ? <Spinner /> : <Content />}` — Loading state snaps
- `style={{ height: isExpanded ? 200 : 0 }}` — Height changes without CSS transition
- Inline styles with dynamic values but no `transition` property

**Where to look for motion gaps:**
- Inspector/settings panels with mode switches
- Conditional form fields
- Tab content areas
- Expandable/collapsible sections
- Toast/notification systems
- Loading states
- Error states

### State Your Inference

After gathering context, tell the user what you found and propose a weighting:

```
## Reconnaissance Complete

**Project type**: [What you inferred — e.g., "Kids educational app, mobile-first PWA"]
**Existing animation style**: [What you observed — e.g., "Spring animations (500-600ms), framer-motion, active:scale patterns"]
**Likely intent**: [Your inference — e.g., "Delight and engagement for young children"]

**Transition candidates**: [Number] conditional renders; [Number] demonstrated findings
- [List the files/areas with gaps, e.g., "Settings panel mode switches", "Loading states"]

**Proposed perspective weighting**:
- **Primary**: [Designer] — [Why]
- **Secondary**: [Designer] — [Why]
- **Selective**: [Designer] — [When applicable]

State material weighting assumptions and continue with the authorized audit.
```

Use the Context-to-Perspective Mapping table in SKILL.md to propose the weighting.

### Proceed with available context

Use explicit user direction, established conventions and the observed interface. Infer reversible weighting and proceed; ask only when a consequential unresolved choice actually blocks a correct result. Do not require confirmation of designer weights or task verbs.

---

## STEP 2: Scoped Audit

Apply the following procedures to the requested surface. Preserve full useful coverage for a substantial audit; for a narrow review load only applicable lens and topic details.

### 2a. Read the Audit Checklist First
**Read `references/audit-checklist.md`** — Use this as your systematic guide. It provides the structured checklist of what to evaluate.

### 2b. Read Designer Files for Your Weighted Perspectives
Based on your context weighting, read the relevant designer files:
- **Read `references/emil-kowalski.md`** if Emil is primary/secondary — Restraint philosophy, frequency rules, decision frameworks
- **Read `references/jakub-krehel.md`** if Jakub is primary/secondary — Production polish philosophy, what to check
- **Read `references/jhey-tompkins.md`** if Jhey is primary/secondary — Playful experimentation philosophy, opportunities to surface

### 2c. Read Topical References as Needed
- **Read `references/accessibility.md`** — MANDATORY. Always check for prefers-reduced-motion. No exceptions.
- **Read `references/anti-checklist.md`** — Apply this as the audit's quality gate. AI-generated motion anti-pattern categories at the top (pulsing indicators, hover-scale-on-everything, stagger-spam, etc.) identify candidates; report findings only after checking purpose and observed consequence. Perspective-specific and general anti-patterns sit below. Each category includes a frequency heuristic so single intentional uses don't trip the gate.
- **Read `references/performance.md`** — If you see complex animations, check for GPU optimization issues
- **Read `references/motion-cookbook.md`** — Reference when making specific implementation recommendations (the recommended fix code, including the per-finding demo motion in HTML mode)

---

## STEP 3: Output Format (inline by default)

Default to prioritized inline findings with evidence location, observed consequence, recommended fix, relevant lens reasoning, working-well observations and untested limits. A rich self-contained HTML report is optional for a requested/substantial visual deliverable. Read `references/output-format.md` and the demo shell only for that mode.

### Optional rich report — preserve the full procedure when this deliverable applies

1. **Resolve the write location.** The file is written to `motion-audits/{project-name}-{UTC-timestamp}-{unique-suffix}.html` in the audited project's root.
   - **Audited project root**: run `git rev-parse --show-toplevel` from the agent's cwd. If it succeeds, use that path. If it fails (no `.git` ancestor), use cwd.
   - **`{project-name}`**: the `name` field from `package.json` at the project root if it exists; else the `name` field from `pyproject.toml`; else the basename of the project root. Strip any scoping prefix (`@scope/pkg` → `pkg`) and sanitize to lowercase kebab-case (`[a-z0-9-]`, replace others with `-`).
   - **`{UTC-timestamp}-{unique-suffix}`**: UTC timestamp plus a random suffix; use exclusive file creation and never overwrite a prior report.
   - Example: `<project-root>/motion-audits/my-app-2026-05-20.html`.
   - Do not modify `.gitignore`. The user sees `motion-audits/` in `git status` and decides whether to ignore it.

2. **Read `references/demo-shell.html`** and use it as the template for each demo card. Embed one card per Critical + Important finding (Opportunities do not get demo cards). Use the suffixed-naming contract — `@keyframes m{n}` and `.demo-{n}__mt`, `{n}` = the finding's 1-indexed position across the whole report — so multiple findings don't collide on CSS names.

3. **Generate per-finding motion code** by reading the audited code, the relevant lens reference, and `references/motion-cookbook.md` for the recipe. Demonstrate the labeled active duration exactly: in a 3000ms replay cycle the endpoint percentage is `duration_ms / 3000 * 100`, followed by a hold. Label any deliberately slowed demonstration. Provide pause/replay and visible focus. The `@keyframes` 100% state must match the motion-target's default static rendering so the shell's `prefers-reduced-motion` guard shows the correct final visual.

4. **Write the file.** Create the output directory if needed. Write the complete document using exclusive creation; preserve all earlier reports.

5. **Open in the default browser** via OS-detected Bash dispatch:

   ```bash
   path="<absolute path to the HTML file>"
   if [ -n "$WSL_DISTRO_NAME" ] || grep -qi microsoft /proc/version 2>/dev/null; then
     win_path=$(wslpath -w "$path")
     cmd.exe /c start "" "$win_path" 2>/dev/null
   else
     case "$(uname -s)" in
       Darwin)               open "$path" ;;
       Linux)                xdg-open "$path" ;;
       MINGW*|MSYS*|CYGWIN*) start "" "$path" ;;
       *)                    echo "Unknown platform — open this file manually: $path" ;;
     esac
   fi
   ```

   If the open command returns non-zero or the platform is unrecognized, print `Open this file in your browser: {absolute path}` and continue. Never abort the audit because of a failed browser-open.

6. **Print the 3-line terminal summary:**

   ```
   🎬 Motion audit complete — 🔴 {N} Critical · 🟡 {N} Important · 🟢 {N} Opportunities
   📄 Report: {absolute path}
   💡 Want the full report inline instead? Re-run with --terminal or say "show inline".
   ```

### Inline mode and output preferences

Inline is the default. When the user signals terminal mode (`--terminal` / `--inline` / `--no-html` flag, or "show the full report inline" / "skip the HTML" / "terminal only"), **skip the HTML write and the browser-open** and render the decorated-markdown report inline per `references/output-format.md` terminal mode. Do not print the 3-line summary in this case.

Match output depth to the task. Preserve distinct findings, rationale and useful lens interpretation; avoid duplicate findings and mandatory bulky output for small reviews.

---

## Agent Gotchas (Self-Check Before Writing the Report)

Common failure modes during HTML report generation. Most break silently or only manifest when a second finding lands in the same report.

- **Don't reuse keyframe or class names across findings.** Each demo uses `@keyframes m{n}` and `.demo-{n}__mt` where `{n}` is the 1-indexed position across the WHOLE report. Duplicate names mean the second finding shadows the first and the first demo breaks silently.
- **Don't redefine the shell's CSS variables.** Per-finding code uses stage tokens `var(--st-bg)`, `var(--st-fg)`, `var(--st-line)`, `var(--st-dim)` and shared font tokens. Hard-coding colors or fonts breaks dark mode and typography consistency.
- **Don't write per-finding overrides inside the `prefers-reduced-motion` block.** The shell's guard collapses all `[class*="__mt"]` animations. Make the `@keyframes` 100% state match the motion-target's default static rendering instead.
- **Don't include demo cards for Opportunities.** Demos are reserved for Critical and Important. Surface Opportunities in text only.
- **Don't animate the report itself.** No entrance, scroll, or mount animations on the report chrome — only the demo cards animate. Animating the report reproduces the AI-generated motion anti-patterns the audit exists to catch.
- **Don't write to cwd if `git rev-parse --show-toplevel` succeeds.** The report goes to `{project-root}/motion-audits/`. Only fall back to cwd when git returns nonzero.
- **Don't abort the audit if browser-open fails.** A non-zero exit code is a "no default handler" condition, not an error. Print the path and continue.
- **Don't modify `.gitignore`.** The skill never touches it. The user adds `motion-audits/` themselves if they want.
- **Preserve useful lens reasoning without duplicating findings.** A rich report can retain full per-lens sections; a small inline audit should stay proportionate.

---

## Success Criteria

- [ ] Context gathered (CLAUDE.md, package.json, existing animations, structure)
- [ ] Transition candidates inspected; missing-animation findings require observed consequences
- [ ] Weighting follows user direction or a stated context-supported inference
- [ ] Audit checklist worked through systematically
- [ ] Anti-checklist applied — AI-generated motion anti-pattern categories checked against the codebase
- [ ] Accessibility checked — prefers-reduced-motion verified (mandatory)
- [ ] Inline result delivered, or requested rich report written without overwrite and inspected
- [ ] Report depth matches scope; optional rich demos have truthful timing, pause/replay, visible focus and reduced-motion states
