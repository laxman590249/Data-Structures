class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.is_visited = False

    def __str__(self):
        return self.name

    def set_neighbours(self, node):
        self.neighbors.append(node)

    def get_neighbours(self):
        return self.neighbors

    def set_visited(self):
        self.is_visited = True

    def set_unvisited(self):
        self.is_visited = False

    def get_visited(self):
        return self.is_visited


class Graph:

    def __init__(self):
        self.graph = []

    def add_vertex(self, name):
        self.graph.append(Node(name))

    def add_directed_edge(self, vertex_1, vertex_2):
        v_1 = [x for x in self.graph if x.name == vertex_1][0]
        v_2 = [x for x in self.graph if x.name == vertex_2][0]
        v_1.set_neighbours(v_2)

    def reset_nodes(self):
        for node in self.graph:
            node.set_unvisited()

    def __str__(self):
        graph_string = ''
        for n in self.graph:
            graph_string += str(n)
            graph_string += ','
        return graph_string


graph = Graph()
for i in range(1, 9):
    graph.add_vertex('V'+str(i))

graph.add_directed_edge('V1', 'V3')
graph.add_directed_edge('V2', 'V3')
graph.add_directed_edge('V3', 'V5')
graph.add_directed_edge('V5', 'V6')
graph.add_directed_edge('V5', 'V7')
graph.add_directed_edge('V7', 'V8')
graph.add_directed_edge('V2', 'V4')
graph.add_directed_edge('V4', 'V7')
print(graph)

