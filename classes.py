# class Food(object):
#     def __init__(self, n, v, w):
#         self.name = n
#         self.value = v
#         self.calories = w
#
#     def getvalue(self):
#         return self.value
#
#     def getcost(self):
#         return self.calories
#
#     def density(self):
#         return self.getvalue() / self.getcost()
#
#     def __str__(self):
#         return self.name + ': <' + str(self.value) + ',' + str(self.calories) + '>'
#
#
# def build_menu(names, values, calories):
#     menu = []
#     for i in range(len(values)):
#         menu.append(Food(names[i], values[i], calories[i]))
#     return menu


class Node(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def __str__(self):
        return self.src.get_name() + ' -> ' + self.dest.get_name()


class Digraph(object):
    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_src()
        dest = edge.get_dest()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('node not in the graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for node in self.edges:
            if node.get_name() == name:
                return node
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in src:
                result += src.get_name() + ' -> ' + dest.get_name()
        return result


class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_dest, edge.get_src)
        Digraph.add_edge(self, rev)
