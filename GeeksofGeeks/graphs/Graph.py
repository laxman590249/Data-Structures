

class Graph:

    def __init__(self):
        self.graph_nodes = {}

    def add_vertex(self, v):
        self.graph_nodes[v] = []

    def add_edge(self, v1, v2):
        self.graph_nodes.get(v1, []).append(v2)
        self.graph_nodes.get(v2, []).append(v1)

    def bfs_traverse(self):
        if not self.graph_nodes:
            print('Graph is Empty')
        else:
            queue = ["V0"]
            visited = ["V0"]
            while queue:
                node = queue.pop(0)
                nodes = self.graph_nodes.get(node, [])
                print(node, '->', end='')
                for n in nodes[::-1]:
                    if n not in visited:
                        visited.append(n)
                        queue.insert(0, n)

    def dfs_traverse(self):
        if not self.graph_nodes:
            print('Graph is Empty')
        else:
            stack = ["V0"]
            visited = ["V0"]
            while stack:
                node = stack.pop(len(stack)-1)
                nodes = self.graph_nodes.get(node, [])
                print(node, '->', end='')
                for n in nodes:
                    if n not in visited:
                        visited.append(n)
                        stack.append(n)
                # print(stack)

    def __str__(self):
        for key, value in self.graph_nodes.items():
            print(key, '->', value)
        return ''


graph = Graph()
graph.add_vertex('V0')
graph.add_vertex('V1')
graph.add_vertex('V2')
graph.add_vertex('V3')
graph.add_vertex('V4')

graph.add_edge('V0', 'V1')
graph.add_edge('V0', 'V4')
graph.add_edge('V1', 'V2')
graph.add_edge('V1', 'V3')
graph.add_edge('V1', 'V4')
graph.add_edge('V2', 'V3')
graph.add_edge('V3', 'V4')

print(graph)

graph.bfs_traverse()
print()
graph.dfs_traverse()





