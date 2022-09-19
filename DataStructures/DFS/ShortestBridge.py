"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Solution**:

https://leetcode.com/problems/shortest-bridge/discuss/189293/C%2B%2B-BFS-Island-Expansion-%2B-UF-Bonus

"""


grid = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0]]

def paint(i, j, value):
    grid[i][j] = value
    if j < len(grid[i])-1 and grid[i][j+1] == 1:
        paint(i, j+1, value)
    if i < len(grid[i])-1 and grid[i+1][j] == 1:
        paint(i+1, j, value)
    if 1 != 0 and grid[i-1][j] == 1:
        paint(i-1, j, value)
    if j != 0 and grid[i][j-1] == 1:
        paint(i, j-1, value)

for k,i in enumerate(grid):
    found = False
    for l,j in enumerate(i):
        if j == 1:
            paint(k, l, 2)
            found = True
            break
    if found:
        break


print(grid)



