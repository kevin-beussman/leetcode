from typing import List
from functools import lru_cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # top-down
        # m = len(grid)
        # n = len(grid[0])

        # def dp(i,j):
        #     if i < 0 or j < 0:
        #         return float('inf')

        #     if i == 0 and j == 0:
        #         return grid[i][j]
            
        #     return min(dp(i-1,j) + grid[i][j], dp(i,j-1) + grid[i][j])
        
        # return dp(m-1,n-1)

        # bottom-up
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        
        return dp[m-1][n-1]

def main():
    grid = [[1,3,1],[1,5,1],[4,2,1]] # 7
    test = Solution()
    print(test.minPathSum(grid))

if __name__ == "__main__":
    main()
