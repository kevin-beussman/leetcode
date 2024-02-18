# Domino and Tromino Tiling
#from typing import List, Optional
from functools import lru_cache
#import heapq

class Solution:
    def numTilings(self, n: int) -> int:
        # 2xn board size
        
        # calculate fully covered and partially coverd boards for each k
        # only need to consider partially covered where top-right is empty due to symmetry

        # top-down DP
        # @lru_cache
        # def dp(k):
        #     if k == 0:
        #         return (1,0)
        #     elif k == 1:
        #         return (1,0)
            
        #     fm1,pm1 = dp(k-1) # full for k-1, partial for k--1
        #     fm2,pm2 = dp(k-2)
        #     full = (fm1 + fm2 + pm1*2) % (10**9 + 7)
        #     part = (fm2 + pm1) % (10**9 + 7)
        #     return (full,part)
        
        # return dp(n)[0]

        # bottom-up DP
        dp = [(1,0)]*(n+1) # number of full, partial coverings
        for k in range(2,n+1):
            fm1,pm1 = dp[k-1]
            fm2,pm2 = dp[k-2]
            full = (fm1 + fm2 + pm1*2) % (10**9 + 7)
            part = (fm2 + pm1) % (10**9 + 7)
            dp[k] = (full,part)
        
        return dp[n][0]

def main():
    n = 5
    test = Solution()
    print(test.numTilings(n))

if __name__ == "__main__":
    main()