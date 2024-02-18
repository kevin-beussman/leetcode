from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # top-down
        # @lru_cache(None)
        # def dp(i,j):
        #     if i == 0 or j == 0:
        #         return 1
        #     return dp(i-1,j) + dp(i,j-1)

        # return dp(m-1,n-1)

        # bottom-up
        dp = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

def main():
    m = 3
    n = 7
    test = Solution()
    print(test.uniquePaths(m,n))

if __name__ == "__main__":
    main()
