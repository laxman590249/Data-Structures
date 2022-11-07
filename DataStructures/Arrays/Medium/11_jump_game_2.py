"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.


Solution:

In this algo we will go for Greedy algo
We will find the current run upto where
In the current run what will be the meximum reach we can make
when the current jump will be finished we will assign current jump ending to maximum reach
again we will be doing the same

"""


class Solution:

    def jump(self, nums: list) -> int:
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps



print(Solution().jump([6, 5, 3, 2, 3, 4, 4, 3, 6, 1, 2, 2, 2, 1]))


