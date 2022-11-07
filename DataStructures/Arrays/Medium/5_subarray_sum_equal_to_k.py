"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Approach 1:

Cumulative array

"""

nums = [1,1,1],
k = 2
count = 0
sum_array = [0]
for i in range(len(nums)+2):
    sum_array.append(0)
print(sum_array)
i = 1
while i < len(sum_array):
    print(i)
    sum_array[i] = sum_array[i-1] + sum_array[i-1]
    i += 1
start = 0
end = 0
while start < len(sum_array):
    end = start + 1
    while end < len(sum_array):
        if sum_array[end] - sum_array[start] == k:
            count += 1
        end += 1
    start += 1

print(count)
