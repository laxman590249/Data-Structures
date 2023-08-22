"""

****
whenever you see max of(min) or min of(max) , 99.99% of the time its binary search.
****

https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.


Solution:

The approach goes like this -
We are iterating over the size of bags (which can range upto 10^9)
In each iteration we consider the mid to be the final penalty score that we can get after dividing the bag.
Considering the mid element as penalty score we calculate the number of operations required to reach that score.
If the number of operations required to reach the score is more than the maximum operations allowed,
then we move the left pointer to the mid + 1 so that we can have penalty score greater than before which can be
achieved by less number of operations. Similarly if the number of operations is less than max allowed operations
 than we can surely select a penalty score which is less than the current score therefore we shift right pointer
 to the mid in the hope that we will get a lower penalty score


Binary search the size of bag,
which is called penalty in this problem.

For each penalty value, we split the balls into bags with this value.
For example, the mid = 3,
A[i] = 2, we split it into [2], and operations = 0
A[i] = 3, we split it into [3], and operations = 0
A[i] = 4, we split it into [3,1], and operations = 1
A[i] = 5, we split it into [3,2], and operations = 1
A[i] = 6, we split it into [3,3], and operations = 1
A[i] = 7, we split it into [3,3,1], and operations = 2

The number of operation we need is (a - 1) / mid

If the total operation > max operations,
the size of bag is too small,
we set left = mid + 1

Otherwise,
this size of bag is big enough,
we set right = mid

We return the final result,
where result = left = right.


"""

"""
The is_feasible function checks if it's possible to achieve the maximum penalty less than or equal to the given value.
We use binary search to find the minimum possible penalty.
The search range is initially set from 1 to the maximum number of balls in any bag.
We iteratively adjust the search range by checking if the current mid penalty is feasible. 
If it is, we update the upper bound of the range; otherwise, we update the lower bound.

The binary search continues until the search range is narrowed down to a single value, which will be the minimum possible penalty.

"""


class Solution:
    def minimumSize(self, nums, maxOperations):
        def is_feasible(max_penalty):
            operations_needed = 0
            for balls in nums:
                operations_needed += (balls - 1) // max_penalty
            return operations_needed <= maxOperations

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2

            if is_feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left

