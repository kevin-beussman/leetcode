# paint house
from typing import List
from functools import lru_cache

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # top-down DP
        # n = len(costs)

        # @lru_cache(None)
        # def dp(i,c): # i is the starting position
        #     if i == 0:
        #         return costs[i][c]
            
        #     if c == 0:
        #         return min(dp(i-1,1),dp(i-1,2)) + costs[i][c]
        #     elif c == 1:
        #         return min(dp(i-1,0),dp(i-1,2)) + costs[i][c]
        #     elif c == 2:
        #         return min(dp(i-1,0),dp(i-1,1)) + costs[i][c]
        
        # return min(dp(n-1,0),dp(n-1,1),dp(n-1,2))

        # bottom-up DP
        n = len(costs)
        if n == 1:
            return min(costs[0])

        dp = [[0]*3 for _ in range(min(n,2))]
        dp[0] = costs[0][:]

        for i in range(1,n):
            for c in range(3):
                dp[1][c] = min(dp[0][(c-1)%3],dp[0][(c-2)%3]) + costs[i][c]
            dp[0] = dp[1][:]
        
        return min(dp[1])
        
def main():
    costs = [[17,2,17],[16,2,5],[14,3,2]] # 10
    test = Solution()
    print(test.minCost(costs))

if __name__ == "__main__":
    main()