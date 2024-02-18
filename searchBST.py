from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(tn,val):
            
            if not tn:
                return None

            if tn.val == val:
                return tn
            elif tn.val > val:
                return dfs(tn.left,val)
            elif tn.val < val:
                return dfs(tn.right,val)
        
        return dfs(root,val)

root = TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7))
val = 2
test = Solution()
temp = test.searchBST(root,val)
print([temp.val,temp.left.val,temp.right.val])
# print([temp.val])