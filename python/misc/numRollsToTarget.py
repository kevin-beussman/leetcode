# Number of Dice Rolls With Target Sum
#from typing import List, Optional
from functools import lru_cache
#import heapq

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # top-down DP
        # @lru_cache(None)
        # def dp(j,t):
        #     nonlocal k
        #     if t == 0 and j == 0:
        #         # print(p)
        #         return 1
        #     elif t < 0 or j == 0:
        #         return 0
            
        #     temp = 0
        #     for roll in range(1,k+1):
        #         temp += dp(j-1,t-roll)
            
        #     return temp % (10**9 + 7)

        # return dp(n,target)

        # bottom-up DP
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1

        for j in range(1,n+1):
            for t in range(1,target+1):
                for roll in range(1,min(t+1,k+1)):
                    dp[j][t] = (dp[j][t] + dp[j-1][t-roll]) % (10**9 + 7)

        return dp[n][target]

def main():
    n = 2 # 6
    k = 6
    target = 7

    n = 30 # 222_616_187
    k = 30
    target = 500

    # n = 3 # 36
    # k = 18
    # target = 10

    test = Solution()
    print(test.numRollsToTarget(n,k,target))

if __name__ == "__main__":
    main()