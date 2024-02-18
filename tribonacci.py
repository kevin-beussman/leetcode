class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n

        out = [0]*(n+1)
        out[0],out[1],out[2] = 0,1,1

        for k in range(3,n+1):
            out[k] = out[k-3] + out[k-2] + out[k-1]
        
        return out[n]
        
test = Solution()
print(test.tribonacci(25))