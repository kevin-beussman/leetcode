# Search a 2D Matrix II
from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if m == 1 and n == 1:
            return matrix[0][0] == target

        quadrants = [[],[],[],[]]
        for i in range(m):
            if i < m//2:
                if n//2 > 0:
                    quadrants[0].append(matrix[i][:n//2])
                quadrants[1].append(matrix[i][n//2:])
            else:
                if n//2 > 0:
                    quadrants[2].append(matrix[i][:n//2])
                quadrants[3].append(matrix[i][n//2:])
        
        for q in quadrants:
            if q and (target >= q[0][0]) and (target <= q[-1][-1]):
                ans = self.searchMatrix(q,target)
                if ans: # need this, because if we just return ans then we might quit before exhausing all 4 quadrants
                    return True
        else:
            return False

def main():
    # matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    # target = 10
    # matrix = [[1,1]]
    # target = 0
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    target = 15
    test = Solution()
    print(test.searchMatrix(matrix,target))

if __name__ == "__main__":
    main()