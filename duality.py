"""
This module contains functions that сheck whether
the graph has the property of the duality.

TODO: use pylint, looks to me that you didn't
TODO: get rid of these global variables
TODO: It would be nice of you to change the last function.
It looks not efective enough
TODO: add doctests
TODO: test your module on some big graphs, with 1000+ nodes
(this, I assume, will also showe you that realisation with 2times nested loop
isn't great)
TODO: conduct some testing with measuring time and memoty taken,
which will be nice to include in our report
"""
from graph_io import read_adjacency_dict


def add_point(vertex: set, parity: int, graph: dict) -> None:
    """
    Adds adjacent vertex to the dictionary, containing devided_vertices,
to the key corresponding to its parity. If all vertices were added returns None.

    TODO: add doctests
    """

    if len(devided_vertices[0]) + len(devided_vertices[1]) == len(graph):
        # even if it is None, I think, that it's better to cpecify what is returns
        return
    
    # can be combined in one line, looks kinda ugly to me
    parity += 1
    parity %= 2
    for adjacent_vertex in vertex:
        if adjacent_vertex not in checked_vertices:
            devided_vertices[parity].add(adjacent_vertex)
            checked_vertices.add(adjacent_vertex)
            add_point(graph[adjacent_vertex], parity, graph)
        # this is not necessary
        else:
            pass
    # specify what you returns, even if it is None I guess
    return


def devided_vertices_create(graph: dict) -> dict:
    """
    Creates a dictionary where keys are the parity of a number
that was given to the vertices according to the following principle and values are
indices of vertex.

Principle: we assign to any vertex 0, 1 to all connected
to the first, 0 to all that are connected to previous and so on.
    """

    # global variables are not the best way to write code,
    # think of possibility to add these two sets(?) as
    # default parameters of function
    global devided_vertices
    global checked_vertices
    devided_vertices = {}
    devided_vertices[0] = set()
    devided_vertices[1] = set()
    
    # I strongly recommend you to change this
    checked_vertices = set()
    parity = 0
    add_point(graph[1], parity, graph)
    return devided_vertices


def duality_check(devided_vertices: dict, graph: dict) -> bool:
    """
    Returns True if graph has the property of the duality and
False if not.
    """
    # it is not necessary to have this variable
    check = True
    
    # this doesn't look like the best way to do this (2 times nested for loop!)
    # consider using dict comprehension or somehow 'zip' two loops.
    for key in devided_vertices:
        for vertex in devided_vertices[key]:
            for dot in graph[vertex]:
                if dot in devided_vertices[key]:
                    check = False
    return check

if __name__ == '__main__':
    graph = read_adjacency_dict('graph.csv')
    print(duality_check(devided_vertices_create(graph), graph))
