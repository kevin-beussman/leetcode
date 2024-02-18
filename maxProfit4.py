# max profit with transaction fee
from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # # top-down
        # n = len(prices)
        
        # @lru_cache(None)
        # def dp(i,h):
        #     if i == n-1:
        #         if h:
        #             return max(0,prices[i] - fee)
        #         else:
        #             return 0
            
        #     if not h:
        #         # if not holding, 2 choices: buy or not
        #         buy = dp(i+1,1) - prices[i]
        #         notbuy = dp(i+1,0)
        #         return max(buy, notbuy)
        #     else:
        #         # if holding, 2 choices: sell or not
        #         sell = dp(i+1,0) + prices[i] - fee
        #         notsell = dp(i+1,1)
        #         return max(sell, notsell)
            
        # return dp(0,0)

        # bottom-up
        n = len(prices)
        
        dp = [[0]*2 for _ in range(2)] # constant space since we don't need future results past i+1
        dp[-1][1] = max(0,prices[n-1] - fee)

        for i in range(n-2,-1,-1):
            for h in range(2):
                if not h:
                    buy = dp[1][1] - prices[i]
                    notbuy = dp[1][0]
                    dp[0][h] = max(buy, notbuy)
                else:
                    sell = dp[1][0] + prices[i] - fee
                    notsell = dp[1][1]
                    dp[0][h] = max(sell, notsell)
            dp[1] = dp[0][:]
        
        return dp[0][0]

        
def main():
    prices = [1,3,2,8,4,9]
    fee = 2
    # prices = [1,3,7,5,10,3]
    # fee = 3
    test = Solution()
    print(test.maxProfit(prices, fee))

if __name__ == "__main__":
    main()