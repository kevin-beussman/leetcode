from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inf = 2**31 - 1
        m = len(rooms)
        n = len(rooms[0])
        
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((0,i,j))
        
        while queue:
            step,ic,jc = queue.pop(0)
            if (rooms[ic][jc] == inf) or (rooms[ic][jc] == 0):
                rooms[ic][jc] = step
                step += 1
                if (ic+1 < m) and (rooms[ic+1][jc] == inf):
                    queue.append((step,ic+1,jc))
                if (ic-1 >= 0) and (rooms[ic-1][jc] == inf):
                    queue.append((step,ic-1,jc))
                if (jc+1 < n) and (rooms[ic][jc+1] == inf):
                    queue.append((step,ic,jc+1))
                if (jc-1 >= 0) and (rooms[ic][jc-1] == inf):
                    queue.append((step,ic,jc-1))
        

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
test = Solution()
test.wallsAndGates(rooms)
print(rooms)