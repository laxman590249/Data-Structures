

INF = float('inf')
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[INF for i in range(vertices)] for i in range(vertices)]

    def floydWarshall(self):
        for k in range(self.V):
            # pick all vertices as source one by one
            for i in range(self.V):
                # Do not traverse the row if it is equal to k, because it is going to be unchanged
                if i != k:
                    # Pick all vertices as destination for the
                    # above picked source
                    for j in range(self.V):
                        # Do no check condition for same column as
                        if j != k:
                            self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])

        # for k in range(self.V):
        #     for i in range(self.V):
        #         for j in range(self.V):
        #             self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])
        print(self.graph)


graph = Graph(4)

graph.graph = [[0, 3, INF, 7],
         [8, 0, 2, INF],
         [5, INF, 0,   1],
         [2, INF, INF, 0]
         ]

graph.floydWarshall()

