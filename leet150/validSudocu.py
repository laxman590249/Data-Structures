"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


"""

class Solution:
    def isValidSudoku(self, board: list) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number != '.':
                    if f'{number} in row {i}' not in seen and f'{number} in column {j}' not in seen and f'{number} in block {i//3} - {j//3}' not in seen:
                        seen.add(f'{number} in row {i}')
                        seen.add(f'{number} in column {j}')
                        seen.add(f'{number} in block {i//3} - {j//3}')
                    else:
                        return False
        return True
