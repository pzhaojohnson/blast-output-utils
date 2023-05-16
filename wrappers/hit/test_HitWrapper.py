import unittest

import json

from wrappers.hit.HitWrapper import HitWrapper


with open('wrappers/hit/example_hits/zero_hsps.json', 'r') as f:
    zero_hsps = json.loads(f.read())

with open('wrappers/hit/example_hits/two_hsps.json', 'r') as f:
    two_hsps = json.loads(f.read())

with open('wrappers/hit/example_hits/four_hsps.json', 'r') as f:
    four_hsps = json.loads(f.read())

with open('wrappers/hit/example_hits/five_hsps.json', 'r') as f:
    five_hsps = json.loads(f.read())


class TestWrappeeProperty(unittest.TestCase):
    def test_zero_hsps(self):
        hit = HitWrapper(zero_hsps)
        self.assertIs(hit.wrappee, zero_hsps)


class TestDescriptionGetter(unittest.TestCase):
    def test_two_hsps(self):
        hit = HitWrapper(two_hsps)
        self.assertEqual(hit.description[0]['id'], 'gnl|BL_ORD_ID|0')
        self.assertEqual(hit.description[0]['accession'], '0')
        self.assertEqual(hit.description[0]['title'], 'CY1')


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


class TestHspsSortedByQueryFromGetter(unittest.TestCase):
    def test_zero_hsps(self):
        hit = HitWrapper(zero_hsps)
        self.assertEqual(len(hit.hsps_sorted_by_query_from), 0)

    def test_four_hsps(self):
        hit = HitWrapper(four_hsps)
        hsps_sorted_by_query_from = hit.hsps_sorted_by_query_from
        # check that hsps are not already sorted
        self.assertNotEqual(hsps_sorted_by_query_from, hit.hsps)
        self.assertEqual(len(hsps_sorted_by_query_from), 4)
        self.assertEqual(hsps_sorted_by_query_from[0].query_from, 1017)
        self.assertEqual(hsps_sorted_by_query_from[1].query_from, 2051)
        self.assertEqual(hsps_sorted_by_query_from[2].query_from, 2053)
        self.assertEqual(hsps_sorted_by_query_from[3].query_from, 2691)

class TestCoveredHitPositionsGetter(unittest.TestCase):
    def test_zero_hsps(self):
        hit = HitWrapper(zero_hsps)
        self.assertEqual(len(hit.covered_hit_positions), 0)

    def test_five_hsps(self):
        hit = HitWrapper(five_hsps)
        ps = set([p for p in range(71, 2477)])
        self.assertEqual(hit.covered_hit_positions, ps)
