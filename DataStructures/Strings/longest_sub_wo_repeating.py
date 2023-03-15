"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
                print('Start', start)
            else:
                maxLength = max(maxLength, i - start + 1)
                print('maxLength', maxLength)

            usedChar[s[i]] = i
            print(usedChar)

        return maxLength
