from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        global ans
        
        def helper(r):
            global ans
            if not r:
                return [False,False]
            out = [False,False]
            if r.val == p.val:
                out[0] = True
                print('Found P at ' + str(r.val))
            elif r.val == q.val:
                out[1] = True
                print('Found Q at ' + str(r.val))
            outl = helper(r.left)
            outr = helper(r.right)
            pq = [out[j] or outl[j] or outr[j] for j in range(2)]
            if all(pq):
                if not ans:
                    ans = r
            return pq
        
        ans = []
        helper(root)
        return ans

tree = TreeNode(4,left=TreeNode(2,left=TreeNode(1),right=TreeNode(3)),right=TreeNode(6,left=TreeNode(5),right=TreeNode(7)))
p = TreeNode(2)
q = TreeNode(6)
test = Solution()
print(test.lowestCommonAncestor(tree, p, q))
