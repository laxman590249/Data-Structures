class Solution:
    def rotate(self, matrix:list) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def print_maxt(self, matrix):
        print('--->')
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                print(matrix[i][j], end = ' ')
            print('')


    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                print(i, j)
                self.print_maxt(matrix)

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

mat = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]]

Solution().print_maxt(mat)

Solution().rotate(mat)