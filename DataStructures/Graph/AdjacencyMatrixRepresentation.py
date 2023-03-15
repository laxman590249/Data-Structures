"""
1. Can be represented by N*N matrix
2. Should be used if it is complete graph or near to complete graph

"""

if __name__ == '__main__':
    print('Write Size of the Graph: ')
    n, m = map(int, input().split())
    adjMat = [[0 for i in range(n)]for j in range(n)]
    # Edges
    print('Write all edges: ')
    for i in range(n):
        u, v = map(int, input().split())
        adjMat[u][v] = 1
        adjMat[v][u] = 1
    print(adjMat)