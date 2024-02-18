# 0000: leetcode problem 0000
from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        out = set()
        queue = [(0,0,"")]
        while queue:
            o,c,cur = queue.pop(0)
            if o == n and c == n:
                out.add(cur)
                continue
            else:
                # can either add a "(" or ")" on left or right
                if o < n:
                    queue.append((o+1,c,cur+"("))
                if c < o:
                    queue.append((o,c+1,cur+")"))
        
        return list(out)

def main():
    n = 4
    test = Solution()
    print(test.generateParenthesis(n))

if __name__ == "__main__":
    main()