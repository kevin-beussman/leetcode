from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        minh = max(height)
        for e in height:
            if e > 0:
                minh = min(minh,e)
        minh -= 1
        height = [h - minh if h > 0 else 0 for h in height]
        
        n = len(height)
        htfbelow = [True]*n
        water = 0
        iL = 0
        iR = n-1
        for j in range(max(height)):
            htf = [(h - j)>0 for h in height]
            iL = htf[iL:iR+1].index(True) + iL
            if iL == 0:
                iR = n - htf[iR::-1].index(True)
            else:
                iR = n - htf[iR:iL-1:-1].index(True)
                
            # for k in range(iL+1,iR):
            #     if (not htf[k]) and (htfbelow[k]):
            #         htf[k] = True
            #         water += 1
            
            pot = htf[iL+1:iR].count(False)
            htf[iL+1:iR] = htfbelow[iL+1:iR]
            water += pot - htf[iL+1:iR].count(False)
            htfbelow = htf[:]
        return water + minh
            
        
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
test = Solution()
print(test.trap(height))