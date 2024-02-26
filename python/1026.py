from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        out = 0
        stack = [(root, root.val, root.val)]
        while stack:
            cur, maxv, minv = stack.pop()
            if cur.val == None:
                continue
            out = max([out, abs(cur.val - maxv), abs(cur.val - minv)])
            maxv = max([maxv, cur.val])
            minv = min([minv, cur.val])
            if cur.left:
                stack.append((cur.left, maxv, minv))
            if cur.right:
                stack.append((cur.right, maxv, minv))
        return out

# root = TreeNode(8,left=TreeNode(3,left=TreeNode(1),right=TreeNode(6,left=TreeNode(4),right=TreeNode(7))),right=TreeNode(10,right=TreeNode(14,left=TreeNode(13))))
root = TreeNode(1,right=TreeNode(2,right=TreeNode(0,left=TreeNode(3))))
test = Solution()
print(test.maxAncestorDiff(root))