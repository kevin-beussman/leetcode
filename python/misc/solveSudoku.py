# 0000: leetcode problem 0000
from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack(i,j):
            
            if board[i][j] != ".":
                if i == 8 and j == 8:
                    return True
                if j == 8:
                    newi = i+1
                    newj = 0
                else:
                    newi = i
                    newj = j+1
                return backtrack(newi,newj)
            else:
                row = board[i]
                col = [r[j] for r in board]
                box = [board[rownum][colnum] for rownum in range((i//3)*3,(i//3)*3+3) for colnum in range((j//3)*3,(j//3)*3+3)]
                for n in range(1,10):
                    num = str(n)
                    if (num not in row) and (num not in col) and (num not in box):
                        board[i][j] = num
                        if i == 8 and j == 8:
                            return True
                        if j == 8:
                            newi = i+1
                            newj = 0
                        else:
                            newi = i
                            newj = j+1
                        check = backtrack(newi,newj)
                        if check:
                            return check
                        board[i][j] = "."
                return False
        
        backtrack(0,0)
        print(board)

def main():
    # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    test = Solution()
    print(test.solveSudoku(board))

if __name__ == "__main__":
    main()