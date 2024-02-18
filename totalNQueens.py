# N-Queens II
#from typing import List, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def totalNQueens(self, n: int) -> int:
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

        def helper(i):
            if i == n:
                return 1
            temp = 0
            for j in range(n):
                if not board[i][j]:
                    add_queen(i,j,True)
                    temp += helper(i+1)
                    add_queen(i,j,False)
            return temp

        board = [[0]*n for _ in range(n)]
        return helper(0)

def main():
    n = 8
    test = Solution()
    print(test.totalNQueens(n))

if __name__ == "__main__":
    main()