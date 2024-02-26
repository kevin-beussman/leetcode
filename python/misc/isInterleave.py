# Interleaving String
#from typing import List, Optional
from functools import lru_cache
#import heapq

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # top-down DP
        # n1 = len(s1)
        # n2 = len(s2)
        # n3 = len(s3)
        # if n3 != (n1 + n2):
        #     return False
        
        # @lru_cache(None)
        # def dp(i1,i2): # i1, i2 indicate which index in s1, s2 we are considering
        #     if (i1 == n1) and (i2 == n2):
        #         return True # we made it to the end!
        #     elif (i1 == n1) and (i2 < n2):
        #         # continue with s2 to the end
        #         if s2[i2:] == s3[(i1+i2):]:
        #             return True
        #         else:
        #             return False
        #     elif (i1 < n1) and (i2 == n2):
        #         # continue with s1 to the end
        #         if s1[i1:] == s3[(i1+i2):]:
        #             return True
        #         else:
        #             return False
            
        #     if s1[i1] == s2[i2] == s3[i1+i2]:
        #         return dp(i1+1,i2) or dp(i1,i2+1)
        #     elif s1[i1] == s3[i1+i2]:
        #         return dp(i1+1,i2)
        #     elif s2[i2] == s3[i1+i2]:
        #         return dp(i1,i2+1)
        #     else:
        #         return False

        # return dp(0,0)

        # bottom-up DP
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n3 != (n1 + n2):
            return False
        if n1 == 0:
            return s2 == s3
        if n2 == 0:
            return s1 == s3

        # dp = [[False]*n2 + [True] for _ in range(n1+1)]
        # dp[-1] = [True]*(n2+1)
        dp = [[False]*(n2+1) for _ in range(n1+1)]
        dp[n1][n2] = True # probably not necessary
        for i1 in range(n1):
            dp[i1][n2] = s1[i1:] == s3[n2+i1:]
        for i2 in range(n2):
            dp[n1][i2] = s2[i2:] == s3[n1+i2:]


        for i1 in range(n1-1,-1,-1):
            for i2 in range(n2-1,-1,-1):
                # print(f"({i1},{i2}) = {i1+i2}")
                if s1[i1] == s2[i2] == s3[i1+i2]:
                    dp[i1][i2] = dp[i1+1][i2] or dp[i1][i2+1]
                elif s1[i1] == s3[i1+i2]:
                    dp[i1][i2] = dp[i1+1][i2]
                elif s2[i2] == s3[i1+i2]:
                    dp[i1][i2] = dp[i1][i2+1]
        
        print(dp)
        return dp[0][0]

def main():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac" # true
    # s3 = "aadbbbaccc" # false
    # s3 = s1+s2

    # s1 = "a"
    # s2 = ""
    # s3 = "c"

    # s1 = "aabd"
    # s2 = "abdc"
    # s3 = "aabdbadc"
    test = Solution()
    print(test.isInterleave(s1,s2,s3))

if __name__ == "__main__":
    main()