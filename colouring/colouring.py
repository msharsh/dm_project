'''
This module implements the ability to find
possible coloring for the graph G = (V, E)
'''

from typing import List, Dict, Set
from doctest import testmod


def colour_graph(graph: Dict[int, List[int]], colors: List[str])\
        -> Dict[str, Set[int]]:
    '''
    Implements the ability to find
    possible coloring for the graph G = (V, E).

    Returns the coloring (correspondens between vertices and colors)

    # цикл з непарною кількістю вершин
    >>> print(colour_graph({1: {9, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3, 5}, \
6: {5, 7}, 7: {8, 6}, 5: {4, 6}, 8: {9, 7}, 9: {8, 1}}, ['white', 'red', 'black', 'green']))
    3

    # цикл з парною кількістю вершин
    >>> print(colour_graph({1: {2, 6}, 2: {1, 3}, 3: {2, 4}, 4: {3, 5}, 6: {1, 5}, 5: {4, 6}}, \
['white', 'red', 'black', 'green']))
    2

    # повний граф
    >>> print(colour_graph({4: {1, 2, 3, 4, 5, 6, 7, 8, 9},\
    9: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 5: {1, 2, 3, 4, 5, 6, 7, 8, 9},\
    1: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 8: {1, 2, 3, 4, 5, 6, 7, 8, 9},\
    2: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 6: {1, 2, 3, 4, 5, 6, 7, 8, 9},\
    7: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 3: {1, 2, 3, 4, 5, 6, 7, 8, 9}},\
    ['white', 'red', 'black', 'green', 'yellow', 'blue', 'pink', 'orange', 'dark blue']))
    9

    # двочастковий граф
    >>> print(colour_graph({2: {3, 4, 5, 6, 7, 8, 9}, 4: {1, 2}, 7: {1, 2},\
    1: {3, 4, 5, 6, 7, 8, 9}, 5: {1, 2}, 8: {1, 2}, 3: {1, 2}, 9: {1, 2},\
    6: {1, 2}}, ['white', 'red', 'black', 'green']))
    2

    >>> print(colour_graph({}, ['white', 'red', 'black', 'green']))
    {}
    '''

    vertices = sorted(list(graph.keys()))
    correspondens = set()
    for vertice in vertices:
        # determines what color will be used (the first one from
        # constant list of colors, which is not in vertice's
        # adjacency list)
        color = find_color(graph, colors, vertice)
        # add this pair (color, vertice) to the list of colorings
        correspondens.add((color, vertice))
        # colors vertices of graph in adjascency list
        # by means of replacing vertice with its color
        graph = colour_vertice(graph, color, vertice)

    coloured_vertices = {}
    for elm in correspondens:
        coloured_vertices.setdefault(elm[0], set()).add(elm[1])
    # this need to be changed to set (but for testing it will be list)
    coloured_vertices = {
        key: coloured_vertices[key] for key in coloured_vertices}

    return coloured_vertices


def find_color(graph: Dict[int, List[int]],
               colors: List[str], vertice: int) -> str:
    '''
    Finds first possible color, that a vertice can be painted with.
    '''

    for color in colors:
        if color not in graph[vertice]:
            return color

    return None


def colour_vertice(graph: Dict[int, List[int]],
                   color: str, vertice: int) -> Dict[int, List[int]]:
    '''
    Changes value (name) of vertice in nested adjacency lists
    into its corresponding color
    '''

    return {key: {color if elm == vertice else elm for elm in graph[key]}
            for key in graph.keys()}


if __name__ == "__main__":
    # testmod()
    from graph_io import read_adjacency_dict
    graph = read_adjacency_dict('graph.csv')
    print(colour_graph(graph, ['white', 'red', 'black', 'green',
                               'yellow', 'blue', 'pink', 'orange', 'dark blue']))
