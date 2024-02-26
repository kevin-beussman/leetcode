# Two Sum
from typing import List #, Optional
#from functools import lru_cache
#import heapq

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,n in enumerate(nums):
            hmap[n] = i
        
        for i,n in enumerate(nums):
            if target-n in hmap:
                if hmap[target-n] != i:
                    return [i,hmap[target-n]]

def main():
    nums = [3,3]
    target = 6
    test = Solution()
    print(test.twoSum(nums,target))

if __name__ == "__main__":
    main()