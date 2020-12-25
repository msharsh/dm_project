from typing import Dict, List, Tuple, Set
import main
from pprint import pprint

def isEuler(graph: Dict[int, Tuple[int]]) -> bool:
    '''
    Checks whether graph has Euler cycle
    '''

    for edge in graph.keys():
        if len(graph[edge]) % 2 != 0:
            return False
    
    return True


if __name__ == "__main__":
    graph = main.read_graph('graphs')
    matrix = main.adjacency_matrix(graph)
    pprint(matrix)
    print(euler_path(matrix))