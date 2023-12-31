class Edge:
    def __init__(self, u, v):
        # Do not call constructor directly. Use Graph's insert_edge(u,v)
        self._origin = u
        self._destination = v

    def endpoints(self):
        # Return (u,v) tuple for vertices u and v
        return self._origin, self._destination

    def opposite(self, v):
        # Return the vertex that is opposite v on this edge
        return self._destination if v is self._origin else self._origin

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination

    def __repr__(self):
        return f"({self._origin},{self._destination})"
