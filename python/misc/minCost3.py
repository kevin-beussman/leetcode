# paint house 3
from typing import List
from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # top-down DP
        # @lru_cache(None)
        # def dp(i,j,k): # k acts as as counter for the number of neighborhoods we can add
        #     if k < 1:
        #         return float("inf")
        #     if houses[i] and houses[i] != j:
        #         return float("inf")
        #     if i+1 < k:
        #         return float("inf")
        #     if i == 0:
        #         if houses[i]:
        #             return 0
        #         else:
        #             return cost[i][j-1]
            
        #     mincost = float("inf")
        #     for c in range(1,n+1):
        #         if c == j:
        #             if houses[i]:
        #                 mincost = min(mincost, dp(i-1,c,k))
        #             else:
        #                 mincost = min(mincost, dp(i-1,c,k) + cost[i][j-1])
        #         else:
        #             if houses[i]:
        #                 mincost = min(mincost, dp(i-1,c,k-1))
        #             else:
        #                 mincost = min(mincost, dp(i-1,c,k-1) + cost[i][j-1])
                        
        #     return mincost
        
        # ans = min(dp(m-1,color,target) for color in range(1,n+1))
        # if ans == float("inf"):
        #     return -1
        # else:
        #     return ans


        # bottom-up DP
        dp = [[[float("inf")]*(target+1) for _ in range(n)] for _ in range(m)]
        if houses[0]:
            dp[0][houses[0]-1][1] = 0
        else:
            for j in range(1,n+1):
                dp[0][j-1][1] = cost[0][j-1]

        for k in range(1,target+1):
            for i in range(1,m):
                if houses[i]:
                    #check dp[i-1] and find min (updating k if dp[i-1] has same color as houses[i])
                    mincost = float("inf")
                    for c in range(1,n+1):
                        if c == houses[i]:
                            dp[i][houses[i]-1][k] = min(dp[i][houses[i]-1][k], dp[i-1][c-1][k])
                        else:
                            dp[i][houses[i]-1][k] = min(dp[i][houses[i]-1][k], dp[i-1][c-1][k-1])
                else:
                    for j in range(1,n+1):
                        if houses[i-1]:
                            if houses[i-1] == j:
                                dp[i][j-1][k] = min(dp[i][j-1][k], dp[i-1][houses[i-1]-1][k] + cost[i][j-1])
                            else:
                                dp[i][j-1][k] = min(dp[i][j-1][k], dp[i-1][houses[i-1]-1][k-1] + cost[i][j-1])
                        else:
                            for c in range(1,n+1):
                                if c == j:
                                    dp[i][j-1][k] = min(dp[i][j-1][k], dp[i-1][c-1][k] + cost[i][j-1])
                                else:
                                    dp[i][j-1][k] = min(dp[i][j-1][k], dp[i-1][c-1][k-1] + cost[i][j-1])
        
        ans = min(dp[m-1][j][target] for j in range(n))
        if ans == float("inf"):
            return -1
        else:
            return ans
        
def main():
    # houses = [0,2,1,2,0] # 11
    # # houses = [0,0,0,0,0] # 9
    # # houses = [2,1,1,0,0] # 2
    # cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    # m = 5
    # n = 2
    # target = 3

    # houses = [3,1,2,3] # -1
    # cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
    # m = 4
    # n = 3
    # target = 3

    houses = [2,3,0]
    cost = [[5,2,3],[3,4,1],[1,2,1]]
    m = 3
    n = 3
    target = 3
    test = Solution()
    print(test.minCost(houses,cost,m,n,target))

if __name__ == "__main__":
    main()