from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)

        @lru_cache(None)
        def dp(i):
            if i > n-1:
                return 1
            
            if int(s[i]) == 0:
                return 0

            if i == n-1:
                return 1

            next = int(s[i:i+2])

            if next <= 26:
                return dp(i+2) + dp(i+1)
            else:
                return dp(i+1)

        return dp(0)
        
def main():
    # s = "226" # 3
    s = "06"
    # s = "12" # 2
    # s = "162450"
    test = Solution()
    print(test.numDecodings(s))

if __name__ == "__main__":
    main()