from wrappers.report.ReportWrapper import ReportWrapper


class BlastOutput2Wrapper:
    def __init__(self, wrappee):
        if 'BlastOutput2' in wrappee:
            self.wrappee = wrappee['BlastOutput2']
        else:
            self.wrappee = wrappee

    @property
    def reports(self):
        return [ReportWrapper(report) for report in self.wrappee]
