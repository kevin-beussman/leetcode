from typing import List
from functools import lru_cache

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # top-down
        # m = len(matrix)
        # n = len(matrix[0])

        # @lru_cache(None)
        # def dp(i,j):
        #     if j < 0 or j >= n:
        #         return float('inf')
        #     if i == 0:
        #         return matrix[i][j]

        #     return min(dp(i-1,j-1),dp(i-1,j),dp(i-1,j+1)) + matrix[i][j]
        
        # return min(dp(m-1,j) for j in range(n))

        # bottom-up
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*n for _ in range(m)]
        dp[0] = matrix[0][:]
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j+1]) + matrix[i][j]
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) + matrix[i][j]
        
        return min(dp[m-1])

def main():
    matrix = [[2,1,3],[6,5,4],[7,8,9]] # 13
    test = Solution()
    print(test.minFallingPathSum(matrix))

if __name__ == "__main__":
    main()
