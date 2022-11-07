"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]




"""
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

top = 0
left = 0
right = len(matrix[0])-1
bottom = len(matrix)-1

last = ''
i = 0
j = 0
result = []
while True:
    if last == '' or last == 'UP':
        j = left
        i = top
        if j > right:
            break
        while j <= right:
            result.append(matrix[i][j])
            j += 1
        top += 1
        last = 'RIGHT'
    elif last == 'RIGHT':
        i = top
        j = right
        if i > bottom:
            break
        while i < bottom:
            result.append(matrix[i][j])
            i += 1
        last = 'DOWN'
        right -= 1
    elif last == 'DOWN':
        i = bottom
        j = right
        if j < left:
            break
        while j >= left:
            result.append(matrix[i][j])
            j -= 1
        last = 'LEFT'
        bottom -= 1
    else:
        i = left
        j = bottom
        if i < top:
            break
        while i >= top:
            result.append(matrix[i][j])
            i -= 1
        last = 'UP'
        left += 1

print(result)


