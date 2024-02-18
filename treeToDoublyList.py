# 426. Convert Binary Search Tree to Sorted Doubly Linked List
from typing import Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        stack = [root]
        minnode = Node(float('inf'))
        checkstart = True
        while stack:
            curnode = stack.pop()
            if curnode.val < minnode.val:
                minnode = curnode
            leftnode = curnode.left
            rightnode = curnode.right

            if not leftnode and not rightnode:
                if not checkstart:
                    curnode.left = prev
                else:
                    checkstart = False
                    firstnode = curnode
                prev = curnode
                continue

            if rightnode:
                stack.append(rightnode)
            curnode.left = None
            curnode.right = None
            stack.append(curnode)
            if leftnode:
                stack.append(leftnode)
        
        lastnode = curnode
        curnode.right = firstnode
        prev = curnode
        while curnode.left:
            curnode = curnode.left
            curnode.right = prev
            prev = curnode

        firstnode.left = lastnode

        return minnode

def main():
    # root = Node(4,Node(2,Node(1),Node(3)),Node(5))
    root = Node(-1,right=Node(1,right=Node(9)))
    test = Solution()
    print(test.treeToDoublyList(root))

if __name__ == "__main__":
    main()