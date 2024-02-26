from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if root:
            stack = [root]
        else:
            stack = []
        curnode = root
        while stack:
            curnode = stack.pop()
            if curnode.right:
                stack.append(curnode.right)
            stack.append(TreeNode(curnode.val))
            if curnode.left:
                stack.append(curnode.left)
            if not curnode.left and not curnode.right:
                out.append(curnode.val)
                stack.pop()
        
        return out

test = Solution()
# print(test.inorderTraversal(TreeNode(1,right=TreeNode(2,left=TreeNode(3)))))
print(test.inorderTraversal(TreeNode(4,left=TreeNode(2,left=TreeNode(1),right=TreeNode(3)),right=TreeNode(6,left=TreeNode(5),right=TreeNode(7)))))
# print(test.inorderTraversal(None))