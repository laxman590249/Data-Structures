"""

1> One list is used to maintain all the nodes
2> all linked nodes are attached to it side wise

"""

class Node:

    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:

    def __init__(self, virtices):
        self.V = virtices
        self.graph = [None for i in range(self.V)]

    def add_edge(self, src, dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def show_graph(self):

        for index, node in enumerate(self.graph):
            temp = node
            print(f'Adjacency list of Vertex: {index}')
            print(f'head ', end='')
            while temp:
                print('->', temp.vertex, end='')
                temp = temp.next


V = 5
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.show_graph()


