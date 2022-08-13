"""
Given a directed graph, find out if a vertex v is reachable from another vertex u for all vertex pairs (u, v) in the
given graph. Here reachable means that there is a path from vertex u to v. The reach-ability matrix is called
transitive closure of a graph.

For example, consider below graph

Transitive closure of above graphs is
     1 1 1 1
     1 1 1 1
     1 1 1 1
     0 0 0 1

1> Use floyed warshall algo
2> Using DFS

    Below are the abstract steps of the algorithm.
    Create a matrix tc[V][V] that would finally have transitive closure of the given graph.
    Initialize all entries of tc[][] as 0.
    Call DFS for every node of the graph to mark reachable vertices in tc[][]. In recursive calls to DFS,
    we don’t call DFS for an adjacent vertex if it is already marked as reachable in tc[][].

"""