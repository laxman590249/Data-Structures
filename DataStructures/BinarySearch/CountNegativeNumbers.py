"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8

Start from the top right corner
count the negative numbers in each columns


"""

grid = [[5, -1, -1, -1],
        [-1, 2, -1, -1],
        [1, -1, -2, -2],
        [-1, -1, -2, -3]]

count = 0
m = len(grid)-1
n = len(grid[0])-1

i = 0
j = n

while j != -1 and i != m:
    if grid[i][j] >= 0:
        i += 1
    else:
        # print(i, j)
        if j == 0:
            count += (m - i + 1)
            j -= 1
        elif grid[i][j-1] >= 0:
            count += (m - i + 1)
            i += 1
            j -= 1
        else:
            count += (m - i + 1)
            j -= 1

print(count)


