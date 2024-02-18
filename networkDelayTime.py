# Maximum Length of Repeated Subarray
from typing import List
from functools import lru_cache
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstra's
        adj = {}
        dist = {}
        for edge in times:
            if edge[0] not in adj:
                adj[edge[0]] = []
            adj[edge[0]].append(edge[1])
            dist[(edge[0],edge[1])] = edge[2]
        
        visited = [False]*n
        pq = [(0,k)]
        maxtime = 0
        while pq:
            curtime, curnode = heapq.heappop(pq)
            if visited[curnode-1]:
                continue
            visited[curnode-1] = True
            maxtime = max(maxtime, curtime)
            if curnode in adj:
                for nextnode in adj[curnode]:
                    if not visited[nextnode-1]:
                        heapq.heappush(pq,(curtime + dist[curnode,nextnode], nextnode))
        
        if not all(visited):
            return -1
        return maxtime
                
def main():
    times = [[2,1,1],[2,3,1],[3,4,1]] # 2
    n = 4
    k = 2
    # times = [[1,2,1],[2,3,2],[1,3,2]] # 2
    # n = 3
    # k = 1
    # times = [[1,2,1],[2,3,2],[1,3,4]] # 3
    # n = 3
    # k = 1

    test = Solution()
    print(test.networkDelayTime(times,n,k))

if __name__ == "__main__":
    main()
    
