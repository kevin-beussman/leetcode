from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # # top down
        # n = len(prices)
        
        # # dp returns max profit starting on day i having used t transactions remaining, holding stock or not
        # @lru_cache(None)
        # def dp(i,t,h):
        #     if i == n-1:
        #         if h:
        #             return prices[i]
        #         else:
        #             return 0
        #     if h:
        #         return max(prices[i] + dp(i+1,t-1,False),dp(i+1,t,True))
        #     else:
        #         if t > 0:
        #             return max(-prices[i] + dp(i+1,t,True),dp(i+1,t,False))
        #         else:
        #             return dp(i+1,t,False)
        
        # return dp(0,k,False)

        # bottom up
        n = len(prices)
        
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for t in range(1,k+1):
                dp[i][t][0] = max(-prices[i] + dp[i+1][t][1], dp[i+1][t][0])
                dp[i][t][1] = max(prices[i] + dp[i+1][t-1][0], dp[i+1][t][1])
        
        return dp[0][k][0]
        
def main():
    k = 2
    prices = [3,2,6,5,0,3] # 7
    test = Solution()
    print(test.maxProfit(k,prices))

if __name__ == "__main__":
    main()