
def breadth_first_search(graph, start, end, path):
    path = path + [start]
    nodes = graph.children_of(start) + [start]
    for node in graph.children_of(nodes[-1]):
        if node == end:
            path = path + [node]
            return path
            break
    if start is not end and len(nodes) > 1:
        nodes.pop()
        path = breadth_first_search(graph, nodes[-1], end, path)
    elif len(nodes) == 1:
        return 'There is no path from ', start, ' to ', end
    return path
