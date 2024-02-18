from typing import List
from functools import lru_cache

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = nums[0]
        largsum = nums[0]
        for j in range(1,len(nums)):
            cursum = max(nums[j],cursum+nums[j])
            largsum = max(largsum,cursum)
        return largsum

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4] # 6
    # nums = [1,9,-3,-2,1,-1,-1,5,5]
    # nums = [1,-1,1,-1,10,-1,5,-2,1,-2,10]
    test = Solution()
    print(test.maxSubArray(nums))

if __name__ == "__main__":
    main()














