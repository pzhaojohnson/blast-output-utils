import unittest

import json

from wrappers.report.ReportWrapper import ReportWrapper


with open('wrappers/report/example_reports/unkeyed.json', 'r') as f:
    unkeyed = json.loads(f.read())

with open('wrappers/report/example_reports/keyed.json', 'r') as f:
    keyed = json.loads(f.read())


class TestReportProperty(unittest.TestCase):
    def test_unkeyed(self):
        report = ReportWrapper(unkeyed)
        self.assertIs(report.report, unkeyed)

    def test_keyed(self):
        report = ReportWrapper(keyed)
        self.assertIs(report.report, keyed['report'])


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
