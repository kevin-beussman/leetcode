class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        haystack.find(needle)

test = Solution()
print(test.strStr('hello','ll'))