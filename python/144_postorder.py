from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if root:
            stack = [root]
        else:
            stack = []
        curnode = root
        while stack:
            curnode = stack.pop()
            stack.append(TreeNode(curnode.val))
            if curnode.right:
                stack.append(curnode.right)
            if curnode.left:
                stack.append(curnode.left)
            if not curnode.left and not curnode.right:
                out.append(curnode.val)
                stack.pop()
        
        return out

test = Solution()
print(test.postorderTraversal(TreeNode(1,right=TreeNode(2,left=TreeNode(3)))))
# print(test.postorderTraversal(TreeNode(4,left=TreeNode(2,left=TreeNode(1),right=TreeNode(3)),right=TreeNode(6,left=TreeNode(5),right=TreeNode(7)))))
# print(test.postorderTraversal(None))