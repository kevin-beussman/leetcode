from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for j in range(len(nums)):
            if nums[j] == val:
                nums[j] = nums[counter]
                nums[counter] = val
                counter += 1
        nums.reverse()
        return len(nums)-counter
    
test = Solution()
# print(test.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
print(test.removeElement(nums = [3,2,2,3], val = 3))