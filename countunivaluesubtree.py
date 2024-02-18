from typing import Optional

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
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # stack = [(True,root.val,root)]
        
        # while stack:
        #     same,val,cur = stack.pop()
            
            
            
        global count
        
        if root == None:
            return 0
        
        def trav(r):
            global count
            if r.right and r.left:
                rlval = trav(r.left)
                rrval = trav(r.right)
                if r.val == rlval and r.val == rrval:
                    count += 1
                    return r.val
                else:
                    return -1001
            elif r.left:
                if r.val == trav(r.left):
                    count += 1
                    return r.val
                else:
                    return -1001
            elif r.right:
                if r.val == trav(r.right):
                    count += 1
                    return r.val
                else:
                    return -1001
            else:
                count += 1
                return r.val
            
        count = 0
        trav(root)
        return count

tree = TreeNode(5,left=TreeNode(0,left=TreeNode(5),right=TreeNode(5)),right=TreeNode(5,right=TreeNode(5,right=TreeNode(5))))
test = Solution()
print(test.countUnivalSubtrees(tree))