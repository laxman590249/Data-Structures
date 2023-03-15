"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

"""

class Solution:  # 28 ms, faster than 88.10%
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] != '0':  # Single digit
                dp[i] = dp[i+1]
            if i+1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):  # Two digits
                dp[i] += dp[i+2]
            print(dp)
        print(dp)
        return dp[0]

print(Solution().numDecodings("11106"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("111"))