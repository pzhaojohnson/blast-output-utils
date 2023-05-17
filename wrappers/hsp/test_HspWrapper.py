import unittest

import json

from wrappers.hsp.HspWrapper import HspWrapper


example_hsps_dir_path = 'wrappers/hsp/example_hsps/'

with open(example_hsps_dir_path + 'hsp1.json', 'r') as f:
    hsp1 = json.loads(f.read())

with open(example_hsps_dir_path + 'plus_hit_strand.json', 'r') as f:
    plus_hit_strand = json.loads(f.read())

with open(example_hsps_dir_path + 'minus_hit_strand.json', 'r') as f:
    minus_hit_strand = json.loads(f.read())


class TestWrappeeProperty(unittest.TestCase):
    def test_hsp1(self):
        hsp = HspWrapper(hsp1)
        self.assertIs(hsp.wrappee, hsp1)


class TestQueryFromGetter(unittest.TestCase):
    def test_hsp1(self):
        hsp = HspWrapper(hsp1)
        self.assertEqual(hsp.query_from, 561)


class TestQueryToGetter(unittest.TestCase):
    def test_hsp1(self):
        hsp = HspWrapper(hsp1)
        self.assertEqual(hsp.query_to, 1234)


class TestQueryStrandGetter(unittest.TestCase):
    def test_hsp1(self):
        hsp = HspWrapper(hsp1)
        self.assertEqual(hsp.query_strand, 'Plus')


class TestHasPlusQueryStrandMethod(unittest.TestCase):
    def test_plus_query_strand(self):
        # make deep copy
        plus_query_strand = json.loads(json.dumps(hsp1))
        # test unusual letter casing
        plus_query_strand['query_strand'] = 'pLUs'
        hsp = HspWrapper(plus_query_strand)
        self.assertTrue(hsp.has_plus_query_strand())

    def test_minus_query_strand(self):
        # make deep copy
        minus_query_strand = json.loads(json.dumps(hsp1))
        # test unusual letter casing
        minus_query_strand['query_strand'] = 'MInUs'
        hsp = HspWrapper(minus_query_strand)
        self.assertFalse(hsp.has_plus_query_strand())


class TestHasMinusQueryStrandMethod(unittest.TestCase):
    def test_plus_query_strand(self):
        # make deep copy
        plus_query_strand = json.loads(json.dumps(hsp1))
        # test unusual letter casing
        plus_query_strand['query_strand'] = 'PluS'
        hsp = HspWrapper(plus_query_strand)
        self.assertFalse(hsp.has_minus_query_strand())

    def test_minus_query_strand(self):
        # make deep copy
        minus_query_strand = json.loads(json.dumps(hsp1))
        # test unusual letter casing
        minus_query_strand['query_strand'] = 'miNUs'
        hsp = HspWrapper(minus_query_strand)
        self.assertTrue(hsp.has_minus_query_strand())


class TestHitFromGetter(unittest.TestCase):
    def test_hsp1(self):
        hsp = HspWrapper(hsp1)
        self.assertEqual(hsp.hit_from, 683)


class TestHitToGetter(unittest.TestCase):
    def test_hsp1(self):
        hsp = HspWrapper(hsp1)
        self.assertEqual(hsp.hit_to, 1)


class TestHitStrandGetter(unittest.TestCase):
    def test_hsp1(self):
        hsp = HspWrapper(hsp1)
        self.assertEqual(hsp.hit_strand, 'Minus')


class TestHasPlusHitStrandMethod(unittest.TestCase):
    def test_plus_hit_strand(self):
        # make deep copy
        plus_hit_strand = json.loads(json.dumps(hsp1))
        # test unusual letter casing
        plus_hit_strand['hit_strand'] = 'PLus'
        hsp = HspWrapper(plus_hit_strand)
        self.assertTrue(hsp.has_plus_hit_strand())

    def test_minus_hit_strand(self):
        # make deep copy
        minus_hit_strand = json.loads(json.dumps(hsp1))
        # test unusual letter casing
        minus_hit_strand['hit_strand'] = 'minUS'
        hsp = HspWrapper(minus_hit_strand)
        self.assertFalse(hsp.has_plus_hit_strand())


class TestHasMinusHitStrandMethod(unittest.TestCase):
    def test_plus_hit_strand(self):
        # make deep copy
        plus_hit_strand = json.loads(json.dumps(hsp1))
        # test unusual letter casing
        plus_hit_strand['hit_strand'] = 'PluS'
        hsp = HspWrapper(plus_hit_strand)
        self.assertFalse(hsp.has_minus_hit_strand())

    def test_minus_hit_strand(self):
        # make deep copy
        minus_hit_strand = json.loads(json.dumps(hsp1))
        # test unusual letter casing
        minus_hit_strand['hit_strand'] = 'MInuS'
        hsp = HspWrapper(minus_hit_strand)
        self.assertTrue(hsp.has_minus_hit_strand())


class TestCoveredHitPositionsGetter(unittest.TestCase):
    def test_plus_hit_strand(self):
        hsp = HspWrapper(plus_hit_strand)
        # hit_from is less than hit_to
        self.assertLess(hsp.hit_from, hsp.hit_to)
        ps = hsp.covered_hit_positions
        self.assertEqual(ps, set([p for p in range(1223, 2377)]))

    def test_minus_hit_strand(self):
        hsp = HspWrapper(minus_hit_strand)
        # hit_from is greater than hit_to
        self.assertGreater(hsp.hit_from, hsp.hit_to)
        ps = hsp.covered_hit_positions
        self.assertEqual(ps, set([p for p in range(23, 2372)]))
