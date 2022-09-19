
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def addEdge(self, s, d):
        self.graph[s] = self.graph.get(s, [])
        if d != None:
            self.graph[s].append(d)

    def dfs(self, source):
        visited = []
        stack = [source]
        # print(self.graph)
        while stack:
            vertex = stack.pop()
            edges = self.graph[vertex]
            visited.append(vertex)
            for edge in edges:
                if edge not in visited:
                    stack.append(edge)
        return visited

    def find_inverse(self):
        inverse = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                inverse.addEdge(j, i)
        for i in self.graph:
            if i not in inverse.graph:
                inverse.graph[i] = []
        return inverse

    def isSC(self):
        source = 0
        dfs_list = self.dfs(source)
        if len(dfs_list) == self.V:
            inverse = self.find_inverse()
            inverse_dfs = inverse.dfs(source)
            if len(inverse_dfs) == self.V:
                return True
        return False

# Create a graph given in the above diagram
g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(2, 4)
g1.addEdge(4, 2)
print ("Yes" if g1.isSC() else "No")

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
g2.addEdge(3, None)
print ("Yes" if g2.isSC() else "No")