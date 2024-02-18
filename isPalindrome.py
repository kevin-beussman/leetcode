# Valid Palindrome
#from typing import List, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to lowercase alphas
        letters = [char for char in s if char.isalnum()]
        newstr = "".join(letters).lower()

        print(newstr)
        l,r = 0,len(newstr)-1
        while l <= r:
            if newstr[l] != newstr[r]:
                return False
            l += 1
            r -= 1
        return True

def main():
    # s = "abba"
    # s = "abcdba"
    # s = "A man, a plan, a canal: Panama"
    s = "0P"
    test = Solution()
    print(test.isPalindrome(s))

if __name__ == "__main__":
    main()