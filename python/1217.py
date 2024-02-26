from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        out1 = 0
        out2 = 0
        # stackpos = max(set(position),key=position.count)
        for j in position:
            out1 += j % 2
            out2 += (j+1) % 2
        return min(out1,out2)
        
pos = [2,2,2,3,3]
# pos = [3,3,1,2,2]
test = Solution()
print(test.minCostToMoveChips(pos))