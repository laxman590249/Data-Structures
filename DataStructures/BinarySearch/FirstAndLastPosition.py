"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Solution:

Can be done with two iterative binary search

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)

For the right part:

The solution is by using a small trick: instead of calculating mid as mid = (i+j)/2, we now do:

mid = (i+j)/2+1

Why does this trick work? When we use mid = (i+j)/2, the mid is rounded to the lowest integer.
In other words, mid is always biased towards the left. This means we could have i == mid when j - i == mid,
but we NEVER have j == mid. So in order to keep the search range moving, you must make sure the new i is set to
something different than mid, otherwise we are at the risk that i gets stuck. But for the new j,
it is okay if we set it to mid, since it was not equal to mid anyways. Our two rules in search of the left boundary
happen to satisfy these requirements, so it works perfectly in that situation. Similarly,
 when we search for the right boundary, we must make sure i won't get stuck when we set the new i to i = mid.
 The easiest way to achieve this is by making mid biased to the right, i.e. mid = (i+j)/2+1.

"""

element = 10
nums = [5,7,7,8, 8,8,8,8,10]

left = 0
right = len(nums)-1

def find_element(nums, left, right, element):
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == element:
            index = mid
            return index
        if nums[mid] > element:
            right = mid
        else:
            left = mid+1
    return -1

def find_index(nums, element):
    last_left = -1
    last_right = -1
    result_index = find_element(nums, 0, len(nums) - 1, element)
    print(result_index)
    result_index_old = result_index
    if result_index == -1:
        return [-1, -1]
    last_left = result_index
    last_right = result_index
    while True:
        print('left', result_index)
        result_index = find_element(nums, 0, result_index-1, element)

        if result_index != -1:
            last_left = result_index
        else:
            break
    while True:
        print(result_index_old)
        result_index_old = find_element(nums, result_index_old+1, len(nums) - 1, element)
        if result_index_old != -1:
            last_right = result_index_old
        else:
            break
    return [last_left, last_right]

print(find_index(nums, element))







