from wrappers.hsp.HspWrapper import HspWrapper

import operator


class HitWrapper:
    def __init__(self, hit):
        self.hit = hit

    @property
    def wrappee(self):
        """Returns the wrapped hit dictionary."""
        return self.hit

    @property
    def description(self):
        return self.hit['description']

    @property
    def hsps(self):
        return [HspWrapper(hsp) for hsp in self.hit['hsps']]

    @property
    def hsps_sorted_by_query_from(self):
        hsps = self.hsps
        hsps.sort(key=operator.attrgetter('query_from'))
        return hsps

    @property
    def hsps_sorted_by_hit_from(self):
        hsps = self.hsps
        hsps.sort(key=operator.attrgetter('hit_from'))
        return hsps

    @property
    def covered_hit_positions(self):
        covered_hit_positions = set()
        for hsp in self.hsps:
            covered_hit_positions.update(hsp.covered_hit_positions)
        return covered_hit_positions
