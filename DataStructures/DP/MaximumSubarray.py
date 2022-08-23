"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Solution:

https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts

We will create a DP array and everytime we will iterate trhough the array we will update the current
value of DP array. If previous value of DP array is positive then we will add it with current otherwise we will not add
it into the DP array


"""


class Solution:

    def maxSubArray(self, nums: list) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_value = dp[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] >= 0 else 0)
            max_value = max(max_value, dp[i])
        print(max_value)
        return max_value


Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
Solution().maxSubArray([1])
Solution().maxSubArray([5, 4, -1, 7, 8])
