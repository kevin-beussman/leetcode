from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # out = []
        # def trav(r):
        #     out.append(r.val)
        #     if r.left:
        #         trav(r.left)
        #     if r.right:
        #         trav(r.right)
        #     return
        # if root:
        #     trav(root)
        # return out
        out = []
        if root:
            stack = [root]
        else:
            stack = []
        curnode = root
        while stack:
            curnode = stack.pop()
            out.append(curnode.val)
            if curnode.right:
                stack.append(curnode.right)
            if curnode.left:
                stack.append(curnode.left)
        
        return out

test = Solution()
# print(test.preorderTraversal(TreeNode(3,left=None,right=TreeNode(2))))
print(test.preorderTraversal(None))