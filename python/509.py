class Solution:
    def fib(self, n: int) -> int:
        a,b,c = 0,1,1
        j = 2
        while j < n:
            a = b
            b = c
            c = a+b
            j += 1
        return c

test = Solution()
print(test.fib(4))