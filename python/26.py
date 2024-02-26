from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        for j in nums:
            if j != nums[counter]:
                counter += 1
                nums[counter] = j
        return counter+1
        
test = Solution()
print(test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))