"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]


Solution 1:

1) Store the first d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]

Solution 2 **:

    nums = "----->-->"; k =3
    result = "-->----->";

reverse "----->-->" we can get "<--<-----"
reverse "<--" we can get "--><-----"
reverse "<-----" we can get "-->----->"

"""


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


nums = [1, 2, 3, 4, 5, 6, 7]
n = len(nums)-1
k = 9
start = 0
reverse(nums, 0, k % n)
reverse(nums, 0, k % n-1)
reverse(nums, k % n, n)

print(nums)
