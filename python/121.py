from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # out = 0
        # minp = prices[0]
        # for j in range(len(prices)-1):
        #     if prices[j] < minp:
        #         minp = prices[j]
        #         out =  max(max(prices[j+1:]) - prices[j],out)
        # return out
        out = 0
        minp = prices[0]
        maxp = prices[0]
        for j in range(len(prices)-1):
            if prices[j] < minp:
                minp = prices[j]
                maxp = prices[j]
            elif prices[j] > maxp:
                maxp = prices[j]
                out = max(out,maxp-minp)
        return out
        
        
# prices = [7,1,5,3,6,4]
prices = [10,10,10,3,4,4,4,9,2,4,4,4,7]
test = Solution()
print(test.maxProfit(prices))



[10,10,10,3,4,4,4,9,2,4,4,4,7]