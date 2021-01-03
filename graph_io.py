'''
This module contains functions that implement the ability
to read and write info to file, build adjacency dictionary and
adjacency matrix.

FEEL FREE TO MAKE CHANGES AND TO IMPROVE THIS FILE
'''

from typing import Dict, Tuple, Set
import numpy as np

def _read_file(path_to_file: str, fedinyak_tests: bool=True) -> Tuple[int, Set[Tuple[int]]]:
    '''
    This function reads info from file containing a graph.
    The file should contain multiple following lines for each edge:
        int (initial vertex num), int (terminal vertex num)

    Returns a set of tuples containing these edges.
    ''' 

    separator = ',' if not fedinyak_tests else ' '

    with open(path_to_file, encoding='utf-8') as file:
        if not fedinyak_tests:
            file.__next__()
        data = file.readlines()

    raw_data_set = set()
    unique_points_set = set()

    for line in data:
        initial, terminal = map(int, line.rstrip().split(separator))
        unique_points_set.add(initial)
        unique_points_set.add(terminal)
        raw_data_set.add((initial, terminal))
    
    number_of_vertices = len(unique_points_set)

    point_rename_map = {
        old_id:new_id
        for old_id, new_id in zip(
            list(unique_points_set),
            list(range(number_of_vertices))
        )
    }

    data_set = set()
    for initial, terminal in raw_data_set:
        data_set.add((point_rename_map[initial], point_rename_map[terminal]))

    return number_of_vertices, data_set


def _adjacency_dict(graph_data: Set[Tuple[int]], oriented: bool=False) -> Dict[int, Set[int]]:
    '''
    This function reads info from file containing a graph and
    creates an adjacency dictionary, where keys are vertices
    of the graph and values are their adjacent ones.
    The file should contain multiple following lines for each edge:
        int (initial vertex num), int (terminal vertex num)
    '''

    graph = {}
    for (initial, terminal) in graph_data:
        graph.setdefault(initial, set()).add(terminal)
        if not oriented:
            graph.setdefault(terminal, set()).add(initial)

    return graph


def _adjacency_matrix(
        number_of_vertices: int, graph_data: Set[Tuple[int]], oriented=False
    ) -> np.array:
    '''
    Build an adjacency matrix for a graph

    Args: edges: set of tuples, that represent edges of the graph

    Returns: n*n matrix, matrix[i][j] == 1, if there is such an edge
    and == 0, if there is not.
    '''

    matrix = np.zeros((number_of_vertices+1, number_of_vertices+1), dtype=bool)
    for (initial, terminal) in graph_data:
        matrix[initial, terminal] = True
        if not oriented:
            matrix[terminal, initial] = True

    return matrix


def read_adjacency_dict(
        path_to_file: str, oriented: bool=False, fedinyak_tests: bool=True
    ) -> Dict[int, Set[int]]:
    """
    Reads a graph from file and forms an adjacency dict
    """
    return _adjacency_dict(
        _read_file(path_to_file, fedinyak_tests=fedinyak_tests)[1],
        oriented=oriented
    )


def read_adjacency_matrix(
        path_to_file: str, oriented: bool=False, fedinyak_tests: bool=True
    ) -> np.array:
    """
    Reads a graph from file and forms an adjacency matrix
    """
    return _adjacency_matrix(
        *_read_file(path_to_file, fedinyak_tests=fedinyak_tests),
        oriented=oriented
    )


def write_adjacency_dict(
        graph: Dict[int, Set[int]], path_to_file: str, oriented: bool=False
    ):
    """
    Writes a graph to file, converting it from an adjacency dictionary.
    """

    with open(path_to_file, "w") as file:

        file.write("initial,terminal\n")

        if oriented:
            for initial in graph:
                for terminal in graph[initial]:
                    file.write(",".join(map(str, (initial, terminal))) + "\n")
        else:
            # remove all the conciding edges
            graph_edges = set()
            for initial in graph:
                for terminal in graph[initial]:
                    graph_edges.add((
                        min(initial, terminal),
                        max(initial, terminal)
                    ))

            for initial, terminal in graph_edges:
                file.write(",".join(map(str, (initial, terminal))) + "\n")


def write_adjacency_matrix(
        graph: np.array, path_to_file: str, oriented: bool=False
    ):
    """
    Writes a graph to file, converting it from an adjacency matrix.
    """

    with open(path_to_file, "w") as file:

        file.write("initial,terminal\n")
        number_of_vertices = max(graph.shape)

        for initial_id in range(number_of_vertices):
            for terminal_id in range(
                    0 if oriented else initial_id,
                    number_of_vertices
                ):
                if graph[initial_id, terminal_id]:
                    file.write(
                        ",".join(map(str, (initial_id, terminal_id))) + "\n"
                    )


def _main():
    """
    An interactive function of the module, demonstrating the main functions
    """

    write_adjacency_dict(
            read_adjacency_dict('graph.csv', oriented=True),
            "graph_out_dict.csv", oriented=True
    )
    write_adjacency_matrix(
            read_adjacency_matrix('graph.csv', oriented=True),
            "graph_out_matrix.csv", oriented=True
    )


if __name__ == "__main__":
    _main()
