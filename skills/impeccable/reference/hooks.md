# $impeccable hooks

Manage the **design detector hook** for the current project.

The hook runs the Impeccable design detector on direct file edits to design-relevant files (`.tsx`, `.jsx`, `.html`, `.vue`, `.svelte`, `.astro`, `.css`, `.scss`, `.sass`, `.less`, `.ts`, `.js`). In Codex, the hook uses `.codex/hooks.json` and pushes a short system reminder into the agent's context after an edit. Findings get a correction prompt, pending issues get a re-nudge, and clean UI-ish files get a short acknowledgement unless quiet mode is on (`hook.quiet` in config). Plain `.ts` and `.js` files are still scanned, but stay quiet unless the detector finds something.

This command toggles the hook **per project** by editing `.impeccable/config.json` (the unified Impeccable config; hook runtime settings live under its `hook` key, and shared detector ignores live under `detector`). Per-developer overrides, including the install consent decision (`hook.consent`) the CLI records, live in the gitignored `.impeccable/config.local.json`. Set `hook.enabled: false` to turn the hook off, `hook.quiet: true` to silence the clean/pending acknowledgements, or `hook.auditLog` to a file path for an NDJSON log. The legacy `IMPECCABLE_HOOK_DISABLED`, `IMPECCABLE_HOOK_QUIET`, and `IMPECCABLE_HOOK_LOG` env vars are still honored and override these config values when set.

Manual detector scans use the same project filter config by default: `detector.ignoreRules`, `detector.ignoreFiles`, `detector.ignoreValues`, and `detector.designSystem.enabled`. `hook.enabled` only controls automatic hook execution, not manual CLI scans. Use the bundled detector script for local scans and use the hook admin script for direct CLI CRUD on the same detector ignores.

Supported public-core harness: Codex, through `.codex/hooks.json` in the project. The underlying Impeccable tooling may contain adapter code for other local harnesses, but this public release documents and supports the Codex path.

## Routing

The first argument is the action. Defaults to `status`.

| Action | What it does |
|---|---|
| `status` | Print current state, shared/local config paths, ignored rules / files / values, env override. |
| `on` | Set `enabled: true` in `.impeccable/config.json`, record local hook consent as accepted, and install/repair the Codex hook manifest when the skill is installed. |
| `off` | Set `enabled: false` in `.impeccable/config.json`. |
| `ignore-rule <id>` | Append `<id>` to `detector.ignoreRules`; for `overused-font`, requires `--all-values`. |
| `ignore-file <glob>` | Append `<glob>` to `detector.ignoreFiles`. |
| `ignore-value <id> <value> [--shared] [--reason "..."]` | Append a rule/value suppression to shared `.impeccable/config.json`. |
| `ignore-value <id> <value> --local [--reason "..."]` | Append a private rule/value suppression to `.impeccable/config.local.json`. |
| `reset` | Delete the project config, dedup cache, and pending hook queue. |

## Flow

1. Resolve the action from the user's argument. If no action was given, default to `status`.
2. Invoke the admin script and pass the user's output through verbatim:

   ```bash
   node ~/.codex/skills/impeccable/scripts/hook-admin.mjs <action> [args...]
   ```

3. If `<action>` is `off`, follow up with a one-line note: "Done. New edits will not trigger the design hook in this project until you run `$impeccable hooks on`."
4. If `<action>` is `on`, follow up with: "Done. The design hook will fire after the next Edit/Write/MultiEdit on a UI file."
5. If `<action>` is `ignore-value`, `ignore-file`, or `ignore-rule`, just print the script output. The default scope is shared `.impeccable/config.json`; add `--local` only when the user explicitly asks for a private exception.
6. If `<action>` is `status`, just print the script output. Do not add commentary unless the user asked a follow-up question.

## Intentional findings

The hook itself never writes ignore config. Persist an exception only after the user explicitly confirms the flagged issue is intentional, and always go through `hook-admin.mjs`.

Prefer the narrowest exception:

- If the finding line shows an exact `ignore-value` command, run that command. This writes shared `.impeccable/config.json` by default.
- For value-specific findings such as `overused-font` and `bounce-easing`, use `ignore-value` when the user confirms the specific value. Do not use `ignore-rule overused-font` for a specific font.
- If the finding has no value-specific command, such as `side-tab`, prefer `ignore-file <path>` for the current file.
- Use `ignore-rule <id>` only when the user asks to suppress that whole rule across the project. For broad overused-font suppression, use `ignore-rule overused-font --all-values` only when the user asks to ignore overused fonts generally.
- Do not add source comments such as `impeccable: ignore`; inline comments pollute code and are not a supported suppression mechanism.

Example value-specific exception:

```bash
node ~/.codex/skills/impeccable/scripts/hook-admin.mjs ignore-value overused-font Inter --shared --reason "User confirmed Inter is intentional"
```

Example intentional motion exception:

```bash
node ~/.codex/skills/impeccable/scripts/hook-admin.mjs ignore-value bounce-easing bounce-ball --shared --reason "User confirmed ball bounce animation is intentional"
```

Example whole-rule font exception:

```bash
node ~/.codex/skills/impeccable/scripts/hook-admin.mjs ignore-rule overused-font --all-values --reason "User asked to ignore overused fonts generally"
```

Example file-scoped exception:

```bash
node ~/.codex/skills/impeccable/scripts/hook-admin.mjs ignore-file "src/legacy/Card.tsx"
```

## Constraints

- Never modify `.impeccable/config.json` or `.impeccable/config.local.json` by hand from this command. Always go through `hook-admin.mjs` so writes stay validated and the file shape stays consistent.
- Do not edit the hook scripts themselves (`hook.mjs`, `hook-lib.mjs`, `hook-before-edit.mjs`) from this flow. Those are skill plumbing.
- Codex hook behavior is post-edit: it surfaces detector findings as reminders instead of silently rewriting user code.
- The hook is bundled with the Impeccable skill and installed through the project-local `.codex/hooks.json` manifest. In Codex, the user must approve the hook via `/hooks` the first time.

## Failure modes

- If `.impeccable/config.json` or `.impeccable/config.local.json` is unreadable or malformed, the hook ignores that file and uses the remaining valid config/defaults. `hook-admin.mjs status` will show malformed files as ignored.
- If the user asks to "disable the hook" globally, lead with `$impeccable hooks off` (persistent for this project; writes `hook.enabled: false` to config). The legacy `IMPECCABLE_HOOK_DISABLED=1` env var also works as a one-shot override that follows the shell.
