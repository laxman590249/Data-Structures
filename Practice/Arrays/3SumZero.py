"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


>>
Two Pointer approach
We will fix one digit, and we will start low and hi untill they collide
"""

class Solution:
    def threeSum(self, nums: list) -> list:
        n = len(nums)
        nums = sorted(nums)
        result = []
        for current in range(n):
            if current == 0 or nums[current] != nums[current-1]:
                low = current + 1
                hi = n-1
                current_number = nums[current]
                while low < hi:
                    current_sum = current_number + nums[low] + nums[hi]
                    if current_sum == 0:
                        result.append([current_number, nums[low], nums[hi]])
                        low += 1
                        hi -= 1
                        while low < hi and nums[low] == nums[low - 1]:
                            low += 1
                    elif current_sum < 0:
                        low += 1
                    else:
                        hi -= 1
        return result


