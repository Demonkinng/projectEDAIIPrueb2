from tkinter import messagebox
from Edge import Edge
from collections import deque


class Graph:
    # Representation of a simple graph using an adjacency map.
    def __init__(self, directed):
        # Create an empty graph(undirected, by default).
        self._directed = directed
        self._vertices = {}

    def insert_vertex(self, new_vertex):
        # Insert a new Vertex with x as information only if the new Vertex doesn't already exist in the graph
        if new_vertex not in self._vertices:
            self._vertices[new_vertex] = []
            messagebox.showinfo('CREAR VERTICE', 'OPERACION EXITOSA\nEL VERTICE [' + str(new_vertex) + '] SE HA CREADO')
        else:
            messagebox.showerror('CREAR VERTICE', 'OPERACION FALLIDA\nEL VERTICE [' + str(new_vertex) + '] YA HA SIDO CREADO')

    def insert_edge(self, origin_vertex, destination_vertex):
        # Insert a new Edge from origin_vertex to destination_vertex
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
            messagebox.showinfo('CREAR ARISTA', 'OPERACION EXITOSA\nLAS ARISTAS [' + str(edge) + ' y ' + str(reflected_edge) + '] SE HAN CREADO')
        else:
            self._vertices[origin_vertex].append(edge)
            messagebox.showinfo('CREAR ARISTA', 'OPERACION EXITOSA\nLA ARISTA [' + str(edge) + '] SE HA CREADO')

    def bfs(self, start, finish):
        search_queue = deque()
        search_queue += self._vertices[start]
        searched = {clave: False for clave in self._vertices}
        parents = {clave: None for clave in self._vertices}
        # searched = []

        while search_queue:
            current_edge = search_queue.popleft()

    def __repr__(self):
        return '\n'.join([f"'{key}': {value}" for key, value in self._vertices.items()])
