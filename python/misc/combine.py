# Combinations
from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(cur):
            if len(cur) == k:
                return [cur]

            temp = []
            if not cur:
                start = 1
            else:
                start = cur[-1] + 1
            for i in range(start,n+1):
                temp += backtrack(cur + [i])
            return temp
        
        return backtrack([])

def main():
    n = 4
    k = 3
    test = Solution()
    print(test.combine(n,k))

if __name__ == "__main__":
    main()