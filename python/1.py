from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		#nums.sort()
		if nums.count(target/2) == 2:
			i1 = nums.index(target/2)
			nums.remove(target/2)
			i2 = nums.index(target/2) + 1
		else:
			for j in nums:
				if nums.count(target - j) > 0:
					if j != target/2:
						i1 = nums.index(j)
						i2 = nums.index(target - j)
		return [i1,i2]


test = Solution()
print(test.twoSum([3,2,4],6))