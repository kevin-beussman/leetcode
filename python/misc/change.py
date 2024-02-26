from functools import lru_cache
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # @lru_cache(None)
        # def dp(amt,i):
        #     """ calculate number of ways to make amt using coins [i:]

        #     Args:
        #         amt (int): amount balance remaining
        #         i (int): index denoting which coins we can still use

        #     Returns:
        #         int: number of ways to make amt using coins[i:]
        #     """
        #     if amt == 0: # if we hit 0, good! return 1 (this is a solution)
        #         return 1
        #     if amt < 0: # if we go lower than 0, return 0 (not a solution)
        #         return 0
        #     if i >= len(coins): # if we run out of new coins to use
        #         return 0
        #     # use it or lose it, to make sure we only get unique solutions
        #     return dp(amt-coins[i],i) + dp(amt,i+1)
            
        # return dp(amount,0)

        # dp = [[0]*amount for _ in coins]
        dp = [0]*(amount+1)
        dp[0] = 1

        for i,c in enumerate(coins):
            for amt in range(c,amount+1):
                dp[amt] += dp[amt-c]
        
        print(dp)
        return dp[amount]

        
def main():
    amount = 6
    coins = [1,2,5]
    test = Solution()
    print(test.change(amount,coins))

if __name__ == "__main__":
    main()