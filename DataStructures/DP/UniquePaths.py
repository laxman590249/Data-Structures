"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
 bottom-right corner.

 Test Case m= 3, n =7, Output 28
 Test Case m= 3, n =2, Output 3


DP Table,
We can create a matrix of m * n and try to find from first point to last point with number of ways

DP[i][j] = DP[i-1][j] + DP[i][j-1]

"""