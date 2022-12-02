import unittest

import json

from wrappers.search.SearchWrapper import SearchWrapper


with open('wrappers/search/example_searches/zero_hits.json', 'r') as f:
    zero_hits = json.loads(f.read())

with open('wrappers/search/example_searches/two_hits.json', 'r') as f:
    two_hits = json.loads(f.read())


class TestSearchProperty(unittest.TestCase):
    def test_two_hits(self):
        search = SearchWrapper(two_hits)
        self.assertIs(search.search, two_hits)


class TestHitsGetter(unittest.TestCase):
    def test_zero_hits(self):
        search = SearchWrapper(zero_hits)
        self.assertEqual(len(search.hits), 0)

    def test_two_hits(self):
        search = SearchWrapper(two_hits)
        self.assertEqual(len(search.hits), 2)
        hit1 = search.hits[0]
        hit2 = search.hits[1]
        # just check some hit values
        self.assertEqual(hit1.hsps[0].query_to, 2013)
        self.assertEqual(hit2.hsps[0].hit_from, 546)


class TestNumHitsGetter(unittest.TestCase):
    def test_zero_hits(self):
        search = SearchWrapper(zero_hits)
        self.assertEqual(search.num_hits, 0)

    def test_two_hits(self):
        search = SearchWrapper(two_hits)
        self.assertEqual(search.num_hits, 2)
