"""This module contains necessary functions
to find Euler cycle in undirected graph.
"""
import copy
from typing import List
from graph_io import read_adjacency_dict
def verticles_parity(dict_graph:dict)->bool:
    """
    Returns True if if all verticles of graph are even and False otherwise.
    >>> verticles_parity(read_adjacency_dict('euler_100_121_try1.csv'))
    True
    >>> verticles_parity(read_adjacency_dict('euler_100_69_try2.csv'))
    False
    """
    all_varticles_even= True
    for i in dict_graph:
        if len(dict_graph[i])%2 !=0:
            all_varticles_even = False
            break
    return all_varticles_even

def find_euler_cycles(initial_dict:dict,dict_graph:dict,verticle:int)-> List[list]:
    """Returns list of Euler cycles of all parts of undirected graph.
    >>> find_euler_cycles(read_adjacency_dict('euler_100_121_try1.csv'),\
read_adjacency_dict('euler_100_121_try1.csv'), 1)
    [[2, 4, 6, 47, 2], [73, 37, 41, 74, 81, 38, 70, 7, 40, 67, 34, 8, 68,\
 62, 55, 99, 68, 67, 54, 35, 47, 26, 23, 22, 9, 51, 43, 72, 1, 82, 20, 100,\
 16, 69, 60, 50, 28, 21, 92, 66, 70, 18, 89, 91, 3, 49, 45, 39, 15, 27, 30,\
 36, 10, 34, 12, 71, 75, 83, 33, 14, 88, 65, 44, 13, 90, 94, 93, 76, 98, 32,\
 11, 17, 80, 31, 33, 24, 19, 85, 100, 99, 78, 42, 95, 48, 46, 29, 87, 5, 97,\
 98, 59, 91, 58, 95, 96, 88, 81, 53, 73, 63, 69, 82, 79, 73], [83, 52, 56, 57,\
 25, 61, 83], [92, 77, 84, 64, 87, 86, 98, 99, 92]]
    """
    cycles = []
    graph_copy = copy.deepcopy(dict_graph)

    for i in dict_graph:
        if graph_copy[i] == set():
            del graph_copy[i]

    if graph_copy == {}:
        return cycles

    next_verticle = None
    if verticle not in graph_copy:
        for i in graph_copy:
            if len(initial_dict[i])>2:
                verticle=i
                break
    while True:
        if graph_copy[verticle] == set():
            break
        cycles.append(verticle + 1)
        next_verticle = min(graph_copy[verticle])
        graph_copy[verticle].remove(next_verticle)
        graph_copy[next_verticle].remove(verticle)
        verticle = next_verticle

    cycles.append(verticle + 1)
    cycles = [cycles]

    return cycles+find_euler_cycles(initial_dict, graph_copy, verticle)

def cycles_union(cycles:List[list])->list:
    """Returns whole Euler cycle, which consists of all smaller euler cycles.
    >>> cycles_union(find_euler_cycles(read_adjacency_dict('euler_100_121_try1.csv'),\
read_adjacency_dict('euler_100_121_try1.csv'), 0))
    [1, 72, 43, 51, 9, 22, 23, 26, 47, 2, 4, 6, 47, 35, 54, 67, 34, 8, 68, 62,\
 55, 99, 68, 67, 40, 7, 70, 18, 89, 91, 3, 49, 45, 39, 15, 27, 30, 36, 10, 34,\
 12, 71, 75, 83, 52, 56, 57, 25, 61, 83, 33, 14, 88, 65, 44, 13, 90, 94, 93, 76,\
 98, 32, 11, 17, 80, 31, 33, 24, 19, 85, 100, 16, 69, 60, 50, 28, 21, 92, 66, 70,\
 38, 81, 53, 73, 63, 69, 82, 79, 73, 37, 41, 74, 81, 88, 96, 95, 42, 78, 99, 92, 77,\
 84, 64, 87, 5, 97, 98, 59, 91, 58, 95, 48, 46, 29, 87, 86, 98, 99, 100, 20, 82, 1]
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
    >>> euler_cycle_main(verticles_parity(read_adjacency_dict('euler_100_121_try1.csv')),\
'euler_100_121_try1.csv')
    [1, 72, 43, 51, 9, 22, 23, 26, 47, 2, 4, 6, 47, 35, 54, 67, 34, 8, 68, 62,\
 55, 99, 68, 67, 40, 7, 70, 18, 89, 91, 3, 49, 45, 39, 15, 27, 30, 36, 10, 34,\
 12, 71, 75, 83, 52, 56, 57, 25, 61, 83, 33, 14, 88, 65, 44, 13, 90, 94, 93, 76,\
 98, 32, 11, 17, 80, 31, 33, 24, 19, 85, 100, 16, 69, 60, 50, 28, 21, 92, 66, 70,\
 38, 81, 53, 73, 63, 69, 82, 79, 73, 37, 41, 74, 81, 88, 96, 95, 42, 78, 99, 92, 77,\
 84, 64, 87, 5, 97, 98, 59, 91, 58, 95, 48, 46, 29, 87, 86, 98, 99, 100, 20, 82, 1]
    >>> euler_cycle_main(verticles_parity(read_adjacency_dict('euler_100_69_try2.csv')),\
 'euler_100_69_try2.csv')
    "This graph doesn't have an Euler cycle."
    """
    if not all_varticles_even:
        return "This graph doesn't have an Euler cycle."
    start_verticle = min(read_adjacency_dict(file_path))
    graph_copy = copy.deepcopy(read_adjacency_dict(file_path))
    cycles = find_euler_cycles(read_adjacency_dict(file_path),graph_copy,start_verticle)
    whole_cycle = cycles_union(cycles)
    return whole_cycle


if __name__ == "__main__":
    path_to_file = "euler_1000_1190_try1.csv"
    print(euler_cycle_main(verticles_parity(read_adjacency_dict(path_to_file)),
                           path_to_file))
