# Permutations
from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [nums]

        out = []
        for i,num in enumerate(nums):
            temp = self.permute(nums[:i] + nums[i+1:])
            out += [[num] + j for j in temp]
        
        return out


def main():
    nums = [1,2,3,4]
    test = Solution()
    print(test.permute(nums))

if __name__ == "__main__":
    main()