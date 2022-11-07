"""
Given an integer array nums,

return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

nums = [20,100,10,11,5,13]
True

Solution:

Find the first number
then second number
then if third number is greater then both return True


"""


class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False

print(Solution().increasingTriplet([20,100,10,11,5,13]))
