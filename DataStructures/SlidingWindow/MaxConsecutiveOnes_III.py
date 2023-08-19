"""
1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Solution:

Try to find the maximum window till the iteration and then iterate with this window.
If Window can be increased increase it otherwise traverse according to window
(Keep in mind we do not need to care about position of 1's and 0's we just need the maximum size of the window)

"""

nums = [1, 0, 0, 0, 0, 0, 0, 0]
k = 2

class Solution:
    def longestOnes(self, nums: list, k: int) -> int:
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
            # print(i, j, k)
        return j - i + 1

print(Solution().longestOnes(nums, k))