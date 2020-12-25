from typing import Dict, List, Tuple, Set
from pprint import pprint

def read_graph(path_to_file: str) -> Set[Tuple[int]]:
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

def dict_graph(edges: set) -> Dict[int, Tuple[int]]:
    '''
    Converts set of vertices into dict, where key is
    edge.
    '''

    graph = {}
    for edge in edges:
        graph.setdefault(edge[0] , set()).add(edge)
        graph.setdefault(edge[1] , set()).add(edge)

    return graph

def adjacency_matrix(graph):
    
    columns = sorted([elm[0] for elm in graph])
    
    matrix = [[0 for _ in range(len(columns))] for _ in range(len(columns))]
    for elm in graph:
        matrix[elm[0] - 1][elm[1] - 1] = 1
    
    return matrix

if __name__ == "__main__":
    graph = read_graph('graphs')
    print(adjacency_matrix(graph))