"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.


Solution:


First we explore all the land and then explore the corresponding water.
If there is all lands (i.e 1) then return -1.
For each BFS level we increase the distance.
Then we return the distance-1.
Explanation
First we put the coordinates of all lands(1) in the q;
Then we explore in all four directions if there is a 0 mark it as 1 and put into queue.
For each pass we increase the distance.
"""