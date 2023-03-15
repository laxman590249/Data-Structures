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
        wordSet = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                # print(s[i:j], dp)
                if dp[j] and s[i:j] in wordSet:
                    dp[i] = True
                    break


        return dp[0]

print(Solution().wordBreak("leetcode",  ["leet","code"]))
print(Solution().wordBreak("applepenapple",  ["apple","pen"]))
print(Solution().wordBreak("catsandog",  ["cats","dog","sand","and","cat"]))


