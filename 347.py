from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = {}
        for j in nums:
            if j in n:
                n[j] += 1
            else:
                n[j] = 1
        
        out = []
        for ik in range(k):
            out.append(max(n, key=n.get))
            n.pop(out[-1])
        
        return out
        
        
nums = [1,1,1,1,1,2,2,2,2,3,3,3]
k = 2
test = Solution()
print(test.topKFrequent(nums,k))

test2 = test.topKFrequent(nums,k)