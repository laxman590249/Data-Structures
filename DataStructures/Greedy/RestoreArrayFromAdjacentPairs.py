"""

There is an integer array nums that consists of n unique elements, but you have forgotten it.
However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that
the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs,
either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

Solution:

1. Use list and stack

Approach2:
2**.
    For each number, record its neighbours using a hash map. The number with only one neighbour is the head
    (or the tail) of the list.


"""
from collections import defaultdict

class Solution:

    def restoreArray(self, pairs):
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        result = []
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                result = [node, neighbors[0]]
                break

        while len(result) <= len(pairs):
            last, prev = result[-1], result[-2]
            candidates = graph[last]
            if candidates[0] != prev:
                result.append(candidates[0])
            else:
                result.append(candidates[1])

        return result


print(Solution().restoreArray([[4,-2],[1,4],[-3,1]]))
print(Solution().restoreArray([[2,1],[3,4],[3,2]]))
print(Solution().restoreArray([[100000,-100000]]))