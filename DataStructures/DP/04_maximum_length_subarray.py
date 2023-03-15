"""

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.



Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

"""

class Solution(object):
    def findLength(self, A, B):
        current_max = 0
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
                    if memo[i][j] > current_max:
                        current_max = memo[i][j]
        for m in memo:
            print(m)
        return current_max


# print(Solution().findLength([0,0,0,0,0], [0,0,0,0,0]))
print(Solution().findLength([1,2,3,2,1], [3,2,1,4,7]))
