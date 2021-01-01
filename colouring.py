'''
This modules implements the ability to find
possible coloring for the graph G = (V, E)
'''

from main import read_file, adjacency_dict
from typing import Union, List, Dict, Set, Tuple


def colour_graph(graph: Dict[int, List[int]], colors: List[str])\
                 -> Set[Tuple[Union[str, int]]]:
    '''
    Implements the ability to find
    possible coloring for the graph G = (V, E).

    Returns the coloring (correspondens between vertices and colors)
    '''

    vertices = list(graph.keys())
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

    return correspondens


def find_color(graph: Dict[int, List[int]],
            colors: List[str], vertice: int) -> str:
    '''
    Finds first possible color, that a vertice can be painted with.
    '''

    for color in colors:
        if color not in graph[vertice]:
            return color


def colour_vertice(graph: Dict[int, List[int]],
                color: str, vertice: int) -> Dict[int, List[int]]:
    '''
    Changes value (name) of vertice in nested adjacency lists
    into its corresponding color
    '''

    return {key : [color if elm == vertice else elm for elm in graph[key]]\
            for key in graph.keys()}



if __name__ == "__main__":
    colors = ['white', 'red', 'black', 'green', 'yellow', 'blue', 'pink']
    edges = read_file('graphs')
    dct = adjacency_dict(edges)
    print(colour_graph(dct, colors))
