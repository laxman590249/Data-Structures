"""
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        start, max_len = 0, 1
        for i in range(n):
            odd = s[i - max_len - 1: i + 1]
            even = s[i - max_len: i + 1]
            # print('odd:', odd, ' even:' ,even,'i:', i,'start:', start,'max_lan:',  max_len, i - max_len - 1, i - max_len)
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
        return s[start: start + max_len]

print(Solution().longestPalindrome('abcdeedcba'))
