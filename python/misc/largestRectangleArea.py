# Largest Rectangle in Histogram
from typing import List
#from functools import lru_cache
#from collections import defaultdict
# import heapq

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # split at min
        # maxrect = maxrec

        # minheights = [(h,i) for i,h in enumerate(heights)]
        # heapq.heapify(minheights)

        # maxrect = 0
        # queue = [heights[:]]
        # while queue:
        #     curheights,start = queue.pop(0)
        #     n = len(curheights)
        #     # print(minheights)
        #     minh = 0
        #     minidx = 0
        #     for i in range(n): # find min in this range
        #         if curheights[i] < curheights[minidx]:
        #             minidx = i

        #     # if (minheights[0][1] >= start+n) or (minheights[0][1] < start):
        #     #     queue.append((curheights,start))
        #     # else:
        #         minh,minidx = heapq.heappop(minheights)
        #         maxrect = max(maxrect,n*minh)
        #         left = curheights[:minidx-start]
        #         right = curheights[minidx-start+1:]
        #         if left:
        #             queue.append((left,start))
        #         if right:
        #             queue.append((right,minidx+1))

        # minheights = [(h,i) for i,h in enumerate(heights)]
        # heapq.heapify(minheights)

        maxrect = 0
        queue = [heights[:]]
        while queue:
            curheights = queue.pop(0)
            if not curheights:
                continue

            n = len(curheights)
            maxh = max(curheights)
            if maxh*n < maxrect:
                continue

            minh = curheights[0]
            minidx = 0
            for i in range(1,n): # find min in this range
                if curheights[i] < minh:
                    minidx = i
                    minh = curheights[i]

            maxrect = max(maxrect,n*minh)
            queue.append(curheights[:minidx])
            queue.append(curheights[minidx+1:])

        return maxrect

def main():
    # heights = [2,1,5,6,2,3]
    heights = [2,2,4,4,4,1]
    test = Solution()
    print(test.largestRectangleArea(heights))

if __name__ == "__main__":
    main()