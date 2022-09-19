"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node
n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
(i.e., there is a directed edge from node i to node graph[i][j]).

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


Use an explicit stack
As we traverse the DAG, store the node along with the path leading to it. See sketch below.
image

https://leetcode.com/problems/all-paths-from-source-to-target/discuss/986429/Python-Iterative-DFS-with-detailed-time-complexity-and-visuals

Algo:

for every node store the node's value along with path



"""


def allPathsSourceTarget(graph):
    # edges cases:
    if not graph:
        return []

    # build di-graph
    d = {}
    for i in range(len(graph)):
        d[i] = graph[i]  # one-way link
    print(d)

    # apply DFS on DAG
    n = len(graph)
    stack = [(0, [0])]  # - store noth the (node, and the path leading to it)
    res = []
    while stack:
        node, path = stack.pop()
        # check leaf
        if node == n - 1:
            res.append(path)
        # traverse rest
        for nei in d[node]:
            stack.append((nei, path + [nei]))
    return res

print(allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
