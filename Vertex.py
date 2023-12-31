class Vertex:

    def __init__(self, info):
        # Do not call constructor directly. Use Graph's insert_vertex(x)
        self._info = info

    @property
    def info(self):
        # Return element associated with this vertex
        return self._info

    def __repr__(self):
        return self._info

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._info == other._info

    def __hash__(self):
        # Hash basado en la info del vertice
        return hash(self._info)
