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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # out = TreeNode(postorder.pop())
        
        # create hashmap of indexes for each node value in inorder and postorder
        hmap = {}
        for ind,val in enumerate(inorder):
            hmap[val] = ind
        
        def helper(indL,indR):
            if indL > indR:
                return None
            else:
                curval = postorder.pop()
                indroot = hmap[curval]
                
                roottree = TreeNode(curval)
                roottree.right = helper(indroot+1,indR)
                roottree.left = helper(indL,indroot-1)
                return roottree
            
        return helper(0,len(postorder)-1)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
# inorder = [2,1]
# postorder = [2,1]
test = Solution()
test2 = test.buildTree(inorder,postorder)