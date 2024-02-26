from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # two indexes to denote current location
        # one index denotes current max square size
        # dp returns square size
        if not matrix:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0]*n for j in range(m)]
        maxsize = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                        maxsize = max(dp[i][j],maxsize)
                        continue
                    
                    cleftup = dp[i-1][j-1]
                    cleft = dp[i-1][j]
                    cup = dp[i][j-1]
                    dp[i][j] = min([cleftup,cleft,cup]) + 1
                    maxsize = max(dp[i][j],maxsize)

        return maxsize**2

def main():
    # matrix = [["0","1"],["1","0"]]
    # matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # matrix = [["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"]]
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    test = Solution()
    print(test.maximalSquare(matrix))

if __name__ == "__main__":
    main()