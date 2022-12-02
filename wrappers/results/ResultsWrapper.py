from wrappers.search.SearchWrapper import SearchWrapper


class ResultsWrapper:
    def __init__(self, results):
        self.results = results

    @property
    def search(self):
        return SearchWrapper(self.results['search'])
