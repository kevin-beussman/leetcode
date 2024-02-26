# Validate Binary Search Tree
from typing import Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # D&C
        def helper(tree,lower,upper):
            check_left = True
            check_right = True
            if tree.left:
                check_left = (tree.left.val < tree.val) and (tree.left.val > lower) and helper(tree.left,lower,tree.val)
            if tree.right:
                check_right = (tree.right.val > tree.val) and (tree.right.val < upper) and helper(tree.right,tree.val,upper)

            if check_left and check_right:
                return True
            else:
                return False
        return helper(root,float("-inf"),float("inf"))

def main():
    # root = TreeNode(2,TreeNode(1),TreeNode(3))
    root = TreeNode(2,TreeNode(1),TreeNode(8,TreeNode(5),TreeNode(20,TreeNode(3),TreeNode(21))))
    test = Solution()
    print(test.isValidBST(root))

if __name__ == "__main__":
    main()