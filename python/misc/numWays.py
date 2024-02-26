from functools import lru_cache

class Solution:
    def numWays(self, n: int, k: int) -> int:
        pass
        # either k ways to paint a post
        # or k-1 ways if last 3 were same color
        # 1 state: i

        @lru_cache(None)
        def dp(i): # returns number of ways posts can be colored up to post i
            if i == 1:
                return k
            elif i == 2:
                return k**2
            else:
                return dp(i-1)*(k-1) + dp(i-2)*(k-1)

        return dp(n)
        
def main():
    n = 7 # 42
    # n = 3 # 6
    k = 3
    test = Solution()
    print(test.numWays(n,k))

if __name__ == "__main__":
    main()