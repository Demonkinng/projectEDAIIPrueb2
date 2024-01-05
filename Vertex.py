"""
    Clase: Vertex
    Autor: Angel David Chuncho Jimenez
    Fecha: 05/01/2024
"""


class Vertex:

    def __init__(self, info):
        # Constructor for Vertex Class
        self._info = info

    @property
    def info(self):
        # Return info associated with this vertex
        return self._info

    def __repr__(self):
        # Method for representing the objects in a class as a string
        return self._info

    def __eq__(self, other):
        # Method to compare Vertex type objects
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._info == other._info

    def __hash__(self):
        # Return hash based on vertex info
        return hash(self._info)
