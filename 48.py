from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        # matrix = [[matrix[i][j] for i in range(m-1,-1,-1)] for j in range(n)]
        # reverse each row first
        for row in matrix:
            row.reverse()
        i,j = 0,0
        for i in range(m):
            for j in range(n-i-1):
                print([i,j,m-1-j,n-1-i])
                matrix[i][j],matrix[m-1-j][n-1-i] = matrix[m-1-j][n-1-i],matrix[i][j]
        print(matrix)


matrix = [[1,2,3],[4,5,6],[7,8,9]] # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
test = Solution()
print(test.rotate(matrix))