# Minimum Cost For Tickets
from typing import List #, Optional
from functools import lru_cache
#import heapq
from collections import defaultdict

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        # find next day after 7 and next day after 30 for each day
        queue7 = []
        queue30 = []
        next7 = {}
        next30 = {}
        for d in range(n):
            while queue7 and days[d] >= days[queue7[0]] + 7:
                next7[queue7.pop(0)] = d
            while queue30 and days[d] >= days[queue30[0]] + 30:
                next30[queue30.pop(0)] = d
            queue7.append(d)
            queue30.append(d)
        
        while queue7: # any remaining items should point past end of days (in dp, this will return 0)
            next7[queue7.pop(0)] = n
        while queue30:
            next30[queue30.pop(0)] = n

        print(next7)
        print(next30)

        @lru_cache(None)
        def dp(d):
            if d >= n:
                return 0
            elif d == n-1:
                return min(costs)
        
            dp7 = next7[d]
            dp30 = next30[d]
            
            buy1 = costs[0] + dp(d+1)
            buy7 = costs[1] + dp(dp7)
            buy30 = costs[2] + dp(dp30)
            return min(buy1,buy7,buy30)

        return dp(0)

def main():
    # days = [1,4,6,7,8,20] # 11
    # costs = [2,7,15]

    # days = [1,2,3,4,5,6,7,8,9,10,30,31] # 17
    # costs = [2,7,15]

    days = [1,4,6,7,8,20] # 6
    costs = [7,2,15]
    test = Solution()
    print(test.mincostTickets(days,costs))

if __name__ == "__main__":
    main()