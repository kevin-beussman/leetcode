# String to Integer (atoi)
#from typing import List, Optional
#from functools import lru_cache
#import heapq

class Solution:
    def myAtoi(self, s: str) -> int:
        # avoiding using int()
        n = len(s)

        i = 0
        while i < n and s[i] == " ": # ignore leading whitespace
            i += 1
        
        if i == n: # all spaces
            return 0
        
        if not s[i].isnumeric() and s[i] not in ("+","-"): # should be at sign or number now
            return 0

        if not s[i].isnumeric(): # get sign
            if s[i] == "-":
                sign = -1
            else:
                sign = 1
            i += 1
        else:
            sign = 1
        
        strtoint = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        digits = []
        order = -1
        while i < n and s[i].isnumeric():
            digits.append(strtoint[s[i]])
            order += 1
            i += 1
        
        out = 0
        while digits:
            out += digits.pop(0)*10**order
            order -= 1
        
        out *= sign

        if out < -2**31:
            return -2**31
        elif out > 2**31-1:
            return 2**31-1
        else:
            return out

def main():
    s = "   424571"
    # s = "-91283472332"
    # s = "words and 987"
    test = Solution()
    print(test.myAtoi(s))

if __name__ == "__main__":
    main()