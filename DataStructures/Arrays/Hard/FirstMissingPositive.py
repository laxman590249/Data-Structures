"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Input: nums = [1,2,0]
Output: 3

Algorithm:

It works on the logic to update the index of its correspondenct number if its present in the list

"""


class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] // n == 0:
                return i
        return n

