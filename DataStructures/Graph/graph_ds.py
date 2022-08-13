

class GraphList:

    def __init__(self):
        self.ad_list = []
        self.graph_list = []

    def add_vertex(self, vertex, edges):
        self.graph_list.append(vertex)
        self.ad_list.append(edges)

    def bfs_traverse(self):
        if not self.ad_list:
            print('Graph is Empty')
        else:
            queue = [self.graph_list[0]]
            visited = []
            while queue:
                vertex = queue[0]
                edges = self.ad_list[self.graph_list.index(vertex)]
                queue.remove(vertex)
                if vertex not in visited:
                    print(f'{vertex}', end='->')
                    for node in edges:
                        if node not in visited:
                            queue.append(node)
                    visited.append(vertex)

    def dfs_traverse(self):
        if not self.ad_list:
            print('Graph is Empty')
        else:
            stack = [self.graph_list[0]]
            visited = []
            while stack:
                vertex = stack.pop()
                edges = self.ad_list[self.graph_list.index(vertex)]
                if vertex not in visited:
                    print(f'{vertex}', end='->')
                    for node in edges:
                        if node not in visited:
                            stack.append(node)
                    visited.append(vertex)


graph = GraphList()
graph.add_vertex('V2', ['V3', 'V5'])
graph.add_vertex('V3', ['V6', 'V10'])
graph.add_vertex('V5', ['V2', 'V8'])
graph.add_vertex('V8', ['V5', 'V9'])
graph.add_vertex('V9', ['V10', 'V6'])
graph.add_vertex('V6', ['V3', 'V9'])
graph.add_vertex('V8', ['V5', 'V9'])
graph.add_vertex('V10', ['V3', 'V9'])
graph.bfs_traverse()
print()
graph.dfs_traverse()











