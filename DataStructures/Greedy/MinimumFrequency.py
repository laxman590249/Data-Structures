"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

Solution:

So, count each character first. For each 26 characters, check if it's count is already used.
If so, delete characters until you find unused count, or reach zero.

"""

import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt, res, used = collections.Counter(s), 0, set()
        for ch, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res


print(Solution().minDeletions('aaabbbccd'))




