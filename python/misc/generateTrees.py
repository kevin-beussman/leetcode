from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def helper(l,r):
            if l > r:
                return [None]
            out = []
            for j in range(l,r+1):
                lefttrees = helper(l,j-1)
                righttrees = helper(j+1,r)
                for lt in lefttrees:
                    for rt in righttrees:
                        temp = TreeNode(j)
                        temp.left = lt
                        temp.right = rt
                        out.append(temp)
            return out
   
        return helper(1,n)

n = 2
test = Solution()
temp = test.generateTrees(n)
