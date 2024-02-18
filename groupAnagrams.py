# Group Anagrams
from typing import List #, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sortstr(word):
            # binary sort string
            if len(word) <= 1:
                return word
            left, mid, right = "", "", ""
            for letter in word[1:]:
                if letter < word[0]:
                    left += letter
                elif letter > word[0]:
                    right += letter
                else:
                    mid += letter
            return sortstr(left) + word[0] + mid + sortstr(right)

        hmap = {}
        for s in strs:
            s_sorted = sortstr(s)
            if s_sorted not in hmap:
                hmap[s_sorted] = [s]
            else:
                hmap[s_sorted] += [s]

        return [hmap[key] for key in hmap]

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    test = Solution()
    print(test.groupAnagrams(strs))

if __name__ == "__main__":
    main()