# N-Queens
from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    # def nQueens(self, n: int) -> int:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def add_queen(i,j,add):
            if add:
                c = 1
            else:
                c = -1

            for row in range(n):
                if row == i:
                    for col in range(n):
                        board[row][col] += c
                else:
                    board[row][j] += c
                    if 0 <= j-(i-row) < n:
                        board[row][j-(i-row)] += c
                    if 0 <= j+(i-row) < n:
                        board[row][j+(i-row)] += c
            return

        def helper(i,rep):
            if i == n:
                out.append(rep)
                return 1
            # temp = 0
            for j in range(n):
                if not board[i][j]:
                    add_queen(i,j,True)
                    repj = rep[:]
                    repj[i] = "."*j + "Q" + "."*(n-1-j)
                    # temp += helper(i+1,repj)
                    helper(i+1,repj)
                    add_queen(i,j,False)
            # return temp
            return

        board = [[0]*n for _ in range(n)]
        rep = ["."*n for _ in range(n)]
        out = []
        helper(0,rep)
        return out

def main():
    n = 5
    test = Solution()
    print(test.solveNQueens(n))

if __name__ == "__main__":
    main()