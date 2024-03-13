"""271: String Encode and Decode

Design an algorithm to encode a list of strings to a single string. The encoded
string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:

    0 <= strs.length < 100 0 <= strs[i].length < 200 strs[i] contains only
    UTF-8 characters.

"""

from typing import List
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += s + "<kb>"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        return s.split("<kb>")[:-1]


def main():
    test = Solution()
    print(test.decode(test.encode(["neet","code","love","you"])))

if __name__ == "__main__":
    main()
