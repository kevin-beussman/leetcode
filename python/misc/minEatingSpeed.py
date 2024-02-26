# 875. Koko Eating Bananas
from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for each col, #hours = piles[i]/k round up
        # total hours = piles[i]/k for i in len(piles)
        # extra = -piles[i] % k
        # if we add 1, extra + 1 % k

        maxk = max(piles)+1 #//(h/len(piles))
        mink = -(-sum(piles)//h)

        while mink < maxk:
            midk = (maxk+mink)//2
            time = sum([-(-j//midk) for j in piles])

            if time <= h:
                maxk = midk
            else:
                mink = midk+1

        return mink

def main():
    piles = [3,6,7,11] # 4
    h = 8
    # piles = [30,11,23,4,20] # 23
    # h = 6
    piles = [30,11,23,4,20] # 30
    h = 5
    # piles = [312884470]
    # h = 312884469


    test = Solution()
    print(test.minEatingSpeed(piles,h))

if __name__ == "__main__":
    main()