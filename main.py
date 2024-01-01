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
    if operation == 1:
        new_vertex = Vertex(simpledialog.askstring("CREAR VERTICE", "Ingrese el vertice:"))
        graph.insert_vertex(new_vertex)
    elif operation == 2:
        origin_vertex = Vertex(simpledialog.askstring("CREAR ARISTA", "Ingrese el vertice de origen:"))
        destination_vertex = Vertex(simpledialog.askstring("CREAR ARISTA", "Ingrese el vertice de destino:"))
        graph.insert_edge(origin_vertex, destination_vertex)
    elif operation == 3:
        start_vertex = Vertex(simpledialog.askstring("INICIO", "Ingrese el vertice de inicio:"))
        finish_vertex = Vertex(simpledialog.askstring("FIN", "Ingrese el vertice de finalizacion:"))
        exist_path = graph.bfs(start_vertex, finish_vertex)
        print('BFS')
        # if exist_path:
        #     print("BFS que no imprime la ruta")
        #     print("\t", f"Existe al menos un path desde {start} hasta {finish}")
        # else:
        #     print("\t", f"No hay un camino desde {start} hasta {finish}")
    elif operation == 4:
        start_vertex = Vertex(simpledialog.askstring("INICIO", "Ingrese el vertice de inicio:"))
        searched = {clave: False for clave in graph.vertices}
        parents = {clave: None for clave in graph.vertices}
        component_r = []
        print('DFS')
        print(searched)
        print(parents)
        graph.dfs(start_vertex, searched, parents, component_r)
        print(component_r)
        graph.construct_dfs_tree(start_vertex, parents)
    elif operation == 5:
        messagebox.showinfo('OPERACIONES DEL GRAFO', 'GRAFO\nRepresentacion: Lista de Adyacencia\n\n' + str(graph))
    elif operation < 1 or operation > 6:
        messagebox.showwarning('OPERACIONES DEL GRAFO', 'Opcion no valida, vuelva a intentarlo')
    else:
        break
