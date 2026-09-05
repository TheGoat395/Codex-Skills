#!/usr/bin/env python3
"""Versioned documentary evidence checks and recoverable legacy migration; no external truth claim."""
import argparse
import hashlib
import json
import os
import tempfile
import sys
from pathlib import Path
REQUIRED = ['source_url', 'creator', 'observed_on', 'evidence', 'sampled_states', 'hierarchy', 'palette', 'typography', 'layout', 'motion_phases', 'input_behavior', 'responsive_evidence', 'reduced_motion', 'technical_inference', 'confidence', 'performance_risk', 'clean_room_brief', 'originality_delta', 'unavailable_evidence']
EMPTY_LISTS = ['unavailable_evidence']
SKILL = 'web-reference-research'
STATUSES = {'pass', 'fail', 'untested', 'not-applicable', 'observed', 'inferred'}


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def check_record(value, versioned=False):
    if not isinstance(value, dict) or not isinstance(value.get('status'), str) or value['status'] not in STATUSES:
        return False
    status = value['status']
    evidence = value.get('evidence')
    if not isinstance(evidence, list):
        return False
    if status in {'pass', 'observed', 'inferred'} and not evidence:
        return False
    if status in {'fail', 'untested', 'not-applicable', 'inferred'} and not nonblank(value.get('rationale')):
        return False
    if versioned:
        if 'applicable' not in value:
            return False
        applicable = value['applicable']
        if applicable is None:
            if status != 'untested':
                return False
        elif not isinstance(applicable, bool) or applicable != (status != 'not-applicable'):
            return False
    for item in evidence:
        if not isinstance(item, dict) or not isinstance(item.get('kind'), str) or item['kind'] not in {'note', 'file', 'url', 'command'} or not nonblank(item.get('value')):
            return False
        if item['kind'] == 'url':
            from urllib.parse import urlparse
            try:
                url = urlparse(item['value'])
                if url.scheme not in {'http', 'https'} or not url.netloc or url.username or url.password:
                    return False
            except ValueError:
                return False
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--require-passed', action='store_true')
    parser.add_argument('--migrate-legacy', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        original_bytes = args.manifest.read_bytes()
        data = json.loads(original_bytes)
    except (OSError, ValueError):
        print('INVALID: unreadable or malformed JSON')
        return 2
    if not isinstance(data, dict):
        print('INVALID: root must be an object')
        return 1
    if args.migrate_legacy:
        if ('schema_version' in data and data['schema_version'] == 2) or args.require_passed:
            print('INVALID: migration accepts legacy input only and never verifies passed status')
            return 2
        if (not args.dry_run and args.output is None) or (args.dry_run and args.output is not None):
            print('INVALID: choose --migrate-legacy --dry-run or --migrate-legacy --output <new-file>')
            return 2
        migrated = {'schema_version': 2, 'skill': SKILL, 'records': {}, 'legacy_source': {
            'format': 'unversioned-legacy', 'sha256': hashlib.sha256(original_bytes).hexdigest(),
            'file': str(args.manifest.absolute()), 'payload': data}}
        for key in REQUIRED:
            migrated['records'][key] = {'status': 'untested', 'applicable': None, 'evidence': [],
                'rationale': 'Legacy content retained without verification; applicability and evidence require review.',
                'legacy_present': key in data, 'legacy_value': data.get(key)}
        if args.dry_run:
            print(json.dumps(migrated, indent=2))
            print('MIGRATION_PREVIEW_ONLY: no writes and no acceptance certification', file=sys.stderr)
            return 0
        temporary = None
        try:
            # Write a complete sibling stage, then publish without clobbering any destination.
            fd, temporary = tempfile.mkstemp(prefix='.evidence-migration-', dir=args.output.parent)
            with os.fdopen(fd, 'w', encoding='utf-8') as output:
                output.write(json.dumps(migrated, indent=2, ensure_ascii=True) + '\n')
                output.flush()
                os.fsync(output.fileno())
            os.link(temporary, args.output)
        except OSError:
            print('INVALID: migration output cannot be published exclusively; input remains unchanged')
            return 1
        finally:
            if temporary is not None:
                Path(temporary).unlink(missing_ok=True)
        print('MIGRATED_UNVERIFIED: ' + str(args.output) + '; source preserved; all converted records require review')
        return 0
    if args.dry_run or args.output:
        print('INVALID: --dry-run/--output require --migrate-legacy')
        return 2
    versioned = 'schema_version' in data
    if versioned:
        if type(data['schema_version']) is not int or data['schema_version'] != 2 or data.get('skill') != SKILL or not isinstance(data.get('records'), dict):
            print('INVALID: expected schema_version 2, matching skill, and records object')
            return 1
        records = data['records']
    else:
        records = data
    bad = [key for key in REQUIRED if not (key in EMPTY_LISTS and records.get(key) == []) and not check_record(records.get(key), versioned)]
    if bad:
        print('INVALID evidence records: ' + ', '.join(bad))
        if not versioned:
            print('Legacy presence-only input needs --migrate-legacy; no old truthy value establishes a pass')
        return 1
    statuses = {key: records[key]['status'] for key in REQUIRED if isinstance(records[key], dict)}
    unresolved = [key for key, status in statuses.items() if status in {'fail', 'untested', 'inferred'}]
    na = [key for key, status in statuses.items() if status == 'not-applicable']
    label = 'V2' if versioned else 'UNVERSIONED_TYPED_COMPATIBILITY'
    if unresolved and (args.require_passed or 'legacy_source' in data):
        print(label + ' STRUCTURALLY_VALID_WITH_UNRESOLVED: ' + ', '.join(unresolved))
        return 1
    print(label + ' STRUCTURALLY_VALID: ' + str(len(REQUIRED)) + ' records; external truth and file existence NOT verified')
    print('Unresolved: ' + (', '.join(unresolved) or 'none declared') + '; N/A (not passes): ' + (', '.join(na) or 'none declared'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
