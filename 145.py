from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def trav(r):
            if r.left:
                trav(r.left)
            if r.right:
                trav(r.right)
            out.append(r.val)
            return
        if root:
            trav(root)
        return out

test = Solution()
print(test.postorderTraversal(TreeNode(3,left=TreeNode(1),right=TreeNode(2))))