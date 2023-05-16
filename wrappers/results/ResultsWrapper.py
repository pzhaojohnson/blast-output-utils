from wrappers.search.SearchWrapper import SearchWrapper


class ResultsWrapper:
    def __init__(self, wrappee):
        self.wrappee = wrappee

    @property
    def search(self):
        return SearchWrapper(self.wrappee['search'])
