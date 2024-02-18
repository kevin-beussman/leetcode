# 1834. Single-Threaded CPU
from typing import List
#from functools import lru_cache
#from collections import defaultdict
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        enqueue = []
        for i,task in enumerate(tasks):
            heapq.heappush(enqueue,(task[0],task[1],i))

        out = []
        time = 0
        avail = []
        while enqueue or avail:
            if avail:
                pT, i = heapq.heappop(avail)
                time += pT
                out.append(i)
            elif enqueue:
                eT, pT, i = heapq.heappop(enqueue)
                time = max(time,eT) # in case of idle time
                heapq.heappush(avail,(pT,i))

            while enqueue and enqueue[0][0] <= time:
                eT, pT, i = heapq.heappop(enqueue)
                heapq.heappush(avail,(pT,i))
        
        return out

def main():
    # tasks = [[1,2],[2,4],[3,2],[4,1]]
    # tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    tasks = [[1,4],[4,3],[5,2],[6,2]]
    test = Solution()
    print(test.getOrder(tasks))

if __name__ == "__main__":
    main()