
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        out = Node(node.val)
        outnodelist = [out]
        outnodevals = [1]
        outnodevisit = [False]
        maxnode = 1
        stack = [(node,out)]
        while stack:
            curnode,curout = stack.pop()
            if outnodevisit[curout.val-1]:
                continue
            outnodevisit[curout.val-1] = True
            for j,neighbor in enumerate(curnode.neighbors):
                while neighbor.val not in outnodevals:
                    maxnode += 1
                    outnodelist.append(Node(maxnode))
                    outnodevals.append(maxnode)
                    outnodevisit.append(False)
                curout.neighbors.append(outnodelist[neighbor.val-1])
                if not outnodevisit[neighbor.val-1]:
                    stack.append((neighbor,curout.neighbors[j]))
        return out



adjList = [[2,4],[1,3],[2,4],[1,3]]