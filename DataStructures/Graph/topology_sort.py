# https://www.youtube.com/watch?v=3tkcfvCNtM8


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

    def topology_sort(self):
        traverse_stack = []
        visited_stack = []

        for l_node in self.graph:
            if not l_node.get_visited():
                traverse_stack.append(l_node)
                while traverse_stack:
                    node = traverse_stack[len(traverse_stack)-1]
                    have_child = False
                    for n in node.get_neighbours():
                        if not n.get_visited():
                            traverse_stack.append(n)
                            have_child = True
                    if not have_child:
                        visited = traverse_stack.pop()
                        visited.set_visited()
                        visited_stack.append(visited)
        for node in visited_stack[::-1]:
            print(node, end=' ')

    def __str__(self):
        graph_string = ''
        for n in self.graph:
            graph_string += str(n)
            graph_string += ','
        return graph_string


graph = Graph()
for i in range(1, 9):
    graph.add_vertex('V'+str(i))

graph.add_directed_edge('B', 'A')
graph.add_directed_edge('B', 'D')
graph.add_directed_edge('A', 'D')
graph.add_directed_edge('D', 'C')
graph.add_directed_edge('D', 'E')
graph.add_directed_edge('G', 'F')
graph.add_directed_edge('G', 'D')
graph.add_directed_edge('F', 'E')
graph.add_directed_edge('H', 'F')
# graph.add_directed_edge

graph.topology_sort()