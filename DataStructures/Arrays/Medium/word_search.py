"""


"""

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"


class Solution:
    def search(self, i, j, board, word):
        print(word, i, j)
        if i < 0 or i >= len(board) or j >= len(board[0]) or j < 0:
            return False
        elif board[i][j] == word[0]:
            if len(word) == 1:
                return True
            up =  self.search(i-1, j, board, word[1:])
            bottom = self.search(i + 1, j, board, word[1:])
            right = self.search(i, j+1, board, word[1:])
            left = self.search(i, j-1, board, word[1:])
            if up or left or right or bottom:
                return True
        else:
            return False


    def word_serach_utils(self, board, word):
        found = [False]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == word[0]:
                    result = self.search(i, j, board, word)
                    if result:
                        found[0] = result
        return found[0]

print(Solution().word_serach_utils(board, word))

