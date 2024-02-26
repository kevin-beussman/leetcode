from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root != None:
            queue = [(0,root)]
        else:
            queue = []
        
        levels = []
        while queue:
            depth,curnode = queue.pop(0)
            if depth >= len(levels):
                levels.append([])
            if curnode != None:
                levels[depth].append(curnode.val)
            else:
                levels[depth].append(-101)
                continue
            queue.append((depth+1,curnode.left))
            queue.append((depth+1,curnode.right))
        
        for level in levels[1:]:
            if level != level[::-1]:
                return False
        return True

test = Solution()
# print(test.isSymmetric(TreeNode(1,left=TreeNode(0))))
# print(test.isSymmetric(TreeNode(1,left=TreeNode(2,left=TreeNode(3),right=TreeNode(4)),right=TreeNode(2,left=TreeNode(4),right=TreeNode(3)))))
# print(test.isSymmetric(TreeNode(1,left=TreeNode(2,right=TreeNode(4)),right=TreeNode(2,right=TreeNode(3)))))
print(test.isSymmetric(TreeNode(0,left=TreeNode(-3,left=TreeNode(-93,left=TreeNode(-77)),right=TreeNode(97,left=TreeNode(-96))),right=TreeNode(-3,left=TreeNode(97,left=TreeNode(-96)),right=TreeNode(-93,right=TreeNode(-77))))))