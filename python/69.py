class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1,x
        while l != r-1:
            m = (l+r)//2
            if m*m > x:
                r = m
            elif m*m < x:
                l = m
            else:
                return m
        return l

test = Solution()
print(test.mySqrt(10))