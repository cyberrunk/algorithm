def depth_first_search(graph, start, end, path, shortest, to_print=False):
    # path += [start]
    path = path + [start]
    if to_print:
        print('Current DSP path: ', print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:
            if shortest is None or len(path) < len(shortest) - 1:
                new_path = depth_first_search(graph, node, end, path, shortest, to_print)
                if new_path is not None:
                    shortest = new_path
        elif to_print:
            print('Already visited ', node)
    return shortest


def shortest_path(graph, start, end, to_print=False):
    return depth_first_search(graph, start, end, [], None, to_print)


def print_path(nodes):
    path = ''
    for node in nodes:
        path += str(node) + ' -> '
    return path[:-3]
