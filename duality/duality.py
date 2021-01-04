"""
This module contains functions that сheck whether
the graph has the property of the duality.
"""
from graph_io import read_adjacency_dict


def add_point(vertex: set, parity: int, graph: dict) -> None:
    """
    Adds adjacent vertex to the dictionary, containing devided_vertices,
to the key corresponding to its parity. If all vertices were added returns None.
    """
    if len(devided_vertices[0]) + len(devided_vertices[1]) == len(graph):
        return
    parity += 1
    parity %= 2
    for adjacent_vertex in vertex:
        if adjacent_vertex not in checked_vertices:
            devided_vertices[parity].add(adjacent_vertex)
            checked_vertices.add(adjacent_vertex)
            add_point(graph[adjacent_vertex], parity, graph)
        else:
            pass
    return


def devided_vertices_create(graph: dict) -> dict:
    """
    Creates a dictionary where keys are the parity of a number
that was given to the vertices according to the following principle and values are
indices of vertex.

Principle: we assign to any vertex 0, 1 to all connected
to the first, 0 to all that are connected to previous and so on.
    """
    global devided_vertices
    global checked_vertices
    devided_vertices = {}
    devided_vertices[0] = set()
    devided_vertices[1] = set()
    checked_vertices = set()
    parity = 0
    add_point(graph[1], parity, graph)
    return devided_vertices


def duality_check(devided_vertices: dict, graph: dict) -> bool:
    """
    Returns True if graph has the property of the duality and
False if not.
    """
    check = True
    for key in devided_vertices:
        for vertex in devided_vertices[key]:
            for dot in graph[vertex]:
                if dot in devided_vertices[key]:
                    check = False
    return check


if __name__ == "__main__":
    graph = read_adjacency_dict('graph.csv')
    print(duality_check(devided_vertices_create(graph), graph))
