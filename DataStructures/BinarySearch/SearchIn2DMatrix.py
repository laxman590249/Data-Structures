"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.



Solution:

Consider the 2D array as 1D array and find the required index according to mid calculated

in M*N matrix

x = M*N//N
Y = M*N%N
"""

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = -1
m = 3
n = 4
left = 0
right = m*n-1

res_x =-1
res_y = -1

while left <= right:
    mid = left + (right-left)//2
    x = mid // n
    y = mid % n
    print(mid, left, right)
    if matrix[x][y] == target:
        res_x = x
        res_y = y
        break
    if mid == 0:
        break
    if matrix[x][y] < target:
        left = mid+1
    else:
        right = mid
print(res_x, res_y)


