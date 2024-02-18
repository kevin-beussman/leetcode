# count vowels permutation
# from typing import List
from functools import lru_cache

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # # top-down DP (doesn't work, TLE or maximum recursion depth)
        # letters = ["a","e","i","o","u"]
        # poss = {"":letters,"a":["e","i","u"],"e":["a","i"],"i":["e","o"],"o":["i"],"u":["i","o"]}

        # @lru_cache(None)
        # def dp(i, l):
        #     if i == 0:
        #         return 1
            
        #     return sum(dp(i-1, c) for c in poss[l]) % (10**9 + 7)
        
        # return dp(n, "")

        # bottom-up
        # letters = ["a","e","i","o","u"] # is [0,1,2,3,4]
        # poss = {"a":["e","i","u"],"e":["a","i"],"i":["e","o"],"o":["i"],"u":["i","o"]}
        poss = {0:[1,2,4],1:[0,2],2:[1,3],3:[2],4:[2,3]}

        dp = [[0]*5 for _ in range(2)]
        dp[0] = [1]*5

        for i in range(1,n):
            for j in range(5):
                dp[1][j] = sum(dp[0][k] for k in poss[j]) % (10**9 + 7)
            dp[0] = dp[1][:]
        
        return sum(dp[0]) % (10**9 + 7)

def main():
    n = 13801
    test = Solution()
    print(test.countVowelPermutation(n))

if __name__ == "__main__":
    main()
    
