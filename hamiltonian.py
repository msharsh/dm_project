import graph_io
import random
import os


def hamiltonian_cycle(graph, start_vertex):
    '''
    Retures hamilton cycle or absence message
    '''
    vertex_count = len(graph)
    to_visit = [None, start_vertex]
    path = []  # current path
    visited = set()  # same as path, used to quickly find unvisited verices
    while(to_visit):
        vertex = to_visit.pop()
        if vertex:
            path.append(vertex)

            # Check if we need to proceed
            path_len = len(path)
            last_in_path = path[path_len-1]
            if path_len == vertex_count and \
                    start_vertex in graph[last_in_path]:
                break

            visited.add(vertex)

            # Add adjacent vertices to visit
            unvisited = graph[vertex] - visited
            for x in unvisited:
                to_visit.extend([None, x])
        else:
            # if None - dead end -> remove last vertex from path and try another one
            visited.remove(path.pop())
    if len(path) > 0:
        return path
    return 'No solution exists'


if __name__ == "__main__":
    tests = os.listdir('tests')
    total = 0
    success = 0
    for i in tests:
        graph = graph_io.adjacency_dict(graph_io.read_file(f'tests/{i}'))
        for v in graph.keys():
            result = hamiltonian_cycle(graph, v)
            if len(result) > 0 and v in graph[result[len(result) - 1]]:
                success += 1
            total += 1
        print(f'Test: {i}\nResult: {result}')
    print('Succeed: {0}\nTotal: {1}'.format(success, total))
