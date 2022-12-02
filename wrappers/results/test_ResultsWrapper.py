import unittest

import json

from wrappers.results.ResultsWrapper import ResultsWrapper


with open('wrappers/results/example_results/results1.json', 'r') as f:
    results1 = json.loads(f.read())


class TestResultsProperty(unittest.TestCase):
    def test_results1(self):
        results = ResultsWrapper(results1)
        self.assertIs(results.results, results1)


class TestSearchGetter(unittest.TestCase):
    def test_results1(self):
        results = ResultsWrapper(results1)
        search = results.search
        # just check some search values
        self.assertEqual(search.hits[0].hsps[0].hit_from, 683)
        self.assertEqual(search.hits[0].hsps[0].hit_strand, 'Minus')
