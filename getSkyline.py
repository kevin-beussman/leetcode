# The Skyline Problem
from typing import List
#from functools import lru_cache
#from collections import defaultdict
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        n = len(buildings)

        finished = set()
        overlaps = []
        for b in buildings:
            overlaps += b[0:2]
        overlaps = list(set(overlaps))
        overlaps.sort() # may not be necessary

        b_at_overlap = {}
        for i,b in enumerate(buildings):
            if b[0] not in b_at_overlap:
                b_at_overlap[b[0]] = [i]
            else:
                b_at_overlap[b[0]].append(i)

        curh = []
        out = []
        prevh = 0
        for x in overlaps:
            if x in b_at_overlap:
                for i in b_at_overlap[x]:
                    heapq.heappush(curh,(-buildings[i][2],i))
            
            while curh and buildings[curh[0][1]][1] <= x:
                heapq.heappop(curh)

            maxh = 0
            if curh:
                maxh = -curh[0][0]
            if maxh != prevh:
                out += [[x,maxh]]
                prevh = maxh

        return out
        # n = len(buildings)

        # out = []
        # ending = []
        # curh = []

        # finished = set()
        
        # s = 0 # buildings started
        # e = 0 # buildings ended
        # while s+e < n*2:
        #     if s == e:
        #         out.append(buildings[s][0:3:2])
        #         heapq.heappush(ending,(buildings[s][1],s))
        #         heapq.heappush(curh,(-buildings[s][2],s))
        #         s += 1
        #         continue
            
        #     if s == n or (ending and ending[0][0] < buildings[s][0]):
        #         e += 1
        #         # losing building b, that had height bh
        #         be,b = heapq.heappop(ending)
        #         bh = -buildings[b][2]

        #         finished.add(b)

        #         prevh = curh[0][0]
        #         while curh and curh[0][1] in finished:
        #             heapq.heappop(curh)

        #         if s == e:
        #             # need to add a point if s==e (we reached the ground floor)
        #             out.append([buildings[b][1],0])
        #         else:
        #             # need to add a point if height changes by losing building b

        #             # if bh == curh[0][0]: # we are losing (a) tallest building
        #             #     heapq.heappop(curh)
        #             if curh[0][0] > prevh: # if we lost THE tallest building, add a point
        #                 out.append([buildings[b][1],-curh[0][0]])
        #     else:
        #         prevh = curh[0][0]
        #         heapq.heappush(curh,(-buildings[s][2],s))
        #         if curh[0][0] < prevh: # we have a new tallest building, add a point
        #             if buildings[s][0] == out[-1][0]:
        #                 out[-1][1] = -curh[0][0]
        #             else:
        #                 out.append([buildings[s][0],-curh[0][0]])

        #         heapq.heappush(ending,(buildings[s][1],s))
        #         s += 1


        # n = len(buildings)-1

        # memo = {}
        # out = []
        # stack = [(0,n)]
        # while stack:
        #     L,R = stack.pop()
        #     print(f'({L},{R})')
        #     if (L,R) in memo:
        #         continue

        #     if R < L:
        #         memo[(L,R)] = []
        #     elif L == R:
        #         memo[(L,R)] = [[buildings[L][0], buildings[L][2]], [buildings[L][1],0]]
        #     else:
        #         M = (L+R)//2
        #         if (L,M) not in memo or (M+1,R) not in memo:
        #             stack.append((L,R))
        #             stack.append((L,M))
        #             stack.append((M+1,R))
        #         else: # merge these two sets of buildings
        #             left = memo[(L,M)]
        #             right = memo[(M+1,R)]

        #             n_l, n_r = len(left), len(right)
        #             i_l, i_r = 0, 0
        #             curh, y_l, y_r = 0, 0, 0
        #             merged = []
        #             while i_l < n_l and i_r < n_r:
        #                 p_l = left[i_l]
        #                 p_r = right[i_r]
        #                 if p_l[0] < p_r[0]:
        #                     x, y_l = p_l
        #                     i_l += 1
        #                 else:
        #                     x, y_r = p_r
        #                     i_r += 1
                        
        #                 maxh = max(y_l, y_r)
                        
        #                 if curh != maxh:
        #                     if not merged or x != merged[-1][0]:
        #                         merged.append([x,maxh])
        #                     else:
        #                         merged[-1][1] = maxh
        #                     curh = maxh
        #             memo[(L,R)] = merged

        # return memo[(0,n)]

def main():
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    # [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    # buildings = [[2,9,10]]
    # buildings = [[1,2,1],[1,2,2],[1,2,3]]
    # [[1,3],[2,0]]
    test = Solution()
    print(test.getSkyline(buildings))

if __name__ == "__main__":
    main()