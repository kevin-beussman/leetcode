

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        out = ""
        if root:
            queue = [root]
        else:
            queue = []
        while queue:
            curnode = queue.pop(0)
            if not curnode:
                out += ',N'
                continue
            if out:
                out += ',' + str(curnode.val)
            else:
                out = str(curnode.val)
            # if curnode.left or curnode.right:
            queue.append(curnode.left)
            queue.append(curnode.right)
        
        return out

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        nodes = data.split(',')
        curval = nodes.pop(0)
        root = TreeNode(int(curval))
        queue = [root]
        while queue:
            curnode = queue.pop(0)
            if nodes:
                if nodes[0] == 'N':
                    curnode.left = None
                    nodes.pop(0)
                else:
                    curnode.left = TreeNode(int(nodes.pop(0)))
                    queue.append(curnode.left)
            if nodes:
                if nodes[0] == 'N':
                    curnode.right = None
                    nodes.pop(0)
                else:
                    curnode.right = TreeNode(int(nodes.pop(0)))
                    queue.append(curnode.right)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# tree = TreeNode(4,left=TreeNode(2,left=TreeNode(1),right=TreeNode(3)),right=TreeNode(6,left=TreeNode(5),right=TreeNode(7)))
# tree = TreeNode(4,left=TreeNode(2,left=TreeNode(1)),right=TreeNode(6,left=TreeNode(5),right=TreeNode(7)))
tree = TreeNode(1,left=TreeNode(2),right=TreeNode(3,left=TreeNode(4),right=TreeNode(5)))
ser = Codec()
deser = Codec()
print(ser.serialize(tree))
out = deser.deserialize(ser.serialize(tree))
print(ser.serialize(deser.deserialize(ser.serialize(tree))))