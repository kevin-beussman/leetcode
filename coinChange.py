from typing import List
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state variables:
        # current total
        # return: minimum number of coins to reach 0

        # @lru_cache(maxsize=None)
        # def dp(t):
        #     if t == 0:
        #         return 0
            
        #     temp = amount # inf
        #     for c in coins:
        #         if c <= t:
        #             temp = min(temp,dp(t-c))
        #     return temp + 1
        
        # result = dp(amount)
        # if result == amount + 1:
        #     return -1
        # else:
        #     return result
        
        dp = [amount+1]*(amount+1) # dp probably doesn't need to be longer than the largest coin size
        # dp = [amount+1]*(max(coins)+1)
        dp[0] = 0

        for t in range(1,amount+1):
            for c in coins:
                if c <= t:
                    dp[t] = min(dp[t],dp[t-c] + 1)

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]


coins = [9]
amount = 13
test = Solution()
print(test.coinChange(coins,amount))