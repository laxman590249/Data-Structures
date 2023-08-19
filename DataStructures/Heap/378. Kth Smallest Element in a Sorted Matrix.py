"""
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solutions/1322101/c-java-python-maxheap-minheap-binary-search-picture-explain-clean-concise/
Solution(2)

Consider it like:

find the smalled element from n sorted lists
Create a Min Heap and put the information about each rows element.
Eveytime pop the element and add the next element according to popped out element

"""
from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        minHeap = []
        for r in range(min(k, m)):
            heappush(minHeap, (matrix[r][0], r, 0))
        ans = -1
        for i in range(k):
            ans, r, c = heappop(minHeap)
            if c+1 < n:
                heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        return ans


print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 4))
