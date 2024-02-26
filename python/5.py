class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if s[1] == s[0]:
            out = s[:2]
        else:
            out = s[0]
        pl = 1
        j = 1
        while j <= len(s) - pl:
            pl = max(1,len(out)//2+1)
            while (j-pl+1 >= 0) and ((j+pl+1) <= len(s)): # even-length palindrome
                s2 = s[j-pl+1:j+pl+1]
                if (s2 == s2[::-1]) and (len(s2) >= len(out)):
                    out = s2
                    pl += 1
                else:
                    break
            
            pl = max(1,len(out)//2)
            while (j-pl >= 0) and ((j+pl+1) <= len(s)): # odd-length palindrome
                s1 = s[j-pl:j+pl+1]
                if (s1 == s1[::-1]) and len(s1) >= len(out):
                    out = s1
                    pl += 1
                else:
                    break
            j += 1
        return out
        # return j
        
# note = 'abbac'
# note = 'abracadabra'
# note = 'abadd'
# note = 'aaaaa'
# note = "iptmykvjanwiihepqhzupneckpzomgvzmyoybzfynybpfybngttozprjbupciuinpzryritfmyxyppxigitnemanreexcpwscvcwddnfjswgprabdggbgcillisyoskdodzlpbltefiz"
test = Solution()
print(test.longestPalindrome(note))