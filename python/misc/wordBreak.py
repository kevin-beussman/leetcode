from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # state variable:
        # i = where to split string s
        # determine if left and right halves are in satisfy by recursion
        # return "true" if 

        # @lru_cache(maxsize=None)
        # def dp(input):
        #     if input in wordDict:
        #         return True
        #     for i in range(len(input)):
        #         if dp(input[:i]) and dp(input[i:]):
        #             return True
        #     return False
        
        # return dp(s)

        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(1,len(s)+1):
            for word in wordDict:
                if not dp[i]: # when dp[i] becomes true, no need to keep checking other words
                    n = len(word)
                    if i >= n:
                        if s[i-n:i] == word:
                            dp[i] = True and dp[i-n]
                            continue
        
        return dp[len(s)]
                


s = "leetcode"
wordDict = ["leet","code"]
# s = "dogsandcats"
# wordDict = ["dogs","sand","cats"]
# s = "dogs"
# wordDict = ["dog","s","gs"]
test = Solution()
print(test.wordBreak(s,wordDict))