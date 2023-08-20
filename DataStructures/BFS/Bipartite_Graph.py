"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Certainly! Let's break down the approach step by step:

1. We are given an undirected graph represented as an adjacency list. The graph is a list of lists, where `graph[u]` contains the nodes that are adjacent to node `u`.

2. We want to determine if the given graph is bipartite. A graph is bipartite if we can partition its nodes into two sets such that every edge connects nodes from different sets.

3. To solve this problem, we will use a BFS (Breadth-First Search) traversal approach. The idea is to traverse the graph level by level, assigning colors to nodes in such a way that adjacent nodes have different colors.

4. We will use a `colors` array to keep track of the color assigned to each node. The colors we use are 1 and -1, where 1 represents Group A and -1 represents Group B. We initialize the `colors` array with zeros to indicate that no color has been assigned yet.

5. For each unvisited node in the graph, we perform a BFS traversal starting from that node:
   - We enqueue the current node into a queue.
   - We assign it to Group A by setting `colors[node] = 1`.
   - While the queue is not empty:
     - Dequeue the front node from the queue.
     - Iterate through its neighbors.
       - If the neighbor has not been visited yet (i.e., `colors[neighbor] == 0`), we assign it the opposite color of the current node and enqueue it.
       - If the neighbor has the same color as the current node, the graph cannot be bipartite, and we return `False`.

6. If we complete the BFS traversal without encountering any conflicts (i.e., same-colored neighbors), we can conclude that the graph is bipartite.

7. We repeat this process for all unvisited nodes in the graph.

8. If we have successfully traversed all nodes without finding any conflicts, we return `True`, indicating that the graph is bipartite.

9. Otherwise, if we find any conflicts during the BFS traversal, we return `False`, indicating that the graph is not bipartite.

The key insight here is that if a graph is bipartite, it means that we can divide its nodes into two sets, and no edge connects nodes within the same set. Using BFS to traverse the graph and assign colors allows us to identify cases where nodes are adjacent but have the same color, which would violate the bipartite property.
"""

from collections import deque


def isBipartite(graph):
    n = len(graph)
    colors = [0] * n  # 0: Not visited, 1: Group A, -1: Group B

    for node in range(n):
        if colors[node] == 0:
            queue = deque([node])
            colors[node] = 1

            while queue:
                current_node = queue.popleft()

                for neighbor in graph[current_node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[current_node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[current_node]:
                        return False

    return True


# Example usage
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(isBipartite(graph))  # Output: True

graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(isBipartite(graph))  # Output: False

