

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def BellmanFord(self, src):

        dist = [float('inf')] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for source, destination, weight in self.graph:
                if dist[source] != float('inf') and dist[source] + weight < dist[destination]:
                    dist[destination] = dist[source] + weight

            print(dist)

        for i in range(self.V):
            print(src, '-> ', i, ': ', dist[i])

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
# Print the solution
g.BellmanFord(4)