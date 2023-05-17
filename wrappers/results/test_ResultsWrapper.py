import unittest

import json

from wrappers.results.ResultsWrapper import ResultsWrapper


example_results_dir_path = 'wrappers/results/example_results/'

example_results = {}

with open(example_results_dir_path + 'results1.json', 'r') as f:
    results1 = json.loads(f.read())
    example_results['results1'] = results1


class TestWrappeeProperty(unittest.TestCase):
    def test_results1(self):
        wrappee = example_results['results1']
        results = ResultsWrapper(wrappee)
        self.assertIs(results.wrappee, wrappee)


class TestSearchGetter(unittest.TestCase):
    def test_results1(self):
        results = ResultsWrapper(example_results['results1'])
        search = results.search
        # just check some search values
        self.assertEqual(search.hits[0].hsps[0].hit_from, 683)
        self.assertEqual(search.hits[0].hsps[0].hit_strand, 'Minus')
