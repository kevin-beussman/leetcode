from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # housemaxes = {}
        
        # def findMaxRemaining(j,houses):
        #     if j >= len(houses):
        #         return 0
        #     if j not in housemaxes:
        #         housemaxes[j] = max(findMaxRemaining(j+1,houses), findMaxRemaining(j+2,houses) + houses[j])
        #     return housemaxes[j]
        
        # findMaxRemaining(0,nums)
        # return housemaxes[0]

        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0:2])
        for j in range(2,n):
            dp[j] = max(dp[j-1], dp[j-2] + nums[j])

        return dp[-1]
        
def main():
    nums = [2,7,9,3,1]
    # nums = [1,2,3,1]
    # nums = [1,2]
    # nums = [2,1]
    # nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
    # nums = [10,1,1,10] # 20
    test = Solution()
    print(test.rob(nums))

if __name__ == "__main__":
    main()