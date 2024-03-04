"""74. Search a 2D Matrix
Solved
Medium
Topics
Companies

You are given an m x n integer matrix matrix with the following two properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top < bottom - 1:
            mid = bottom + (top - bottom) // 2
            if matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid
        
        if target >= matrix[bottom][0]:
            row = bottom
        else:
            row = top

        left = 0
        right = len(matrix[row]) - 1
        while left < right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        mid = left + (right - left) // 2
        if matrix[row][mid] == target:
            return True
        return False

def main():
    test = Solution()
    # print(test.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
    print(test.searchMatrix(matrix=[[1],[3]], target=2))

if __name__ == "__main__":
    main()
