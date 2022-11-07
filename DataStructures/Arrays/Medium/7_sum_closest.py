"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Solution:

1. Two pointers
2. Binary search with two fix and find the third close one

"""


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        sorted_nums = sorted(nums)
        result_sum = sorted_nums[0] + sorted_nums[1] + sorted_nums[2]
        min_difference = abs(target - result_sum)
        for i in range(0, len(nums) - 1):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                current_sum = sorted_nums[i] + sorted_nums[lo] + sorted_nums[hi]
                if current_sum == target:
                    return current_sum

                if abs(target - current_sum) < min_difference:
                    min_difference = abs(target - current_sum)
                    result_sum = current_sum
                if current_sum >= target:
                    hi -= 1
                else:
                    lo += 1
        return result_sum

print(Solution().threeSumClosest([1,1,1,0], -100))




