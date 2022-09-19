"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks,
return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater
than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Solution:

Consider that each local maximum is one valid peak.
My solution is to find one local maximum with binary search.
Binary search satisfies the O(logn) computational complexity.


"""


def find_peak(nums, left, right):
    if left == right:
        return left
    mid = (left+right)//2
    if nums[mid] > nums[mid+1]:
        return find_peak(nums, left, mid)
    else:
        return find_peak(nums, mid+1, right)


nums =[1,2,1,3,5,6,4]
print(find_peak(nums, 0, len(nums)-1))
