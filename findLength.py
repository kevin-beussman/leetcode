# Maximum Length of Repeated Subarray
from typing import List
from functools import lru_cache

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # # top-down DP
        # n1 = len(nums1)
        # n2 = len(nums2)
        
        # @lru_cache(None)
        # def dp(i1, i2):
        #     nonlocal maxlen
        #     if i1 == n1-1 or i2 == n2-1:
        #         if nums1[i1] == nums2[i2]:
        #             return 1
        #         else:
        #             return 0
        #     if nums1[i1] == nums2[i2]:
        #         ans = dp(i1+1,i2+1) + 1
        #         maxlen = max(maxlen,ans)
        #         return ans
        #     else:
        #         return 0

        # maxlen = 0
        # for i in range(n1):
        #     for j in range(n2):
        #         dp(i,j)
        # return maxlen

        # bottom-up DP
        # n1 = len(nums1)
        # n2 = len(nums2)
        
        # maxlen = 0
        # dp = [[0]*n2 for _ in range(n1)]
        # for i1 in range(n1-1,-1,-1):
        #     for i2 in range(n2-1,-1,-1):
        #         if i1 == n1-1 or i2 == n2-1:
        #             if nums1[i1] == nums2[i2]:
        #                 dp[i1][i2] = 1
        #             else:
        #                 dp[i1][i2] = 0
        #             continue
        #         if nums1[i1] == nums2[i2]:
        #             dp[i1][i2] = dp[i1+1][i2+1] + 1
        #             maxlen = max(dp[i1][i2],maxlen)
        # return maxlen

        # bottom-up DP
        n1 = len(nums1)
        n2 = len(nums2)
        
        maxlen = 0
        dp = [[0]*n2 for _ in range(n1)]
        for i1 in range(n1):
            for i2 in range(n2):
                if i1 == 0 or i2 == 0:
                    if nums1[i1] == nums2[i2]:
                        dp[i1][i2] = 1
                elif nums1[i1] == nums2[i2]:
                    dp[i1][i2] = dp[i1-1][i2-1] + 1
                maxlen = max(dp[i1][i2],maxlen)

        return maxlen
                

        

def main():
    # nums1 = [1,2,3,2,1,4,7]
    # nums2 = [1,0,2,0,3,0,2,0,1,0,4,0,7]
    # nums2 = [3,2,1,4,7,8,9,1,2,3,2,1,4]

    # nums1 = [0,1,1,1,1] # 2
    # nums2 = [1,0,1,0,1]

    nums1 = [1,1,0,0,1] # 4
    nums2 = [1,1,0,0,0]

    # nums1 = [5,14,53,80,48] # 1
    # nums2 = [50,47,3,80,83]

    # nums1 = [0,0,0,0,0] # 5
    # nums2 = [0,0,0,0,0]

    # nums1 = [1,2,3,2,8] # 1
    # nums2 = [5,6,1,4,7]

    test = Solution()
    print(test.findLength(nums1,nums2))

if __name__ == "__main__":
    main()
    
