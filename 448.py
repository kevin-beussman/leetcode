from typing import List

class Solution:
	def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
		nums.sort()
		ans = []
		if nums[0] != 1:
			ans.extend(range(1,nums[0]))
		for j in range(len(nums)-1):
			if nums[j+1]-nums[j] > 1:
				ans.extend(range(nums[j]+1,nums[j+1]))
		if nums[-1] != len(nums):
			ans.extend(range(nums[-1]+1,len(nums)+1))
		return ans
# 		return [val for val in range(1,n+1) if val not in nums]

test = Solution()
print(test.findDisappearedNumbers([1,1,3,3,3,4,4,4,4]))