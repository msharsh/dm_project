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
