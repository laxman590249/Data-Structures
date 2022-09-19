"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Soultion:

Just do binary search
"""


def find_element(nums, target):
    index = -1
    left = 0
    right = len(nums)-1
    loop_count = 0
    while left < right:
        mid = left + (right-left+1)//2
        loop_count += 1
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid-1
        else:
            left = mid
    return -1

nums = [-1,0,3,5,9,12]
target = 3

print(find_element(nums, target))