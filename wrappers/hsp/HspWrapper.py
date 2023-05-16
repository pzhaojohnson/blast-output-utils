class HspWrapper:
    def __init__(self, hsp):
        self.hsp = hsp

    @property
    def wrappee(self):
        """Returns the wrapped hsp dictionary."""
        return self.hsp

    @property
    def query_from(self):
        query_from = self.wrappee['query_from']
        assert type(query_from) is int
        return query_from

    @property
    def query_to(self):
        query_to = self.wrappee['query_to']
        assert type(query_to) is int
        return query_to

    @property
    def query_strand(self):
        query_strand = self.wrappee['query_strand']
        assert type(query_strand) is str
        return query_strand

    def has_plus_query_strand(self):
        return self.query_strand.lower() == 'plus'

    def has_minus_query_strand(self):
        return self.query_strand.lower() == 'minus'

    @property
    def hit_from(self):
        hit_from = self.wrappee['hit_from']
        assert type(hit_from) is int
        return hit_from

    @property
    def hit_to(self):
        hit_to = self.wrappee['hit_to']
        assert type(hit_to) is int
        return hit_to

    @property
    def hit_strand(self):
        hit_strand = self.wrappee['hit_strand']
        assert type(hit_strand) is str
        return hit_strand

    def has_plus_hit_strand(self):
        return self.hit_strand.lower() == 'plus'

    def has_minus_hit_strand(self):
        return self.hit_strand.lower() == 'minus'

    @property
    def covered_hit_positions(self):
        pmin = min(self.hit_from, self.hit_to)
        pmax = max(self.hit_from, self.hit_to)
        return set([p for p in range(pmin, pmax + 1)])
