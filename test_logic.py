import unittest, json
from pathlib import Path
from logic import run
class LogicTests(unittest.TestCase):
    def setUp(self):
        self.records=json.loads(Path(__file__).with_name("sample_data.json").read_text())
    def test_guarded_passes(self):
        self.assertEqual(run({'candidate':'guarded'},self.records)['pass_rate'],1)
    def test_regression_detected(self):
        self.assertEqual(run({'candidate':'baseline'},self.records)['pass_rate'],0.8)
    def test_bad_candidate(self):
        with self.assertRaises(ValueError): run({'candidate':'unknown'},self.records)
    def test_empty_dataset(self):
        self.assertEqual(run({},[])['pass_rate'],0)
