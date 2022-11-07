"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

"""
nums = [4,3,2,7,8,2,3,1]
max_num = max(nums)
i = 0
while i < len(nums):
    nums[(nums[i]-1)%max_num] = (nums[i] % max_num) + max_num
    i += 1
res  = []
print(nums)
for index, value in enumerate(nums):
    if value / max_num > 1:
        res.append(index+1)
print(res)

