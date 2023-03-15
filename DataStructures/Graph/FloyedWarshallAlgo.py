"""
To find all the distances by finding distances with intermediate vertex.

We keep maintain the Matrix[V,V] and in every loop we try to find the Matrix by any vertex.

A1 : All distance from vertex 1
A2: All distance from vertex 2
..
..
An: Final matrix gives the result

"""


INF = float('inf')


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[INF for i in range(vertices)] for i in range(vertices)]

    def floydWarshall(self):
        for k in range(self.V):
            for i in range(self.V):
                if i != k:
                    for j in range(self.V):
                        if j != k:
                            self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])
            print(self.graph)
        # print(self.graph)


graph = Graph(4)

graph.graph = [[0, 3, INF, 7],
         [8, 0, 2, INF],
         [5, INF, 0,   1],
         [2, INF, INF, 0]
         ]

graph.floydWarshall()

