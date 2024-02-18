# Longest Palindromic Substring
#from typing import List, Optional
from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dynamic programming with one index
        # @lru_cache(None)
        # def dp(i): # returns largest palindrome up to and including i
        #     if i == 0:
        #         return 1
        #     prev = i - dp(i-1) - 1
        #     if prev >= 0 and s[i] == s[prev]:
        #         ans = dp(i-1) + 2
        #     else: # not part of previous longest
        #         ans = 1
        #         j = 1
        #         while i-j >= 0 and s[i] == s[i-j]: # while loop checks long repeating chars
        #             ans += 1
        #             j += 1
        #     if ans > self.maxlen:
        #         self.maxlen = ans
        #         self.out = s[i-ans+1:i+1]
        #     return ans
        
        # self.maxlen = 1
        # self.out = s[0]
        # print([dp(j) for j in range(len(s))])
        # dp(len(s)-1)
        # return self.out

        # iterative
        if len(s) == 1:
            return s
        if s[1] == s[0]:
            out = s[:2]
        else:
            out = s[0]
        pl = 1
        j = 1
        while j <= len(s) - pl:
            pl = max(1,len(out)//2+1)
            while (j-pl+1 >= 0) and ((j+pl+1) <= len(s)): # even-length palindrome
                s2 = s[j-pl+1:j+pl+1]
                if (s2 == s2[::-1]) and (len(s2) >= len(out)):
                    out = s2
                    pl += 1
                else:
                    break
            
            pl = max(1,len(out)//2)
            while (j-pl >= 0) and ((j+pl+1) <= len(s)): # odd-length palindrome
                s1 = s[j-pl:j+pl+1]
                if (s1 == s1[::-1]) and len(s1) >= len(out):
                    out = s1
                    pl += 1
                else:
                    break
            j += 1
        return out

def main():
    # s = "babad"
    # s = "cbbd"
    # s = "abrarbacada"
    # s = "bbb"
    # s = "aba"
    # s = "sabbbbbasdf"
    s = "nvavnvavn"
    test = Solution()
    print(test.longestPalindrome(s))

if __name__ == "__main__":
    main()