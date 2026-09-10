#!/usr/bin/env python3
"""Regression tests for bundled helpers; these do not evaluate model behavior."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'


def load(relative, name):
    spec = importlib.util.spec_from_file_location(name, SKILLS / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


collision = load('agent-evaluation-operations/scripts/analyze_skill_collisions.py', 'collision')
catalog = load('premium-visual-reference-library/scripts/query_catalog.py', 'query_catalog')


class HelperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def invoke(self, script, *args):
        return subprocess.run([sys.executable, str(SKILLS / script), *map(str, args)], capture_output=True, text=True)

    def test_collision_reads_folded_and_quoted_descriptions(self):
        for value in ['>\n  Inspect focus\n  and keyboard access.', '"Inspect focus and keyboard access." # note', "'Inspect focus and keyboard access.'"]:
            with self.subTest(value=value):
                self.assertEqual(collision.frontmatter_value('---\nname: focus\ndescription: '+value+'\n---\n', 'description'), 'Inspect focus and keyboard access.')

    def test_collision_missing_root_is_not_an_empty_success(self):
        result = self.invoke('agent-evaluation-operations/scripts/analyze_skill_collisions.py', '--root', self.root/'absent')
        self.assertNotEqual(result.returncode, 0)

    def test_collision_reports_unassessed_symlink(self):
        source = self.root/'source';source.mkdir();(source/'SKILL.md').write_text('---\nname: test\ndescription: Test description.\n---\n')
        target = self.root/'skills';target.mkdir();(target/'external').symlink_to(source, target_is_directory=True)
        result = self.invoke('agent-evaluation-operations/scripts/analyze_skill_collisions.py', '--root', target, '--json')
        data = json.loads(result.stdout)
        self.assertEqual(data['assessed_skills'], 0)
        self.assertEqual(data['unassessed'], ['external'])

    def test_corpus_rejects_false_float_and_empty_scorer(self):
        script = 'agent-evaluation-operations/scripts/validate_regression_corpus.py'
        original = json.loads((SKILLS/'agent-evaluation-operations/references/regression-corpus.json').read_text())
        self.assertEqual(self.invoke(script).returncode, 0)
        for invalid in (False, 0.0, 1):
            data = copy.deepcopy(original)
            data['cases'][0]['acceptance_threshold']['prohibited_behaviors_allowed'] = invalid
            fixture = self.root/'corpus.json';fixture.write_text(json.dumps(data))
            with self.subTest(invalid=invalid):self.assertNotEqual(self.invoke(script, fixture).returncode, 0)
        data = copy.deepcopy(original);data['scorer_contracts'][data['cases'][0]['scorer']] = {}
        fixture.write_text(json.dumps(data));self.assertNotEqual(self.invoke(script, fixture).returncode, 0)

    def test_catalog_has_all_records_with_matching_provenance(self):
        records = catalog.load_records()
        self.assertEqual(len(records), 192)
        self.assertEqual(len({r['record']['id'] for r in records}), 192)
        self.assertTrue(all(r['provenance']['id']==r['record']['id'] for r in records))

    def test_catalog_search_is_bounded_and_id_preserves_source(self):
        script = 'premium-visual-reference-library/scripts/query_catalog.py'
        result = self.invoke(script, '--search', 'motion', '--limit', '2')
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout);self.assertEqual(data['returned'], 2);self.assertGreater(data['total_matches'], 2)
        exact = json.loads(self.invoke(script, '--id', 'M-01').stdout)
        source = catalog.load_records()
        self.assertEqual(exact['record'], next(x['record'] for x in source if x['record']['id']=='M-01'))
        self.assertIn('not project instructions', exact['boundary'])
        self.assertNotEqual(self.invoke(script, '--id', '../outside').returncode, 0)

    def test_catalog_rejects_stale_fingerprint(self):
        target = self.root/'references';shutil.copytree(catalog.ROOT, target)
        p=target/'style-playbooks.json';p.write_bytes(p.read_bytes()+b'\n')
        with self.assertRaisesRegex(ValueError, 'fingerprint'):catalog.load_records(target)

    def test_evidence_helpers_preserve_unknowns_and_migrate_without_clobber(self):
        for skill, filename in [('final-client-handoff','verify-handoff.py'),('web-reference-research','verify-reference-record.py')]:
            with self.subTest(skill=skill):
                script=f'{skill}/scripts/{filename}';module=load(script, skill.replace('-','_'))
                records={key:{'status':'pass','applicable':True,'evidence':[{'kind':'note','value':'Synthetic fixture assertion only.'}]} for key in module.REQUIRED}
                fixture=self.root/f'{skill}.json';data={'schema_version':2,'skill':skill,'records':records};fixture.write_text(json.dumps(data))
                self.assertEqual(self.invoke(script,fixture,'--require-passed').returncode,0)
                records[module.REQUIRED[0]]={'status':'untested','applicable':None,'evidence':[],'rationale':'Not run in fixture.'};fixture.write_text(json.dumps(data))
                self.assertNotEqual(self.invoke(script,fixture,'--require-passed').returncode,0)
                records[module.REQUIRED[0]]=False;fixture.write_text(json.dumps(data))
                self.assertNotEqual(self.invoke(script,fixture).returncode,0)
                legacy=self.root/f'{skill}-legacy.json';legacy.write_text(json.dumps({module.REQUIRED[0]:False}));before=legacy.read_bytes()
                output=self.root/f'{skill}-migrated.json'
                self.assertEqual(self.invoke(script,legacy,'--migrate-legacy','--output',output).returncode,0)
                migrated=json.loads(output.read_text());saved=output.read_bytes()
                self.assertTrue(all(r['status']=='untested' and r['applicable'] is None for r in migrated['records'].values()))
                self.assertEqual(migrated['legacy_source']['payload'],{module.REQUIRED[0]:False})
                self.assertNotEqual(self.invoke(script,output,'--require-passed').returncode,0)
                self.assertNotEqual(self.invoke(script,legacy,'--migrate-legacy','--output',output).returncode,0)
                self.assertEqual(output.read_bytes(),saved);self.assertEqual(legacy.read_bytes(),before)

    @unittest.skipUnless(shutil.which('node'), 'Node unavailable; capture destination guard not tested')
    def test_stitched_force_rejects_symlink_and_preserves_target(self):
        source=self.root/'source.txt';source.write_text('must survive')
        output=self.root/'capture.png';output.symlink_to(source)
        script=SKILLS/'visual-regression-lab/scripts/capture-stitched-full-page.mjs'
        result=subprocess.run(['node',str(script),'--url','http://127.0.0.1:1','--output',str(output),'--force'],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0);self.assertIn('regular file',result.stderr)
        self.assertEqual(source.read_text(),'must survive');self.assertTrue(output.is_symlink())


if __name__ == '__main__':
    unittest.main()
