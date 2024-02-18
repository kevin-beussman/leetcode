from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = [[]]
        if root:
            queue = [(0,root)]
        else:
            queue = []
        while queue:
            j,curnode = queue.pop(0)
            if len(out) <= j:
                out.append([])
            out[j].append(curnode.val)
            # queue.append(TreeNode(curnode.val))
            if curnode.left:
                queue.append((j+1,curnode.left))
            if curnode.right:
                queue.append((j+1,curnode.right))
        
        return out

test = Solution()
# print(test.levelOrder(TreeNode(1,right=TreeNode(2,left=TreeNode(3)))))
# print(test.levelOrder(TreeNode(4,left=TreeNode(2,left=TreeNode(1),right=TreeNode(3)),right=TreeNode(6,left=TreeNode(5),right=TreeNode(7)))))
print(test.levelOrder(None))