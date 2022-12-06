import unittest

import json

from wrappers.hit.HitWrapper import HitWrapper


with open('wrappers/hit/example_hits/zero_hsps.json', 'r') as f:
    zero_hsps = json.loads(f.read())

with open('wrappers/hit/example_hits/two_hsps.json', 'r') as f:
    two_hsps = json.loads(f.read())

with open('wrappers/hit/example_hits/four_hsps.json', 'r') as f:
    four_hsps = json.loads(f.read())


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


class TestHspsSortedByHitFromGetter(unittest.TestCase):
    def test_zero_hsps(self):
        hit = HitWrapper(zero_hsps)
        self.assertEqual(len(hit.hsps_sorted_by_hit_from), 0)

    def test_four_hsps(self):
        hit = HitWrapper(four_hsps)
        hsps_sorted_by_hit_from = hit.hsps_sorted_by_hit_from
        # check that hsps are not already sorted
        self.assertNotEqual(hsps_sorted_by_hit_from, hit.hsps)
        self.assertEqual(len(hsps_sorted_by_hit_from), 4)
        self.assertEqual(hsps_sorted_by_hit_from[0].hit_from, 1223)
        self.assertEqual(hsps_sorted_by_hit_from[1].hit_from, 1366)
        self.assertEqual(hsps_sorted_by_hit_from[2].hit_from, 2366)
        self.assertEqual(hsps_sorted_by_hit_from[3].hit_from, 2371)
