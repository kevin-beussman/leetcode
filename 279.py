import time

class Solution:
    def numSquares(self, n: int) -> int:
        num = 1
        numsq = 1
        numsqlist = []
        while numsq <= n:
            numsqlist.append(numsq)
            num += 1
            numsq = num**2
        
        queue = [(0,0)]
        while queue:
            tot,out = queue.pop(0)
            if tot == n:
                return out
            if (n - tot) in numsqlist:
                return out + 1
            for numsq in numsqlist[::-1]:
                if tot + numsq < n:
                    queue.append((tot + numsq,out + 1))


 
test = Solution()
start_time = time.time()
print(test.numSquares(7168))
print("--- %.8f seconds ---" % (time.time() - start_time))
