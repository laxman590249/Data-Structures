"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

"""

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

dp_matrix = [[0 for i in outer ] for outer in matrix]
print(dp_matrix)
max_number = 0
for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
        if i == 0 or j == 0:
            dp_matrix[i][j] = int(matrix[i][j])
        else:
            if int(matrix[i][j]):
                dp_matrix[i][j] = int(matrix[i][j])
            else:
                dp_matrix[i][j] = min(dp_matrix[i-1][j-1], dp_matrix[i-1][j], dp_matrix[i][j-1]) + 1
        if max_number < dp_matrix[i][j]:
            max_number = dp_matrix[i][j]
        print(dp_matrix)
print(dp_matrix)
print(max_number)




