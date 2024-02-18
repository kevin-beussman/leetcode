from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # find a 0
        # check neighbors for ones
        # start bfs: stack = (dist=0,r,c)
        # for each neighbor, add to stack if dist+1 < val
        # repeat until stack is empty

        m = len(mat)
        n = len(mat[0])
        visited = [[False for j in range(n)] for k in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    stack = [(0,i,j)]
        
                    while stack:
                        dc,ic,jc = stack.pop()
                        
                        if not visited[ic][jc]:
                            mat[ic][jc] = dc
                            visited[ic][jc] = True
                        else:
                            if mat[ic][jc] > dc:
                                mat[ic][jc] = dc
                            else:
                                continue
                        
                        # add surround 0s
                        if (ic+1 < m) and (mat[ic+1][jc] == 0):
                            stack.append((0,ic+1,jc))
                        if (ic-1 >= 0) and (mat[ic-1][jc] == 0):
                            stack.append((0,ic-1,jc))
                        if (jc+1 < n) and (mat[ic][jc+1] == 0):
                            stack.append((0,ic,jc+1))
                        if (jc-1 >= 0) and (mat[ic][jc-1] == 0):
                            stack.append((0,ic,jc-1))

                        if (ic+1 < m) and (mat[ic+1][jc] > 0):
                            stack.append((dc+1,ic+1,jc))
                        if (ic-1 >= 0) and (mat[ic-1][jc] > 0):
                            stack.append((dc+1,ic-1,jc))
                        if (jc+1 < n) and (mat[ic][jc+1] > 0):
                            stack.append((dc+1,ic,jc+1))
                        if (jc-1 >= 0) and (mat[ic][jc-1] > 0):
                            stack.append((dc+1,ic,jc-1))
                                            
                    return mat

# mat = [[0,0,0],[0,1,0],[1,1,1]]
# mat = [[0]*5,[0]*5,[0,0,0,1,1],[1]*5,[0,1,1,1,1]]
mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
test = Solution()
print(mat)
print(test.updateMatrix(mat))