# Structural evidence record schema

Each required field is a typed record: `{"status":"pass","evidence":[{"kind":"note","value":"Concrete check, result and scope"}]}`. Evidence kinds: `note`, `file`, `url`, `command`; values must be nonblank strings. Evidence paths are references only: this checker does not open or certify them. Before claiming file-backed proof, check existence and inspect contents within already authorized source roots; apply exclusions and symlink boundaries first.

Statuses: `pass`, `fail`, `untested`, `not-applicable`, `observed`, `inferred`. Fail, untested, N/A and inferred need a nonblank `rationale`. Pass/observed/inferred need nonempty evidence. A failed finding can contain a truthful negative test result. N/A has an empty evidence list if appropriate and describes why the requirement does not apply; it is never counted as a pass. Use observed/inferred for research rather than implying a runtime test.

`--require-passed` rejects declared fail, untested or inferred records; even a successful invocation only establishes structure. JSON cannot establish the truth of its own claims, rendered inspection or production certification.

Required fields: `classification`, `scope`, `exclusions`, `repository`, `release_id`, `environments`, `ownership`, `secrets_owner`, `content_owner`, `analytics_consent_owner`, `qa_evidence`, `monitoring`, `backup_restore`, `rollback`, `licenses`, `support`, `unresolved_risks`, `untested`, `domain_dns_owner`, `forms_owner`.

Fields permitting a truthful empty list: `unresolved_risks`, `untested`. Other fields require the record envelope. This explicitly replaces the earlier presence-only format; migrate old records rather than treating legacy strings/booleans as verified evidence.

## Version and compatibility

New manifests use `{"schema_version":2,"skill":"final-client-handoff","records":{...}}`. Each record additionally includes `applicable: true` for applicable work or `false` for justified `not-applicable`; `null` is allowed only with `untested` while applicability is unknown. Existing unversioned typed records remain accepted as explicitly labeled compatibility input, not inferred legacy truth.

To preserve an old presence-only manifest, run the helper with `<old.json> --migrate-legacy --dry-run` to inspect the conversion or `<old.json> --migrate-legacy --output <new.json>` to create a new file exclusively. The source and an existing destination are never overwritten. The v2 envelope retains the entire original object and source SHA-256 under `legacy_source`, plus each required field's original value. Every migrated requirement is `untested` with unknown applicability; no string, list, false boolean, or other old truthy value is converted to `pass`. Review actual evidence before adopting a status. Migration success describes file creation only; validation of a migrated manifest with unresolved records returns non-pass. Dry-run output is a preview, not saved evidence.
