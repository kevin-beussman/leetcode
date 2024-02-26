from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        prev = nums[j]
        while (j > 0) and (nums[j-1] > prev):
            j2 = j-1
            prev = nums[j2]
            while (j2 < len(nums) - 1) and (nums[j2] > nums[j2+1]):
                nums[j2],nums[j2+1] = nums[j2+1],nums[j2]
                j2 += 1
            j -= 1
        
        if j == 0:
            nums.sort()
        else:
            piv = j-1
            while (j < len(nums) - 1) and (nums[j] <= nums[piv]):
                j += 1
            nums[piv],nums[j] = nums[j],nums[piv]
        return nums

test = Solution()
print(test.nextPermutation([9,5,4,3,1]))