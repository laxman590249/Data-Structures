

"""
An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1

Solution:

Do binary search
Everytime find the mid and check
if mid is greater then mid-1,
and mid is greater then mid+1 that will be your answer

Change mid according to the mid-1 and mid+1 values

"""

arr =  [-1, 1, 2, 3, 2, 1, 0, -1, -2]
low = 0
high = len(arr)-1


class Solution:
    def peakIndexInMountainArray(self, arr: list) -> int:
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid - 1]:
                high = mid
            else:
                low = mid

