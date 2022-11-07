"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

"""

class Solution:

    def jump_possible(self, nums):
        farthest = nums[0]
        if len(nums) == 1:
            return True
        for jump in range(len(nums)):
            farthest = max(farthest, nums[jump] + jump)
            print(farthest)
            if farthest >= len(nums)-1:
                return True
            if farthest == jump:
                return False
        return False

print(Solution().jump_possible([2, 0, 0]))
