from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        n = len(nums) - k
        while True:
            pivot = nums.pop(0)
            nex = [j for j in nums if j < pivot]
            cL = len(nex)
            if cL == n:
                return pivot
            elif cL < n:
                nex = [j for j in nums if j >= pivot]
                n = n - cL - 1
            # n -= 1
            nums = nex[:]
                


test = Solution()
print(test.findKthLargest([3,2,3,1,2,4,5,5,6],9))
# print(test.findKthLargest([2,1],2))