class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # kth term in nth row is going to come from the (k//2)th term from (n-1)th row
        if n == 1: # base case
            return 0
        
        temp = self.kthGrammar(n-1,k//2 + k%2) # get (k//2)th term from (n-1)th row
        if temp: # k is in "10"
            if k%2: # if k is even
                return 1
            else:
                return 0
        else: # k is in "01"
            if k%2:
                return 0
            else:
                return 1

n = 2
k = 2
test = Solution()
print(test.kthGrammar(n,k))