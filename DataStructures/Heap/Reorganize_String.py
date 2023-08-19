"""
767. Reorganize String
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.


Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""


"""
from collections import Counter
import heapq


class Solution:

    def reorganizeString(self, S):
        res, c = [], Counter(S)
        pq = [(-value, key) for key, value in c.items()]
        heapq.heapify(pq)
        print(pq)
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
            print(pq)
        res = ''.join(res)
        if len(res) != len(S): return ""
        return res


print(Solution().reorganizeString('aaabbbccc'))
