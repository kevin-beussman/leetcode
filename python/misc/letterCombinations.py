# Letter Combinations of a Phone Number
from typing import List #, Optional
from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        # phone = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        @lru_cache(None)
        def helper(i):
            if i == n:
                return [""]
            poss = phone[digits[i]]
            ans = []
            for char in poss:
                ans += [char + j for j in helper(i+1)]
            return ans
        
        return helper(0) if n > 0 else []

def main():
    digits = "2"
    test = Solution()
    print(test.letterCombinations(digits))

if __name__ == "__main__":
    main()