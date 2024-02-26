#2039. The Time When the Network Becomes Idle
from typing import List
from functools import lru_cache
from collections import defaultdict
import heapq

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # first, find shortest distances between server and nodes
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1]) # undirected graph
            adj[edge[1]].append(edge[0])
        
        # djikstra's (heap)
        # pq = [(0,0)]
        # dist = {}
        # while pq:
        #     curdist,curnode = heapq.heappop(pq)
        #     if curnode in dist:
        #         continue
        #     dist[curnode] = curdist
        #     for nextnode in adj[curnode]:
        #         if nextnode not in dist:
        #             heapq.heappush(pq,(curdist + 1, nextnode))
        
        # bfs (queue)
        queue = [(0,0)]
        dist = {}
        while queue:
            curdist,curnode = queue.pop(0)
            if curnode in dist:
                continue
            dist[curnode] = curdist
            for nextnode in adj[curnode]:
                if nextnode not in dist:
                    queue.append((curdist + 1,nextnode))
        
        # now we have min distance between each data server and each master server stored in dist
        # worked out these by hand
        # if dist = 2, patience = 3: time = 7
        # if dist = 2, patience = 1: time = 7
        # if dist = 2, patience = 2: time = 6
        # if dist = 3, patience = 1: time = 11
        # if dist = 3, patience = 3: time = 9
        # if dist = 6, patience = 5: time = 22
        # equation is then time = dist*2 + (dist*2-1)//patience*patience
        
        n = len(dist)
        maxtime = 0
        for d in range(1,n):
            time = dist[d]*2 + (dist[d]*2-1)//patience[d]*patience[d]
            # print(f"Data server {d} takes time {time}")
            maxtime = max(maxtime, time)
        
        return maxtime + 1 # want the second when idle STARTS. Above formula gives traversal time.
                
def main():
    # edges = [[0,1],[0,2],[1,2]] # 3
    # patience = [0,10,10]
    edges = [[0,1],[1,2]] # 7
    patience = [0,2,1]
    test = Solution()
    print(test.networkBecomesIdle(edges,patience))

if __name__ == "__main__":
    main()
    
