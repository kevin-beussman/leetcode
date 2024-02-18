class Solution:
    def firstUniqChar(self, s: str) -> int:
        sraw = s
        while s:
            c = s[0]
            n = len(s)
            s = s.replace(c,"")
            if len(s) == n - 1:
                return sraw.find(c)
        return -1
        # for j in range(len(s)):
        #     n = len(s)
        #     if len(s.replace(s[j],"")) == n-1:
        #         return j
        # return -1
        
test = Solution()
print(test.firstUniqChar('leetcodel'))