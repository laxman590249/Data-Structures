

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

    @staticmethod
    def dfsVisit(node_1):
        node_1.set_visited()
        print(node_1, end=' ')
        for node in node_1.get_neighbours():
            if not node.get_visited():
                Graph.dfsVisit(node)

    def __init__(self):
        self.graph = []

    def add_vertex(self, name):
        self.graph.append(Node(name))

    def add_undirected_edge(self, vertex_1, vertex_2):
        v_1 = [x for x in self.graph if x.name == vertex_1][0]
        v_2 = [x for x in self.graph if x.name == vertex_2][0]
        v_1.set_neighbours(v_2)
        v_2.set_neighbours(v_1)

    def add_directed_edge(self, vertex_1, vertex_2):
        v_1 = [x for x in self.graph if x.name == vertex_1][0]
        v_2 = [x for x in self.graph if x.name == vertex_2][0]
        v_1.set_neighbours(v_2)

    def reset_nodes(self):
        for node in self.graph:
            node.set_unvisited()

    def bfs_traversal(self):
        if not self.graph:
            print('Graph is Empty, Try to create adnd traverse')
            return
        else:
            node = self.graph[0]
            queue = [node]
            while queue:
                node = queue.pop(0)
                if not node.get_visited():
                    print(node, end=' ')
                    node.set_visited()
                    for n in node.get_neighbours():
                        queue.append(n)
        print()

    def dfs_traversal(self):
        if not self.graph:
            print('Graph is Empty, Try to create and traverse')
            return
        else:
            stack = [self.graph[0]]
            while stack:
                node = stack.pop()
                if not node.get_visited():
                    print(node, end=' ')
                    node.set_visited()
                    for n in node.get_neighbours():
                        stack.append(n)

    def dfs(self):
        for node in self.graph:
            if not node.get_visited():
                Graph.dfsVisit(node)

    def __str__(self):
        graph_string = ''
        for n in self.graph:
            graph_string += str(n)
            graph_string += ','
        return graph_string


# graph = Graph()
# graph.add_vertex('V2')
# graph.add_vertex('V3')
# graph.add_vertex('V5')
# graph.add_vertex('V6')
# graph.add_vertex('V8')
# graph.add_vertex('V9')
# graph.add_vertex('V10')
#
# graph.add_directed_edge('V2', 'V3')
# graph.add_directed_edge('V2', 'V5')
# graph.add_directed_edge('V3', 'V6')
# graph.add_directed_edge('V3', 'V10')
# graph.add_directed_edge('V5', 'V8')
# graph.add_directed_edge('V9', 'V10')
# graph.add_directed_edge('V9', 'V6')
# graph.add_directed_edge('V8', 'V9')
# #
# graph.dfs()
# graph.reset_nodes()
# print()
# graph.dfs_traversal()
# graph.reset_nodes()
# print()
# graph.bfs_traversal()
#
# graph = Graph()
# for i in range(1, 11):
#     graph.add_vertex('V'+str(i))
#
# graph.add_undirected_edge('V1', 'V2')
# graph.add_undirected_edge('V1', 'V4')
# graph.add_undirected_edge('V2', 'V3')
#
# graph.add_undirected_edge('V2', 'V5')
# graph.add_undirected_edge('V3', 'V6')
# graph.add_undirected_edge('V3', 'V10')
#
# graph.add_undirected_edge('V4', 'V7')
# graph.add_undirected_edge('V5', 'V8')
# graph.add_undirected_edge('V6', 'V9')
#
# graph.add_undirected_edge('V7', 'V8')
# graph.add_undirected_edge('V8', 'V9')
# graph.add_undirected_edge('V9', 'V10')
# print('Started 2')

# for i in range(1, 8):
#     graph.add_vertex('V'+str(i))
#
# graph.add_undirected_edge('V1', 'V2')
# graph.add_undirected_edge('V1', 'V3')
# graph.add_undirected_edge('V2', 'V4')
# graph.add_undirected_edge('V2', 'V5')
# graph.add_undirected_edge('V3', 'V6')
# graph.add_undirected_edge('V3', 'V7')
# graph.bfs_traversal()
# graph.reset_nodes()
# graph.dfs()
# graph.reset_nodes()
# print()
# graph.dfs_traversal()






