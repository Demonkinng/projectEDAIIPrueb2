class Edge:
    def __init__(self, u, v):
        # Constructor for Edge Class
        self._origin = u
        self._destination = v

    @property
    def origin(self):
        # Return origin vertex associated with this edge
        return self._origin

    @property
    def destination(self):
        # Return destination vertex associated with this edge
        return self._destination

    def __repr__(self):
        # Method for representing the objects in a class as a string
        return f"({self._origin},{self._destination})"
