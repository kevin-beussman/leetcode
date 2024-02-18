from typing import List
from functools import lru_cache

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # using hashmap recursion
        # pointmap = {():0}
        # def dp(numlist):
        #     if numlist not in pointmap:
        #         if len(numlist) == 1:
        #             pointmap[numlist] = numlist[0]
        #         else:
        #             maxnum = max(numlist)
        #             maxcount = numlist.count(maxnum)
        #             take,notake = [],[]
        #             for val in numlist:
        #                 if val != maxnum:
        #                     notake.append(val)
        #                     if val != (maxnum-1):
        #                         take.append(val)
        #             if (maxnum-1) in numlist:
        #                 pointmap[numlist] = max(maxnum*maxcount + dp(tuple(take)), dp(tuple(notake)))
        #             else:
        #                 pointmap[numlist] = maxnum*maxcount + dp(tuple(take))
        #     return pointmap[numlist]
        
        # return dp(tuple(nums))

        # using cache recursive
        # @lru_cache(maxsize=None)
        # def dp(numlist):
        #     if len(numlist) == 0:
        #         return 0
        #     elif len(numlist) == 1:
        #         return numlist[0]
        #     else:
        #         maxnum = max(numlist)
        #         maxcount = numlist.count(maxnum)
        #         take,notake = [],[]
        #         for val in numlist:
        #             if val != maxnum:
        #                 notake.append(val)
        #                 if val != (maxnum-1):
        #                     take.append(val)
        #         if (maxnum-1) in numlist:
        #             return max(maxnum*maxcount + dp(tuple(take)), dp(tuple(notake)))
        #         else:
        #             return maxnum*maxcount + dp(tuple(take))
        
        # return dp(tuple(nums))

        # bottom-up DP
        nums.sort()
        n = len(nums)
        c = []
        c.append(nums.count(nums[0]))
        dp = []
        dp.append(nums[0]*c[0])
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                c.append(nums.count(nums[i]))
                if nums[i] == nums[i-1]+1:
                    if len(dp) == 1:
                        dp.append(max(dp[-1],nums[i]*c[-1]))
                    else:
                        dp.append(max(dp[-1],dp[-2] + nums[i]*c[-1]))
                else:
                    dp.append(dp[-1] + nums[i]*c[-1])
        
        return dp[-1]
        
def main():
    # nums = [2,7,9,3,1] # 20
    # nums = [2,2,3,3,3,4] # 9
    # nums = [3,4,2] # 6
    # nums = [1,1,1,1,1,2,2] # 5
    # nums = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3]
    nums = [12,32,93,17,100,72,40,71,37,92,58,34,29,78,11,84,77,90,92,35,12,5,27,92,91,23,65,91,85,14,42,28,80,85,38,71,62,82,66,3,33,33,55,60,48,78,63,11,20,51,78,42,37,21,100,13,60,57,91,53,49,15,45,19,51,2,96,22,32,2,46,62,58,11,29,6,74,38,70,97,4,22,76,19,1,90,63,55,64,44,90,51,36,16,65,95,64,59,53,93]
    test = Solution()
    print(test.deleteAndEarn(nums))

if __name__ == "__main__":
    main()