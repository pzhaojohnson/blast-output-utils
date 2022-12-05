import unittest

import json

from wrappers.hsp.HspWrapper import HspWrapper


with open('wrappers/hsp/example_hsps/hsp1.json', 'r') as f:
    hsp1 = json.loads(f.read())


class TestHspProperty(unittest.TestCase):
    def test_hsp1(self):
        hsp = HspWrapper(hsp1)
        self.assertIs(hsp.hsp, hsp1)


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
