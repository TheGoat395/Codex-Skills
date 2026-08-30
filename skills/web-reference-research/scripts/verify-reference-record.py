#!/usr/bin/env python3
import json,sys
required=['source_url','creator','observed_on','evidence','sampled_states','hierarchy','palette','typography','layout','motion_phases','input_behavior','responsive_evidence','reduced_motion','technical_inference','confidence','performance_risk','clean_room_brief','originality_delta','unavailable_evidence']
if len(sys.argv)!=2: print('Usage: verify-reference-record.py <record.json>');raise SystemExit(2)
data=json.load(open(sys.argv[1]));missing=[x for x in required if x not in data or data[x] in ['',None,[],{}]]
if missing: print('FAIL missing: '+', '.join(missing));raise SystemExit(1)
print(f'PASS reference record: {len(required)}/{len(required)} fields')
