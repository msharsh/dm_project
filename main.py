'''
This module contains funtions that implement the ability
to read info from file, build adjacency dictionary and
adjacency matrix

TODO: adjancency matrix for orientated graph
TODO: improve adjancency dict for orieentated graph
TODO: if someone will need to use weighed graph,
you should use matrix (which won't only be binary),
moreover, you will need to change some function here.

FEEL FREE TO MAKE CHANGES AND TO IMPROVE THIS FILE
'''

from typing import Dict, List, Tuple, Set
from pprint import pprint

import csv
import numpy as np

def read_file(path_to_file: str) -> Set[Tuple[int]]:
    '''
    This functions reads info from file with graph.
    Info should look like:
        int (which rerpresents first edge), int (second edge)

    Returns set of tuples of graph.
    '''

    with open(path_to_file, encoding='utf-8') as f:
        data = f.readlines()

    for idx, line in enumerate(data):
        data[idx] = tuple(map(int, line.rstrip().split(', ')))

    return set(data)

def dict_graph_orien(edges: set) -> Dict[int, Tuple[int]]:
    '''
    Creates adjacency dictionary, which keys are vertices and
    values are edges of the graph.
    It is not optimised well, however that's the first thing that I came up to
    for orientated graphs.
    '''

    graph = {}
    for edge in edges:
        graph.setdefault(edge[0] , set()).add(edge)
        graph.setdefault(edge[1] , set()).add(edge)

    return graph

def adjacency_dict(edges):
    '''
    Creates adjacency dictionary, which keys are vertices and
    values are vertices that have an edge with key-vertice.
    '''

    graph = {}
    for edge in edges:
        graph.setdefault(edge[0] , set()).add(edge[1])
        graph.setdefault(edge[1] , set()).add(edge[0])

    return graph

def adjacency_matrix(edges: Set[Tuple[int]], dtype='int8'):
    '''
    Build an adjacency_matrix for non-orientated graph

    Args: edges: set of tuples, that represent edges of the graph

    Returns: n*n matrix, matrix[i][j] == 1, if there is such an edge
    and == 0, if there is not.
    '''

    num_of_vertices = len(edges)
    # dtype is specified here as int8, however, it may need some changes
    # if you will need weighed edges
    matrix = np.zeros((num_of_vertices, num_of_vertices), dtype=dtype)
    # elements that are adjacent receives value of one
    for edge in edges:
        matrix[edge[0] - 1, edge[1] - 1] = 1

    return matrix

if __name__ == "__main__":
    graph = read_file('graphs')
    print(adjacency_dict(graph))
    print(adjacency_matrix(graph))
