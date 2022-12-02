import unittest

import json

from wrappers.hit.HitWrapper import HitWrapper


with open('wrappers/hit/example_hits/zero_hsps.json', 'r') as f:
    zero_hsps = json.loads(f.read())

with open('wrappers/hit/example_hits/two_hsps.json', 'r') as f:
    two_hsps = json.loads(f.read())


class TestHitProperty(unittest.TestCase):
    def test_zero_hsps(self):
        hit = HitWrapper(zero_hsps)
        self.assertIs(hit.hit, zero_hsps)


class TestHspsGetter(unittest.TestCase):
    def test_zero_hsps(self):
        hit = HitWrapper(zero_hsps)
        self.assertEqual(len(hit.hsps), 0)

    def test_two_hsps(self):
        hit = HitWrapper(two_hsps)
        self.assertEqual(len(hit.hsps), 2)
        hsp1 = hit.hsps[0]
        hsp2 = hit.hsps[1]
        # check just some hsp values
        self.assertEqual(hsp1.query_to, 1008)
        self.assertEqual(hsp2.hit_from, 2678)
