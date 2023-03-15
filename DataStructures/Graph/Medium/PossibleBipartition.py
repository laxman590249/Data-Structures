"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some
other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not
like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].

Solution:

Implement the graph
Find the graph do have any circle or not
"""


class Solution:

    def is_bipartition(self, n, dislikes):

        adjacency = [list() for i in range(n+1)]
        color = [-1] * (n+1)

        for dislike in dislikes:
            adjacency[dislike[0]].append(dislike[1])
            adjacency[dislike[1]].append(dislike[0])

        for index in range(1, n+1):
            if color[index] == -1:
                if self.dfs(color, adjacency, index):
                    return False
        return True

    def dfs(self, color, adjacency, index):
        if color[index] == -1:
            color[index] = 1

        for new_index in adjacency[index]:
            if color[new_index] == -1:
                color[new_index] = 1 - color[index]
                if self.dfs(color, adjacency, new_index):
                    return True
            elif color[new_index] == color[index]:
                return True
        return False


print(Solution().is_bipartition(4, [[1, 2], [1, 3], [2, 4]]))
print(Solution().is_bipartition(3, [[1, 2], [1, 3], [2, 3]]))






