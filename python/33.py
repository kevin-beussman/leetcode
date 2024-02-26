from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l != r-1:
            m = (l+r)//2
            if (target > nums[l]) and (target < nums[m]):
                r = m
            elif (target > nums[m]) and (target > nums[l]):
                l = m
            else:
                if (nums[l] > nums[m]) and (target <= nums[m]):
                    r = m
                elif (nums[r] < nums[m]) and (target <= nums[m]):
                    l = m
        return l

test = Solution()
print(test.search([4,5,6,7,0,1,2],3))
