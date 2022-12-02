from wrappers.hit.HitWrapper import HitWrapper


class SearchWrapper:
    def __init__(self, search):
        self.search = search

    @property
    def query_title(self):
        query_title = self.search['query_title']
        assert type(query_title) is str
        return query_title

    @property
    def hits(self):
        return [HitWrapper(hit) for hit in self.search['hits']]

    @property
    def num_hits(self):
        return len(self.hits)
