import sys
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def minDistance(self, dist, sptset):
        min = sys.maxsize
        min_index = -1
        for index in range(self.V):
            if not sptset[index] and dist[index] < min:
                min = dist[index]
                min_index = index
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptset = [False] * self.V

        for count in range(self.V):

            x = self.minDistance(dist, sptset)
            sptset[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and self.graph[x][y] + dist[x] < dist[y]:
                    dist[y] = self.graph[x][y] + dist[x]
                    if sptset[y]:
                        sptset[y] = False

        for i in range(self.V):
            print(src, '->', i, ': ', dist[i])


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]

g.dijkstra(0)
