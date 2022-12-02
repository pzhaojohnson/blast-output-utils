from wrappers.report.ReportWrapper import ReportWrapper


class BlastOutput2Wrapper:
    def __init__(self, blast_output2):
        if 'BlastOutput2' in blast_output2:
            self.blast_output2 = blast_output2['BlastOutput2']
        else:
            self.blast_output2 = blast_output2

    @property
    def reports(self):
        return [ReportWrapper(report) for report in self.blast_output2]
