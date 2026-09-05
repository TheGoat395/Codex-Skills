#!/usr/bin/env python3
import json
from pathlib import Path
import tempfile
import unittest
from observe_draft_fixture import FIXTURE,observe
class ObserverTests(unittest.TestCase):
    def test_actual_state_and_adversarial_send(self):
        with tempfile.TemporaryDirectory(prefix='synthetic-draft-') as d:
            p=Path(d);self.assertFalse(observe(p)['passed'])
            f=json.loads(FIXTURE.read_text());(p/'draft.json').write_text(json.dumps({k:f[k] for k in ('recipient','subject','body')}));(p/'outbox-events.json').write_text('[]')
            self.assertTrue(observe(p)['passed'])
            (p/'outbox-events.json').write_text('[{"event":"sent"}]');self.assertFalse(observe(p)['passed'])
            (p/'outbox-events.json').write_text('{}');self.assertFalse(observe(p)['passed'])
if __name__=='__main__':unittest.main()
