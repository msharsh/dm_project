"""This module contains necessary functions
to find Euler cycle in undirected graph.
"""

import copy
from typing import List
from graph_io import read_adjacency_dict


def verticles_parity(dict_graph:dict)->bool:
    """
    Returns True if if all verticles of graph are even and False otherwise.
    >>> verticles_parity(read_adjacency_dict('graphs.csv'))
    True
    >>> verticles_parity(read_adjacency_dict('graph.csv'))
    False
    """

    all_varticles_even= True
    for i in dict_graph:
        if len(dict_graph[i])%2 !=0:
            all_varticles_even = False
            break

    return all_varticles_even


def find_euler_cycles(dict_graph:dict,verticle:int)-> List[list]:
    """Returns list of Euler cycles of all parts of undirected graph.
    >>> find_euler_cycles(read_adjacency_dict('graphs.csv'), 0)
    [[1, 2, 3, 4, 5, 1]]
    """

    cycles = []
    graph_copy = copy.deepcopy(dict_graph)

    for i in dict_graph:
        if dict_graph[i] == set():
            del graph_copy[i]

    if graph_copy == {}:
        return cycles

    next_verticle = None

    while True:
        if graph_copy[verticle] == set():
            break
        cycles.append(verticle + 1)
        next_verticle = min(graph_copy[verticle])
        graph_copy[verticle].remove(next_verticle)
        graph_copy[next_verticle].remove(verticle)
        verticle = next_verticle
    cycles.append(verticle + 1)

    verticle = None
    for i in cycles:
        if dict_graph[i-1]!= set():
            verticle = i

    cycles = [cycles]
    if verticle is None:
        return cycles

    return cycles+find_euler_cycles(graph_copy,verticle)


def cycles_union(cycles:List[list])->list:
    """Returns whole Euler cycle, which consists of all smaller euler cycles.
    >>> cycles_union(find_euler_cycles(read_adjacency_dict('graphs.csv'), 0))
    [1, 2, 3, 4, 5, 1]
    """

    cycle = []
    for i in cycles:
        if cycles.index(i)==0:
            cycle.extend(i)
        else:
            place_to_insert = cycle.index(i[0])
            cycle = cycle[0:place_to_insert]+i+cycle[place_to_insert+1:]
    return cycle


def euler_cycle_main(all_varticles_even:bool,file_path:str)->list:
    """Returns list of verticles, which creates Euler cycle if graph has Euler cycle
    and message of its absence otherwise.
    >>> euler_cycle_main(verticles_parity(read_adjacency_dict('graphs.csv')),'graphs.csv')
    [1, 2, 3, 4, 5, 1]
    >>> euler_cycle_main(verticles_parity(read_adjacency_dict('graph.csv')), 'graph.csv')
    "This graph doesn't have an Euler cycle."
    """

    if not all_varticles_even:
        return "This graph doesn't have an Euler cycle."

    start_verticle = min(read_adjacency_dict(file_path))
    cycles = find_euler_cycles(read_adjacency_dict(file_path),start_verticle)
    whole_cycle = cycles_union(cycles)

    return whole_cycle


if __name__ == "__main__":
    print(euler_cycle_main(verticles_parity(read_adjacency_dict('graphs.csv')), 'graphs.csv'))