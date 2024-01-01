from tkinter import messagebox, simpledialog
from Vertex import Vertex
from Graph import Graph

# Simuliting a switch case for choose the type of graph
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

# Simuliting a switch case for choose the operation in the graph
while True:
    operation = simpledialog.askinteger("OPERACIONES DEL GRAFO", "Ingrese una opcion:\n1. Crear Vertice\n2. Crear Arista\n3. BFS\n4. DFS\n5. Ver Grafo\n6. Salir")
    if operation == 1:
        info_vertex = Vertex(simpledialog.askstring("CREAR VERTICE", "Ingrese el vertice:"))
        graph.insert_vertex(info_vertex)
    elif operation == 2:
        origin_vertex = Vertex(simpledialog.askstring("CREAR ARISTA", "Ingrese el vertice de origen:"))
        destination_vertex = Vertex(simpledialog.askstring("CREAR ARISTA", "Ingrese el vertice de destino:"))
        graph.insert_edge(origin_vertex, destination_vertex)
        print(graph)
    elif operation == 3:
        start = Vertex(simpledialog.askstring("INICIO", "Ingrese el vertice de inicio:"))
        finish = Vertex(simpledialog.askstring("FIN", "Ingrese el vertice de finalizacion:"))
        exist_path = graph.bfs(start, finish)
        print('BFS')
        if exist_path:
            print("BFS que no imprime la ruta")
            print("\t", f"Existe al menos un path desde {start} hasta {finish}")
        else:
            print("\t", f"No hay un camino desde {start} hasta {finish}")
    # elif operation == 4:
    #     start = simpledialog.askstring("INICIO", "Ingrese el vertice de inicio:")
    #     # print('DFS')
    elif operation == 5:
        messagebox.showinfo('OPERACIONES DEL GRAFO', 'GRAFO\nRepresentacion: Lista de Adyacencia\n\n' + str(graph))
    elif operation < 1 or operation > 6:
        messagebox.showwarning('OPERACIONES DEL GRAFO', 'Opcion no valida, vuelva a intentarlo')
    else:
        break
