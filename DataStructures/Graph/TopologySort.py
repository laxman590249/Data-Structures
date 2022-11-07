

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_directed_edge(self, source, destination):
        edeg_list = self.adjacency_list.get(source, [])
        edeg_list.append(destination)
        self.adjacency_list[destination]  = self.adjacency_list.get(destination, [])
        self.adjacency_list[source] = edeg_list


def topology_sort(graph) -> list:

    visited = {key:False for key,value in graph.adjacency_list.items()}

    def get_anynode(visited):
        for i, j in visited.items():
            if not j:
                return i
        return -1
    ans_stack = []
    stack = []
    while True:
        if len(stack) == 0:
            node = get_anynode(visited)
        else:
            node = stack.pop()
        if node == -1:
            print(ans_stack[::-1])
            return ans_stack
        else:
            print('Node', node)
            adjacency = graph.adjacency_list[node]
            visited[node] = True
            found = False
            for n in adjacency:
                if not visited[n]:
                    stack.append(n)
                    found = True
            if not found:
                ans_stack.append(node)
            print(visited)
            print(ans_stack)

graph = Graph()
graph.add_directed_edge('B', 'A')
graph.add_directed_edge('B', 'D')
graph.add_directed_edge('A', 'D')
graph.add_directed_edge('D', 'C')
graph.add_directed_edge('D', 'E')
graph.add_directed_edge('G', 'F')
graph.add_directed_edge('G', 'D')
graph.add_directed_edge('F', 'E')
graph.add_directed_edge('H', 'F')
print(topology_sort(graph))
