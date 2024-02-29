

from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

                print(end, queue, seen)

        return False

Solution().wordBreak('applepenapple', ["apple","pen"])