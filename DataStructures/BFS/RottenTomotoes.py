"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Solution:

Use BFS
> Use a Queue where you will add the starting position of all the rotting oranges
> Everytime use QUEUE and modiify the array and according to it update the queue
> Loop until the Queue is Empty

[[2,1,1],[1,1,0],[0,1,1]]

>
Queue -> [(0,0)]

Step1, Min1:
[(0,1), (1,0)]

Step1, Min2:
[(0,2), (1,1)]

so on etc...
"""