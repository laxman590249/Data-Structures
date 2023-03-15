"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

"""


nums = [1,7,3,6,5,6]


class Solution:

    def pivot_index(self, nums):

        left_sum = nums[0]
        right_sum = nums[-1]
        left_index = 0
        right_index = len(nums) - 1

        while True:
            print(left_index, right_index, left_sum, right_sum)
            if left_sum < right_sum:
                left_index += 1
                left_sum += nums[left_index]
            elif left_sum > right_sum:
                right_index -= 1
                right_sum += nums[right_index]
            else:
                if left_index + 1 == right_index - 1:
                    return left_index + 1
                else:
                    return -1

print(Solution().pivot_index(nums))


