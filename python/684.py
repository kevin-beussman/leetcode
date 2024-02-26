from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def isTree(edgelist):
            adj = {}
            for edge in edgelist:
                if edge[0] in adj:
                    adj[edge[0]].append(edge[1])
                else:
                    adj[edge[0]] = [edge[1]]
                if edge[1] in adj:
                    adj[edge[1]].append(edge[0])
                else:
                    adj[edge[1]] = [edge[0]]
            
            # Traverse the graph. If we ever run into a visited node, return False. If the node
            # has no edges, return False.
            visited = [False]*n
            queue = [1]
            while queue:
                cur = queue.pop(0)
                if visited[cur-1] or (cur not in adj):
                    return False
                visited[cur-1] = True
                nextnodes = adj.pop(cur)
                for node in nextnodes:
                    adj[node].remove(cur)
                    queue.append(node)
            if all(visited):
                return True
            else:
                return False

        n =  len(edges)
        edges.reverse()
        for j,edge in enumerate(edges):
            if edge == [4,19]:
                print('hi')
            if isTree(edges[:j] + edges[j+1:]):
                return edge


# edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# edges = [[1,2],[1,3],[2,3]]
# edges = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
edges = [[20,24],[3,17],[17,20],[8,15],[14,17],[6,17],[15,23],[6,8],[15,19],[16,22],[7,9],[8,22],[2,4],[4,11],[22,25],[6,24],[13,19],[15,18],[1,9],[4,9],[4,19],[5,10],[4,21],[4,12],[5,6]]
test = Solution()
print(test.findRedundantConnection(edges))