"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


Solution:

We have to select K start either from start or end.
So if we chose k cards from start then we chose 0 card from end
If we chose k-1 cards from start then we chose 1 card from end
...
..
This is how it goes, do we can just create DP solution where we maintain the sum from end as well in every run

Above can be done by creaing two extra list
1. write a list from o to k sum
2. write a list from last to last-k list
3. Then iterate through using both list and find the required sum

"""

# Below
class Solution:
    def maxScore(self, cardPoints: list, k: int) -> int:
        def get_max(cardPoints, i, j, k):
            if k == 1 or i >= j:
                return max(cardPoints[i], cardPoints[j])
            left_max = get_max(cardPoints, i + 1, j, k - 1) + cardPoints[i]
            right_max = get_max(cardPoints, i, j - 1, k - 1) + cardPoints[j]
            return max(left_max, right_max)

        if len(cardPoints) == k:
            return sum(cardPoints)
        return get_max(cardPoints, 0, len(cardPoints) - 1, k)

# print(Solution().maxScore([30,88,33,37,18,77,54,73,31,88,93,25,18,31,71,8,97,20,98,16,65,40,18,25,13,51,59], 26))

class Solution2:
    def maxScore(self, cardPoints: list, k) -> int:

         start = k-1
         end = len(cardPoints)-1
         start_sum = 0
         end_sum = 0
         max_sum = 0
         start = 0
         while start < k:
             start_sum += cardPoints[start]
             start += 1
         start -= 1
         max_sum = start_sum
         while start >= 0:
             # print(start, end, max_sum)
             start_sum -= cardPoints[start]
             end_sum += cardPoints[end]
             max_sum = max(start_sum + end_sum, max_sum)
             start -= 1
             end -= 1

         return max_sum

print(Solution2().maxScore([30,88,33,37,18,77,54,73,31,88,93,25,18,31,71,8,97,20,98,16,65,40,18,25,13,51,59], 26))
