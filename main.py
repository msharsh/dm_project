import sys
import os
# import graph_io_old as graph_io
import graph_io
import random
import colouring.colouring as colouring
import euler_cycle.euler_cycle as euler_cycle
import duality.duality as duality
import hamiltonian.hamiltonian as hamiltonian
from pprint import pp


def proceed_graph(file_path):
    graph = graph_io.read_adjacency_dict(file_path)
    print(f'Graph: {graph}')

    print(f'Euler cycle: {execute_euler_cycle(file_path)}')

    print(f'Hamiltonian cycle: {execute_hamiltonian_cycle(file_path)}')

    print(f'Colouring cycle: {execute_coloring(file_path)}')

    print(f'Duality: {execute_duality(file_path)}')


def execute_euler_cycle(file_path):
    graph = graph_io.read_adjacency_dict(file_path)
    parity = euler_cycle.verticles_parity(graph)
    return euler_cycle.euler_cycle_main(parity, file_path)


def execute_hamiltonian_cycle(file_path):
    graph = graph_io.read_adjacency_dict(file_path)
    start_vertex = random.choice(list(graph.keys()))
    return hamiltonian.hamiltonian_cycle(
        graph, start_vertex)


def execute_coloring(file_path):
    colors = ['white', 'red', 'black', 'green',
              'yellow', 'blue', 'pink', 'orange', 'dark blue']
    graph = graph_io.read_adjacency_dict(file_path)
    return len(colouring.colour_graph(graph, colors))


def execute_duality(file_path):
    sys.setrecursionlimit(8000)
    graph = graph_io.read_adjacency_dict(file_path)
    return duality.duality_check(
        duality.devided_vertices_create(graph), graph)


def test_function(func_to_test, expected_type, expected_value, file_path):
    result = func_to_test(file_path)
    if isinstance(result, expected_type):
        if expected_value:
            if expected_value == result:
                return True
            else:
                return False
        return True
    return False


def run_tests():
    tests = {'euler': (execute_euler_cycle, list, None),
             '3col': (execute_coloring, int, 3), 'bipartie': (execute_duality, bool, True), 'hamiltonian': (execute_hamiltonian_cycle, list, None)}
    for key, value in tests.items():
        print(f'-- Checking: {key}')
        failed = []
        succeed = []
        test_files = os.listdir(f'tests/{key}')
        for file_name in test_files:
            file_path = f'tests/{key}/{file_name}'
            if test_function(*value, file_path):
                succeed.append(file_path)
            else:
                failed.append(file_path)
        print('Positive result:\n', succeed)
        print('Negative result:\n', failed)
        print('*' * 20)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == '--test':
            run_tests()
        elif command == '--help':
            print('Arguments:')
            print('--test - runs all test cases')
            print('FILE_PATH - gets results for graph, located at FILE_PATH')
        else:
            if os.path.exists(command):
                proceed_graph(command)
            else:
                print('Incorrect path!')
    else:
        proceed_graph('graph.csv')
