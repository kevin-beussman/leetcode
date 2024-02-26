class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = 0
        seen = {}
        ls = 0
        for j in range(0,len(s)):
            if s[j] in seen:
                ls = max(ls,seen[s[j]] + 1)
            seen[s[j]] = j
            out = max(out,j - ls + 1)
        return out
    
s = "abcababa"
# s = "bbbbbab"
# s = "abba"
test = Solution()
print(test.lengthOfLongestSubstring(s))