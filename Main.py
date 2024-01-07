"""
    Estructura de Datos y Algoritmos II
    Proyecto # 01 - Implementacion de Grafos en Python con POO
    Autor: Angel David Chuncho Jimenez
    Carrera: Ingenieria de Software
    Fecha: 05/01/2024
    Referencia: Data Structures & Algorithms in Python by Michael Goodrich, et al. (1st Edition)
"""

from tkinter import messagebox, simpledialog
from Vertex import Vertex
from Graph import Graph

# Choose the type of graph (directed or indirected)
while True:
    typeGraph = simpledialog.askinteger("TIPO DE GRAFO", "Elija el tipo de grafo a crear:\n1. Directo\n2. Indirecto")
    if typeGraph == 1:
        graph = Graph(True)
        break
    elif typeGraph == 2:
        graph = Graph(False)
        break
    else:
        messagebox.showwarning('TIPO DE GRAFO', 'Opcion no valida, vuelva a intentarlo')

# Choose the operations for the created graph (Deleted operations aren't implemented)
while True:
    operation = simpledialog.askinteger("OPERACIONES DEL GRAFO", "Ingrese una opcion:\n1. Crear Vertice\n2. Crear Arista\n3. BFS\n4. DFS\n5. Ver Grafo\n6. Salir")
    if operation == 1:  # Insert Vertex
        new_vertex = Vertex(simpledialog.askstring("CREAR VERTICE", "Ingrese el vertice:"))
        graph.insert_vertex(new_vertex)
    elif operation == 2:  # Insert Edge
        origin_vertex = Vertex(simpledialog.askstring("CREAR ARISTA", "Ingrese el vertice de origen:"))
        destination_vertex = Vertex(simpledialog.askstring("CREAR ARISTA", "Ingrese el vertice de destino:"))
        graph.insert_edge(origin_vertex, destination_vertex)
    elif operation == 3:  # BFS
        start_vertex = Vertex(simpledialog.askstring("INICIO", "Ingrese el vertice de inicio:"))
        finish_vertex = Vertex(simpledialog.askstring("FIN", "Ingrese el vertice de finalizacion:"))
        parents = {clave: None for clave in graph.vertices}
        exist_path = graph.bfs(start_vertex, finish_vertex, parents)
        bfs_tree = graph.construct_tree(start_vertex, parents)
        if exist_path:
            messagebox.showinfo('BFS', f'Ruta mas corta: {str(exist_path)} \n\nArbol BFS:\n {bfs_tree}')
        else:
            messagebox.showinfo('BFS', f'No existe una ruta desde {start_vertex} hacia {finish_vertex}')
    elif operation == 4:  # DFS
        start_vertex = Vertex(simpledialog.askstring("INICIO", "Ingrese el vertice de inicio:"))
        searched = {clave: False for clave in graph.vertices}
        parents = {clave: None for clave in graph.vertices}
        component_r = []
        graph.dfs(start_vertex, searched, parents, component_r)
        dfs_tree = graph.construct_tree(start_vertex, parents)
        messagebox.showinfo('DFS', 'Componente Conectado:\n' + str(component_r) + '\n\nArbol DFS:\n' + dfs_tree)
    elif operation == 5:  # View Graph
        messagebox.showinfo('OPERACIONES DEL GRAFO', 'GRAFO\nRepresentacion: Lista de Adyacencia\n\n' + str(graph))
    elif operation < 1 or operation > 6:  # Invalid options
        messagebox.showwarning('OPERACIONES DEL GRAFO', 'Opcion no valida, vuelva a intentarlo')
    else:
        break
