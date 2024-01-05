"""
    Clase: Graph
    Autor: Angel David Chuncho Jimenez
    Fecha: 05/01/2024
"""

from tkinter import messagebox
from Edge import Edge
from collections import deque


class Graph:
    # Representation of a simple graph using an adjacency map.
    def __init__(self, directed):
        # Constructor for Graph Class
        self._directed = directed
        self._vertices = {}

    def insert_vertex(self, new_vertex):
        # Insert a new Vertex only if the new Vertex doesn't already exist in the graph
        if new_vertex not in self._vertices:
            self._vertices[new_vertex] = []
            messagebox.showinfo('CREAR VERTICE', 'OPERACION EXITOSA\nEL VERTICE [' + str(new_vertex) + '] SE HA CREADO')
        else:
            messagebox.showerror('CREAR VERTICE', 'OPERACION FALLIDA\nEL VERTICE [' + str(new_vertex) + '] YA HA SIDO CREADO')

    def insert_edge(self, origin_vertex, destination_vertex):
        # Insert a new Edge from origin_vertex to destination_vertex only if the new Edge doesn't already exist in the graph
        if origin_vertex not in self._vertices or destination_vertex not in self._vertices:
            invalid_vertices = [vertex for vertex in [origin_vertex, destination_vertex] if vertex not in self._vertices]
            messagebox.showerror('CREAR ARISTA', 'OPERACION FALLIDA\nVERTICE(S) NO VALIDO(S): ' + str(invalid_vertices))
            return

        if any(edge.origin == origin_vertex and edge.destination == destination_vertex for edges in self._vertices.values() for edge in edges):
            messagebox.showerror('CREAR ARISTA', 'OPERACION FALLIDA\nLA ARISTA INGRESADA YA EXISTE')
            return

        edge = Edge(origin_vertex, destination_vertex)

        if not self._directed:
            reflected_edge = Edge(destination_vertex, origin_vertex)
            self._vertices[origin_vertex].append(edge)
            self._vertices[destination_vertex].append(reflected_edge)
            messagebox.showinfo('CREAR ARISTA', f'OPERACION EXITOSA\nLAS ARISTAS [({origin_vertex},{destination_vertex}) y ({destination_vertex},{origin_vertex})] SE HAN CREADO')
        else:
            self._vertices[origin_vertex].append(edge)
            messagebox.showinfo('CREAR ARISTA', f'OPERACION EXITOSA\nLA ARISTA [({origin_vertex},{destination_vertex})] SE HA CREADO')

    def bfs(self, start, finish, parents):
        # Method to apply the bfs algorithm
        search_queue = deque()
        searched = {clave: False for clave in self._vertices}
        path = []

        search_queue.append(start)
        searched[start] = True

        while search_queue:
            vertex = search_queue.popleft()
            if vertex == finish:
                # Build the path from the start vertex to the end vertex
                while vertex is not None:
                    path.insert(0, vertex)
                    vertex = parents[vertex]
                return path

            for neighbor_edge in self._vertices[vertex]:
                neighbor_vertex = neighbor_edge.destination
                if not searched[neighbor_vertex]:
                    searched[neighbor_vertex] = True
                    parents[neighbor_vertex] = vertex
                    search_queue.append(neighbor_vertex)
            # If a route is not found, return an empty list
        return path

    def dfs(self, vertex, searched, parents, component_r):
        # Method to apply the dfs algorithm
        component_r.append(vertex)
        searched[vertex] = True

        for neighbor in self._vertices[vertex]:
            if not searched[neighbor.destination]:
                parents[neighbor.destination] = vertex
                self.dfs(neighbor.destination, searched, parents, component_r)  # Recursive call

    def construct_tree(self, vertex, parents, level=0):
        # Method to build the tree with the parents structure
        if vertex is None:
            return

        dfs_tree = "  " * level + str(vertex) + "\n"

        for key, value in parents.items():
            if value == vertex:
                dfs_tree += self.construct_tree(key, parents, level+1)  # Recursive call

        return dfs_tree

    @property
    def vertices(self):
        # Return dictionary vertices associated with this graph
        return self._vertices

    def __repr__(self):
        # Method for representing the objects in a class as a string
        return '\n'.join([f"'{key}': {value}" for key, value in self._vertices.items()])
