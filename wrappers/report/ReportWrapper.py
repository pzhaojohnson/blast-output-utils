from wrappers.results.ResultsWrapper import ResultsWrapper


class ReportWrapper:
    def __init__(self, wrappee):
        if 'report' in wrappee:
            self.wrappee = wrappee['report']
        else:
            self.wrappee = wrappee

    @property
    def results(self):
        return ResultsWrapper(self.wrappee['results'])
