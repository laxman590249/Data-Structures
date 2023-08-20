"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8

1. Start from the top right corner
count the negative numbers in each columns

2. Do Binary Search in each row, find the last negative and find the count of the negative

"""


class Solution:
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        count = 0

        for row in grid:
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += n - left  # Add the count of negative numbers in the row

        return count





