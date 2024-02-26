from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # kadane's

        cur = prices[0]
        maxprof = 0
        for p in prices:
            if p < cur:
                cur = p
            else:
                maxprof = max(maxprof,p-cur)
        
        return maxprof
        
def main():
    # prices = [1,2,3,0,2] # 2
    # prices = [7,1,5,3,6,4] # 5
    prices = [7,6,4,3,1] # 0
    # prices = [1]
    test = Solution()
    print(test.maxProfit(prices))

if __name__ == "__main__":
    main()