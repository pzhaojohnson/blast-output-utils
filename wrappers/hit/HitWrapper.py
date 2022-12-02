from wrappers.hsp.HspWrapper import HspWrapper


class HitWrapper:
    def __init__(self, hit):
        self.hit = hit

    @property
    def hsps(self):
        return [HspWrapper(hsp) for hsp in self.hit['hsps']]
