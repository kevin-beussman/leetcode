class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def numTrees(self, n: int) -> int:

        def helper(l,r):
            if l > r:
                return 1
            out = 0
            for j in range(l,r+1):
                if (l,j-1) not in memo:
                    memo[(l,j-1)] = helper(l,j-1)
                if (j+1,r) not in memo:
                    memo[(j+1,r)] = helper(j+1,r)
                out += memo[(l,j-1)]*memo[(j+1,r)]
            return out

        memo = {}
        return helper(1,n)

n = 19
test = Solution()
print(test.numTrees(n))