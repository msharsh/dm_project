'''
This module contains functions that implement the ability
to read and write info to file, build adjacency dictionary and
adjacency matrix.
'''

from typing import Dict, Tuple, Set
from itertools import chain
import numpy as np

def read_file(path_to_file: str) -> Set[Tuple[int]]:
    """
    This function reads info from file containing a graph.
    The file should contain multiple following lines for each edge:
        int (initial vertex num), int (terminal vertex num)

    Returns a set of tuples containing these edges.
    """

    with open(path_to_file, encoding='utf-8') as file:
        # if you assume that there will be the first line
        # you can simply write file.next() (because files
        # are actually iterators)
        data = file.readlines()

    # doesn't get your idea to count vertices in function,
    # that reads the file, if you need this, write other function
    # (you might use itertools.chain for this, or some comprehension)
    #
    # number_of_vertices = 0
    # data_set = set()

    return {tuple(map(int, line.rstrip().split(','))) for line in data}
    #for idx, line in enumerate(data):
        #initial, terminal = map(int, line.rstrip().split(','))
        #number_of_vertices = max(number_of_vertices, initial, terminal)
        #data_set.add((initial, terminal))
#
    #return number_of_vertices, data_set


def count_vertices(set_of_edges: Set[int]) -> int:
    """
    Counts edges of graph
    """

    return len(set(chain(*set_of_edges)))

def adjacency_dict(graph_data: Set[Tuple[int]], oriented: bool=False) -> Dict[int, Set[int]]:
    """
    This function reads info from file containing a graph and
    creates an adjacency dictionary, where keys are vertices
    of the graph and values are their adjacent ones.
    The file should contain multiple following lines for each edge:
        int (initial vertex num), int (terminal vertex num)
    """

    graph = {}
    for (initial, terminal) in graph_data:
        graph.setdefault(initial, set()).add(terminal)
        if not oriented:
            graph.setdefault(terminal, set()).add(initial)

    return graph

# NO -> need to be rewritten, because I changed the first function
# doesn't like this thou
def adjacency_matrix(number_of_vertices: int, graph_data: Set[Tuple[int]],
                    oriented=False) -> np.array:
    """
    Build an adjacency matrix for a graph

    Args: edges: set of tuples, that represent edges of the graph

    Returns: n*n matrix, matrix[i][j] == 1, if there is such an edge
    and == 0, if there is not.
    """

    # I don't think that this is efficient enough to work with such an ugly relisation
    matrix = np.zeros((number_of_vertices+1, number_of_vertices+1), dtype=bool)
    for (initial, terminal) in graph_data:
        matrix[initial, terminal] = True
        if not oriented:
            matrix[terminal, initial] = True

    return matrix


def read_adjacency_dict(path_to_file: str, oriented: bool=False) -> Dict[int, Set[int]]:
    """
    Reads a graph from file and forms an adjacency dict
    """

    # that's good, but what for?
    return adjacency_dict(read_file(path_to_file)[1], oriented=oriented)


def read_adjacency_matrix(path_to_file: str, oriented: bool=False) -> np.array:
    """
    Reads a graph from file and forms an adjacency matrix
    """
    # that's good, but what for?
    return adjacency_matrix(*read_file(path_to_file), oriented=oriented)


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


def main():
    """
    An interactive function of the module.
    """

    write_adjacency_dict(
            read_adjacency_dict('graph.csv'),
            "graph_out_dict.csv",
    )
    write_adjacency_matrix(
            read_adjacency_matrix('graph.csv'),
            "graph_out_matrix.csv",
    )


if __name__ == "__main__":
    main()
