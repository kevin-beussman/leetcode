from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def helper(j,cursum):
            nonlocal out, n, memo, target
            if (j,cursum) in memo:
                return memo[(j,cursum)]
                
            if (j == n):
                if (cursum == target):
                    memo[(j,cursum)] = 1
                    return memo[(j,cursum)]
                else:
                    return 0
            
            memo[(j,cursum)] = helper(j+1,cursum + nums[j]) + helper(j+1,cursum - nums[j])
            return memo[(j,cursum)]
        
        out = 0
        n = len(nums)
        memo = {}
        return helper(0,0)


# nums = [1,1,1,1,1]
# target = 3
# nums = [1]
# target = 1
# nums = [33,36,38,40,25,49,1,8,50,13,41,50,29,27,18,25,37,8,0,48]
# target = 0
nums = [0,0,0,0,0,0,0,0,1] # 256
target = 1
test = Solution()
print(test.findTargetSumWays(nums,target))