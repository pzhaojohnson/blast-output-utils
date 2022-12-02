from wrappers.results.ResultsWrapper import ResultsWrapper


class ReportWrapper:
    def __init__(self, report):
        if 'report' in report:
            self.report = report['report']
        else:
            self.report = report

    @property
    def results(self):
        return ResultsWrapper(self.report['results'])
