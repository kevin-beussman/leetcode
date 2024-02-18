class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1
        for j in range(n-1):
            one,two = one+two,one
        return one

test = Solution()
print(test.climbStairs(5))