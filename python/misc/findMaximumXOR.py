# Maximum XOR of Two Numbers in an Array
from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # # brute force
        # n = len(nums)
        # tried = set()
        # maxxor = 0
        # for i in range(n):
        #     if i not in tried:
        #         tried.add(i)
        #     else:
        #         continue
        #     for j in range(i+1,n):
        #         if j not in tried:
        #             maxxor = max(maxxor,nums[i]^nums[j])
        
        # return maxxor

        # n = len(nums)
        # # generate trie
        # trie = {}
        # for num in nums:
        #     binnum = bin(num)

        pass

def main():
    nums = [14,70,53,83,49,91,36,80,92,51,66,70] # 127
    test = Solution()
    print(test.findMaximumXOR(nums))

if __name__ == "__main__":
    main()