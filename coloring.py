'''
This module implements the ability to determine
whether a graph can be coloured and if it can,
returns this coloring.

It uses Backtracking algorithm for the
determination of the chromatic number χ(G) of the graph G = (V, E).

TODO: Thanks to some idiot on geekforgeeks, who posted his shity realisation
that doesn't work, this need to be rewritten
'''

from main import read_file, adjacency_matrix

from itertools import chain
from typing import Union, List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

COLORS = ['white', 'red', 'black', 'green', 'yellow', 'blue', 'pink']

def safe_to_coloue(graph, vertice, colors: List, curent_color: str):
    # print((graph, vertice, colors, curent_color))
    for i in range(len(graph)):
        try:
            if graph[vertice][i] == 1 and colors[i] == curent_color:
                return False
        except IndexError:
            continue

    return True


def is_colourable(graph: List[List[int]], colors: List[str], vertice: int):
    '''
    '''
    # print(colors, vertice)
    if vertice == len(graph):
        return True

    for color in range(3):
        if safe_to_coloue(graph, vertice, colors, color):
            colors[vertice] = color
            if is_colourable(graph, colors, vertice + 1):
                return True
            colors[vertice] = 0

def show_graph(matrix, colors):
    '''
    '''

    if isinstance(matrix, list):
        matrix = np.array(matrix)
    rows, cols = np.where(matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    # it's obviously easy to make this label some color, however, need to think how to
    # make a node coloured indeed
    colors = [COLORS[color - 1] for color in colors]
    nx.draw(gr, node_size=500, labels = dict(zip(gr.nodes(), colors)), with_labels=True)
    plt.show()

def colour_graph(graph: List[List[int]], num_of_colors):
    '''
    >>> print(colour_graph([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]], 3))
    True
    '''

    # creates list of available colors
    colors = [color for idx, color in enumerate(COLORS) if idx <= num_of_colors]
    if not is_colourable(graph, colors, 0):
        return False

    show_graph(graph, colors)

    return True


if __name__ == "__main__":
    edges = read_file('graphs')
    mtx = adjacency_matrix(edges)
    
    print(colour_graph(mtx, 4))

