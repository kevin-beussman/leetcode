# 134. Gas Station
from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        tot = 0
        tank = 0
        start = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            tot += gas[i] - cost[i]
            if tank < 0:
                start = i+1
                tank = 0

        if tot < 0:
            return -1
        else:
            return start
        


def main():
    # gas = [1,2,3,4,5]
    # cost = [3,4,5,1,2]
    gas = [2,3,4]
    cost = [3,4,3]
    test = Solution()
    print(test.canCompleteCircuit(gas,cost))

if __name__ == "__main__":
    main()