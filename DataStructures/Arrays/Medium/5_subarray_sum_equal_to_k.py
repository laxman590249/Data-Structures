"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Approach 1:

Prefix sum, Linear Approach


"""
nums = [1, -1, 1, 1, 1, 1]

class Solution:

    def find_subarrays_count(self, nums, k):
        prefix_sum = { 0: 1}
        total_sum = 0
        result = 0
        for num in nums:
            total_sum += num
            prefix = total_sum - k
            result += prefix_sum.get(prefix, 0)
            prefix_sum[total_sum] = prefix_sum.get(total_sum, 0) + 1
        return result

print(Solution().find_subarrays_count([1, -1, 1, 1, 1, 1], k=3))