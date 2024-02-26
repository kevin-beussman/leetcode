from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        memo = {}
        def pascal(row,col):
            if (row == 0) or (col == 0) or (col == row):
                memo[(row,col)] = 1
            else:
                if (row-1,col-1) not in memo:
                    memo[(row-1,col-1)] = pascal(row-1,col-1)
                if (row-1,col) not in memo:
                    memo[(row-1,col)] = pascal(row-1,col)
                memo[(row,col)] = memo[(row-1,col-1)] + memo[(row-1,col)]
            return memo[(row,col)]
        
        out = []
        for j in range(rowIndex+1):
            out.append(pascal(rowIndex,j))
        
        return out

        
test = Solution()
print(test.getRow(3))