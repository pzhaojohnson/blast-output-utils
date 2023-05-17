import unittest

import json

from wrappers.report.ReportWrapper import ReportWrapper


example_reports_dir_path = 'wrappers/report/example_reports/'

example_reports = {}

with open(example_reports_dir_path + 'unkeyed.json', 'r') as f:
    unkeyed = json.loads(f.read())
    example_reports['unkeyed'] = unkeyed

with open(example_reports_dir_path + 'keyed.json', 'r') as f:
    keyed = json.loads(f.read())
    example_reports['keyed'] = keyed


class TestWrappeeProperty(unittest.TestCase):
    def test_unkeyed(self):
        report = ReportWrapper(unkeyed)
        self.assertIs(report.wrappee, unkeyed)

    def test_keyed(self):
        report = ReportWrapper(keyed)
        self.assertIs(report.wrappee, keyed['report'])


class TestResultsGetter(unittest.TestCase):
    def test_unkeyed(self):
        report = ReportWrapper(unkeyed)
        results = report.results
        # just check one results value
        self.assertEqual(results.search.hits[0].hsps[0].hit_from, 1250)

    def test_keyed(self):
        report = ReportWrapper(keyed)
        results = report.results
        # just check one results value
        self.assertEqual(results.search.hits[0].hsps[0].query_to, 195)
