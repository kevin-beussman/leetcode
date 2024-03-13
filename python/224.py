
"""0000: leetcode problem 0000
problem description
"""

#from typing import List, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def paren_handler(self, s: str) -> list[int]:
        out = []
        prev = ""
        in_paren = 0
        for c in s:
            if (c == "("):
                if in_paren:
                    prev += c
                else:
                    if prev:
                        out.append(prev)
                        prev = ""
                in_paren += 1
            elif (c == ")"):
                in_paren -= 1
                if in_paren:
                    prev += c
                else:
                    out.append(prev)
                    prev = ""
            else:
                prev += c
        if prev:
            out.append(prev)

        tot = 0
        for i, s_out in enumerate(out):
            if i == 0:
                tot += self.calculate(s_out)
            else:
                if out[i - 1][-1] == "-":
                    tot -= self.calculate(s_out)
                else:
                    tot += self.calculate(s_out)
        return tot

    def calculate(self, s: str) -> int:
        s = "".join(c for c in s if c != " ")
        if ("(" in s):
            return self.paren_handler(s)
        
        prev = 0
        op = ""
        idx = 0
        while (idx < len(s)):
            if (s[idx] in "+-"):
                op = s[idx]
                idx += 1
                continue

            curr = ""
            while ((idx < len(s)) and (s[idx] in "0123456789")):
                curr += s[idx]
                idx += 1
            if (not op) or (op == "+"):
                prev += int(curr)
            elif (op == "-"):
                prev -= int(curr)
        return prev


def main():
    test = Solution()
    # print(test.calculate("1 + 1"))
    # print(test.calculate("2-1 + 2"))
    # print(test.calculate("(1+(4+5+2)-3)+(6+8)"))
    print(test.calculate("1-(     -2)"))

if __name__ == "__main__":
    main()
