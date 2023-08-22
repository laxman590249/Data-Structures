"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".


"""


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        word_set = set(wordDict)
        n = len(s)

        # dp[i] indicates whether the prefix s[:i] can be segmented into words
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

print(Solution().wordBreak("leetcode",  ["leet","code"]))
print(Solution().wordBreak("applepenapple",  ["apple","pen"]))
print(Solution().wordBreak("catsandog",  ["cats","dog","sand","and","cat"]))


