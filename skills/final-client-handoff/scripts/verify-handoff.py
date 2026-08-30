#!/usr/bin/env python3
import json,sys
required=['classification','scope','exclusions','repository','release_id','environments','ownership','secrets_owner','content_owner','analytics_consent_owner','qa_evidence','monitoring','backup_restore','rollback','licenses','support','unresolved_risks','untested']
if len(sys.argv)!=2: print('Usage: verify-handoff.py <handoff.json>');raise SystemExit(2)
data=json.load(open(sys.argv[1]));missing=[x for x in required if x not in data or data[x] in ['',None]]
if missing: print('FAIL missing: '+', '.join(missing));raise SystemExit(1)
print(f'PASS handoff: {len(required)}/{len(required)} fields')
