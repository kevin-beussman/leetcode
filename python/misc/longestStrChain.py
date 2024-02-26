# 1048. Longest String Chain
from typing import List
from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # top-down DP
        # @lru_cache(None)
        # def dp(s):
        #     if not s:
        #         return 0
        #     if s not in words:
        #         return 0
            
        #     temp = 0
        #     for i,l in enumerate(s):
        #         temp = max(temp,dp(s[:i] + s[i+1:]) + 1)
        #     return temp
        
        # return max(dp(word) for word in words)

        # bottom-up DP
        # sort words by size:
        n = len(words)
        words.sort(key=lambda x:len(x)) # O(n*logn)
        ind_lookup = {word:i for i,word in enumerate(words)}

        dp = [1]*n
        for i,s in enumerate(words):
            for j in range(len(s)):
                s_prev = s[:j] + s[j+1:]
                if s_prev in ind_lookup:
                    dp[i] = max(dp[i], dp[ind_lookup[s_prev]] + 1)
        
        return max(dp)


def main():
    # words = ["a","b","ba","bca","bda","bdca"] # 4
    # words = ["xbc","pcxbcf","xb","cxbc","pcxbc"] # 5
    # words = ['a','ab','abc','dabc','edabc','efdabc'] # 6
    # words = ['a'] # 1
    # words = ['a','b'] # 1
    words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]

    test = Solution()
    print(test.longestStrChain(words))

if __name__ == "__main__":
    main()