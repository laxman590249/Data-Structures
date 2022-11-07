"""


"""
from functools import lru_cache

class Solution:

    def coinChange_2(self, coins: list, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]) + 1
        return -1 if dp[amount] == float('inf') else dp[amount]

print(Solution().coinChange_2([4, 5], 11))

