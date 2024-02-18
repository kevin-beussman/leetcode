# Same Tree
from typing import Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack = [(p,q)]
        while stack:
            a,b = stack.pop()
            if (a and not b) or (b and not a):
                return False
            elif a and b:
                if a.val != b.val:
                    return False
                stack.append((a.left,b.left))
                stack.append((a.right,b.right))
        return True

def main():
    p = TreeNode()
    q = TreeNode()
    test = Solution()
    print(test.isSameTree(p,q))

if __name__ == "__main__":
    main()