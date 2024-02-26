from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2:
            return False
        
        if max(nums) > tot/2:
            return False
        
        memo = {}
        def dfs(nums,target,n):
            if target == 0:
                return True
            elif n == 0 or target < 0:
                return False
            if (target,n-1) not in memo:
                memo[(target,n-1)] = dfs(nums,target,n-1)
            if (target-nums[n-1],n-1) not in memo:
                memo[(target-nums[n-1],n-1)] = dfs(nums,target-nums[n-1],n-1)
            t1 = memo[(target,n-1)]
            t2 = memo[(target-nums[n-1],n-1)]
            return t1 or t2
        
        return dfs(nums,tot/2,len(nums)-1)


        # nums.sort()
        # rem = []
        # diff = tot/2 - nums.pop()
        # if not diff:
        #     return True
        
        # while nums and nums[0] <= diff:
        #     rem.append(nums.pop(0))
        
        # if not rem:
        #     return False
        
        # if rem[-1] == diff:
        #     return True
               
        # stack = [(diff,rem)]
        # while stack:
        #     cdiff,crem = stack.pop()
        #     for j,v in enumerate(crem):
        #         if v == cdiff:
        #             return True
        #         elif v < cdiff:
        #             stack.append((cdiff-v, crem[0:j] + crem[j+1:]))
        # return False

nums = [38,7,20,83,13,44,87,70,45,54,23,72,81,62,33,55,16,96,9,64,15,88,45,97,43,55,56,43,13,29,79,27,26,50,25,5,24,61,48,32,52,62,25,77,18,4,59,73,70,92,2,36,94,4,24,71,42,11,41,94,20,82,14,71,45,80,35,61,31,61,46,47,40,80,52,90,52,6,75,28,67,68,8,77,19,2,85,69,35,14,58,67,45,66,87,6,24,88,11,24]
test = Solution()
print(test.canPartition(nums))