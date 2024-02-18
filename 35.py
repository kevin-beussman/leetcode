from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for j in range(len(nums)):
            if nums[j] >= target:
                return j
        return j+1
    
test = Solution()
print(test.searchInsert(nums = [1,3,5,6], target = 2))