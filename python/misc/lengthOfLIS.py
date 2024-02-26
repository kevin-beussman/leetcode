from typing import List
from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # state variables:
        # index i for how far along in nums we are
        # h which is the highest value in the current substring
        # dp returns the length of the longest substring in nums[i:] starting above h
        
        # dp returns the longest substring up to and including node i
        # @lru_cache(maxsize=None)
        # def dp(i):
        #     nonlocal maxval
        #     if i == 0:
        #         return 1
            
        #     temp = float('-inf')
        #     for j in range(0,i):
        #         temp2 = dp(j)
        #         if nums[i] <= nums[j]:
        #             temp2 = 0
        #         temp = max(temp,temp2 + 1)
        #     maxval = max(maxval,temp)
        #     print(temp)
        #     return temp
        # maxval = float('-inf')
        # dp(n-1)
        # return maxval

        dp = [1]*n
        for i in range(1,n):
            prev = -1
            for j in range(i-1,-1,-1):
                if (nums[i] > nums[j]) and (dp[j]+1 > dp[i]):
                    dp[i] = dp[j]+1

        return max(dp)

        # # this doesn't work in time:
        

        # @lru_cache(maxsize=None)
        # def dp(i,h):
        #     if i == n:
        #         return 0
            
        #     temp = float('-inf')
        #     take = float('-inf')
        #     if nums[i] > h: # can only take if num is bigger than previous largest
        #         take = dp(i+1,nums[i]) + 1
        #     nottake = dp(i+1,h)
        #     temp = max(temp,nottake,take)
        #     return temp
        
        # return dp(0,float('-inf'))

# nums = [10,9,2,5,3,7,101,18] # 4
# nums = [7,7,7,7,7,7,7] # 1
# nums = [0,1,0,3,2,3] # 4
# nums = [4,10,4,3,8,9] # 3
nums = [1,3,6,7,9,4,10,5,6] # 6
# nums = [10,9,2,5,3,4] # 3
test = Solution()
print(test.lengthOfLIS(nums))