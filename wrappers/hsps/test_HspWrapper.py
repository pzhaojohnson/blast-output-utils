import unittest

import json

from wrappers.hsps.HspWrapper import HspWrapper


with open('wrappers/hsps/example_hsps/hsp1.json', 'r') as f:
    hsp1 = json.loads(f.read())


class TestHspWrapper(unittest.TestCase):
    def test_hsp1(self):
        hsp = HspWrapper(hsp1)
        self.assertIs(hsp.hsp, hsp1)
        self.assertEqual(hsp.query_from, 561)
        self.assertEqual(hsp.query_to, 1234)
        self.assertEqual(hsp.query_strand, 'Plus')
        self.assertEqual(hsp.hit_from, 683)
        self.assertEqual(hsp.hit_to, 1)
        self.assertEqual(hsp.hit_strand, 'Minus')
