"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Approach:

1. Negative Marking
You can just modify the list and make the index of the number to negative. So again if that number comes if that index
value is negative then you can just say it is already there


2. Binary Search
Search the possible number with the help of binary search from 0 to N
count the number less then that number if it is equal to that number then Answer will be in right side
if it is more then the number then solution can be there in left side
we do it again and again until we find the number
complexity n Log n

"""

class Solution:
    def findDuplicate(self, nums: list) -> int:
        low = 1
        high = len(nums) - 1

        while low <= high:
            cur = (low + high) // 2
            count = 0
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1

        return duplicate

print(Solution().findDuplicate([3, 3, 3, 2, 4]))
