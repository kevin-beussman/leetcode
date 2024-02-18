# paint house 2
from typing import List
from functools import lru_cache

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # top-down DP
        # n = len(costs)
        # ncolor = len(costs[0])

        # @lru_cache(None)
        # def dp(i,c): # i is the starting position
        #     if i == 0:
        #         return costs[i][c]
            
        #     return min(dp(i-1,(c-j)%ncolor) for j in range(1,ncolor)) + costs[i][c]
        
        # return min(dp(n-1,j) for j in range(ncolor))

        # bottom-up DP O(n*k^2)
        # n = len(costs)
        # ncolor = len(costs[0])
        # if n == 1:
        #     return min(costs[0])

        # dp = [[0]*ncolor for _ in range(min(n,2))]
        # dp[0] = costs[0][:]

        # for i in range(1,n):
        #     for c in range(ncolor):
        #         dp[1][c] = min(dp[0][(c-j)%ncolor] for j in range(1,ncolor)) + costs[i][c]
        #     dp[0] = dp[1][:]
        
        # return min(dp[1])

        # bottom-up DP O(n*k)
        n = len(costs)
        ncolor = len(costs[0])

        mindp = [[0]*2 for _ in range(2)] # 2 lowest values of dp from prev and current step
        minc = [0]*2 # indices for the first lowest value of dp from prev and current step
        
        for i in range(0,n):
            mindp[1] = [float("inf")]*2
            minc[1] = 0
            for c in range(ncolor):
                if c != minc[0]:
                    ans = mindp[0][0] + costs[i][c]
                else:
                    ans = mindp[0][1] + costs[i][c]
                
                if ans <= mindp[1][0]:
                    mindp[1][1] = mindp[1][0]
                    mindp[1][0] = ans
                    minc[1] = c
                elif ans < mindp[1][1]:
                    mindp[1][1] = ans
            
            mindp[0] = mindp[1][:]
            minc[0] = minc[1]
            
        return mindp[1][0]
        
def main():
    # costs = [[2,7,2,5,6,8,12],[2,9,4,1,2,9,14],[2,9,4,1,2,9,14],[2,9,4,1,2,9,14],[2,9,4,1,2,9,14]]
    # costs = [[1,5,3],[2,9,4]]
    # costs = [[8,16,12,18,9],[19,18,8,2,8],[8,5,5,13,4],[15,9,3,19,2],[8,7,1,8,17],[8,2,8,15,5],[8,17,1,15,3],[8,8,5,5,16],[2,2,18,2,9]]
    # 28
    costs = [[7,19,11,3,7,15,17,5,6,18,1,15,18,11],[13,18,18,8,13,12,11,13,4,8,2,4,5,20],[14,5,18,4,7,6,1,6,11,6,16,6,13,17],[18,17,11,3,12,4,8,6,2,7,10,9,19,3],[4,3,2,14,11,15,18,1,17,1,6,14,14,9],[9,13,15,14,5,1,1,6,11,15,16,12,10,18],[19,2,11,3,13,4,13,7,16,16,20,18,20,8],[8,19,20,9,18,13,17,1,2,4,3,20,15,9],[9,10,11,6,14,20,4,1,5,15,13,10,13,5],[13,11,9,11,9,16,3,19,1,11,6,7,12,13],[14,1,15,14,11,12,7,14,12,11,6,9,5,5]]
    # 17
    test = Solution()
    print(test.minCostII(costs))

if __name__ == "__main__":
    main()