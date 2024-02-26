from typing import List
from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # state variable is i and l, number of items taken and number of items taken from left of nums
        n = len(nums)
        m = len(multipliers)

        # @lru_cache(maxsize=None)
        # def dp(i,l):
        #     takeleft = multipliers[i]*nums[l]
        #     takeright = multipliers[i]*nums[(n-1)-(i-l)]

        #     if i == m-1:
        #         return max(takeleft,takeright)
        #     else:
        #         return max(dp(i+1,l+1) + takeleft, dp(i+1,l) + takeright)
        
        # return dp(0,0)

        dp = [[0]*(m+1) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            temp = float("-inf")
            for l in range(i+1):
                takeleft = multipliers[i]*nums[l]
                takeright = multipliers[i]*nums[(n-1)-(i-l)]
                
                dp[i][l] = max(dp[i+1][l+1] + takeleft,dp[i+1][l] + takeright)
        
        return dp[0][0]

        # this keeps dp size m, and updates dp for each i
        # dp = [0]*(m+1)

        # for i in range(m-1,-1,-1):
        #     temp = float("-inf")
        #     for l in range(i+1):
        #         takeleft = multipliers[i]*nums[l]
        #         takeright = multipliers[i]*nums[(n-1)-(i-l)]
                
        #         dp[l] = max(dp[l+1] + takeleft,dp[l] + takeright)
        
        # return dp[0]
        
def main():
    nums = [-5,-3,-3,-2,7,1]
    multipliers = [-10,-5,3,4,6]
    # nums = [1,2,3]
    # multipliers = [3,2,1]
    test = Solution()
    print(test.maximumScore(nums,multipliers))

if __name__ == "__main__":
    main()