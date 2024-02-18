from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # start with largest possible rectangle m by n
        # search for first row with n contiguous 1's
        # if none, n -= 1 and repeat
        # once found, check next row for ones in same positions
        # continue 
        
        m,n = len(matrix),len(matrix[0])
        out = 0
        for row in range(m):
            rowstr = ""
            for e in matrix[row]:
                rowstr += e
            
            start = n
            while "1"*start not in rowstr:
                start -= 1
            out = max(out,start)
            
            indL = 0
            candidates = []
            while indL >= 0:
                indL = rowstr.find("1"*start,indL+1)
                candidates += indL
            
            # look below candidate
            
            for cand in candidates:
                nrow = row + 1
                nstart = start
                
                while True:
                    nrow += 1
                    nrowstr = ""
                    for e in matrix[nrow][cand:cand + nstart]:
                        nrowstr += e
                    
                    while "1"*nstart not in nrowstr:
                        nstart -= 1
                    
                    cand = nrowstr.find("1"*nstart)
        pass

# matrx = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrx = [["1","0","1","1","1"]]
test = Solution()
print(test.maximalRectangle(matrx))