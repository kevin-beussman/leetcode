"""201: leetcode problem 201
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0

Constraints:
    0 <= left <= right <= 231 - 1
"""
#from typing import List, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # answer will alwasy be between 0 and left

        # continue decreasing right until it reaches left,
        # keeping only the bits that are '&'ed together each step
        while right > left:
            right &= right - 1
        # now right is <= left, so we just keep right
        return right

def main():
    test = Solution()
    print(test.rangeBitwiseAnd(5, 389))

if __name__ == "__main__":
    main()
