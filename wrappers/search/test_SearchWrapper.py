import unittest

import json

from wrappers.search.SearchWrapper import SearchWrapper


example_searches_dir_path = 'wrappers/search/example_searches/'

example_searches = {}

with open(example_searches_dir_path + 'zero_hits.json', 'r') as f:
    example_searches['zero_hits'] = json.loads(f.read())

with open(example_searches_dir_path + 'two_hits.json', 'r') as f:
    example_searches['two_hits'] = json.loads(f.read())


class TestWrappeeProperty(unittest.TestCase):
    def test_two_hits(self):
        wrappee = example_searches['two_hits']
        search = SearchWrapper(wrappee)
        self.assertIs(search.wrappee, wrappee)


class TestQueryTitleGetter(unittest.TestCase):
    def test_two_hits(self):
        search = SearchWrapper(example_searches['two_hits'])
        self.assertEqual(search.query_title, 'read3')


class TestHitsGetter(unittest.TestCase):
    def test_zero_hits(self):
        search = SearchWrapper(example_searches['zero_hits'])
        self.assertEqual(len(search.hits), 0)

    def test_two_hits(self):
        search = SearchWrapper(example_searches['two_hits'])
        self.assertEqual(len(search.hits), 2)
        hit1 = search.hits[0]
        hit2 = search.hits[1]
        # just check some hit values
        self.assertEqual(hit1.hsps[0].query_to, 2013)
        self.assertEqual(hit2.hsps[0].hit_from, 546)


class TestNumHitsGetter(unittest.TestCase):
    def test_zero_hits(self):
        search = SearchWrapper(example_searches['zero_hits'])
        self.assertEqual(search.num_hits, 0)

    def test_two_hits(self):
        search = SearchWrapper(example_searches['two_hits'])
        self.assertEqual(search.num_hits, 2)
