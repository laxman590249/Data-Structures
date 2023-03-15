

class ShortestPath:

    def find_minimum_index(self, distance, visited):
        min = float('inf')
        min_index = -1
        for index, value in enumerate(distance):
            if not visited[index] and  value < min:
                min = value
                min_index = index
        return min_index

    def dijkstra(self, graph, source):
        nodes = len(graph)
        distance = [float('inf')] * nodes
        visited = [False] * nodes
        distance[source] = 0
        while True:
            min_index = self.find_minimum_index(distance, visited)
            visited[min_index] = True
            if min_index == -1:
                break
            else:
                for index in range(0, nodes):
                    if graph[min_index][index] != 0 and distance[index] > distance[min_index] + graph[min_index][index]:
                        distance[index] = distance[min_index] + graph[min_index][index]
                        visited[index] = False
        return distance


graph =  [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ],
                [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ],
                [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ],
                [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ],
                [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ],
                [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ],
                [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ],
                [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ],
                [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] ]
t = ShortestPath()
print(t.dijkstra(graph, 0))