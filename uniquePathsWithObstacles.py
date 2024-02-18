from typing import List
from functools import lru_cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # # top-down
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])

        # @lru_cache(None)
        # def dp(i,j):
        #     if i == 0 and j == 0:
        #         return 1
        #     if i < 0 or j < 0:
        #         return 0
            
        #     if obstacleGrid[i][j] == 1:
        #         return 0
        #     else:
        #         return dp(i-1,j) + dp(i,j-1)
        
        # return dp(m-1,n-1)

        # bottom-up
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]
        
        for i in range(1,m):
            for j in range(0,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[m-1][n-1]

def main():
    obstacleGrid = [[0,1,0],[0,0,0],[0,1,0]]
    test = Solution()
    print(test.uniquePathsWithObstacles(obstacleGrid))

if __name__ == "__main__":
    main()
