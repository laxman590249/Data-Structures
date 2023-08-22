"""
96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty tree is considered a valid BST

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                # dp[j-1] is the number of unique BSTs for the left subtree
                # dp[i-j] is the number of unique BSTs for the right subtree
                dp[i] += dp[j - 1] * dp[i - j]
                print(dp, i, j)

        return dp[n]

# Example usage
n = 3
solution = Solution()
unique_bsts = solution.numTrees(n)
print(unique_bsts)  # Output: 5