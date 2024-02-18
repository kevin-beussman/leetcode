from typing import List
from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # state variables:
        # ijob = job index
        # iday = day number

        n = len(jobDifficulty)

        if n < d:
            return -1
        
        # @lru_cache(maxsize=None)
        # def dp(ijob,iday):
        #     if iday == d:
        #         return max(jobDifficulty[ijob:])
            
        #     temp = dp(ijob+1,iday+1) + jobDifficulty[ijob]
        #     rem_n = (n - ijob)
        #     rem_d = (d - iday)
        #     for njobs in range(2,rem_n - rem_d + 1): # need to leave 1 job for each day after iday
        #         hardest = max(jobDifficulty[ijob:ijob+njobs]) # this is slow, see below iterative
        #         temp = min(temp,dp(ijob+njobs,iday+1) + hardest)
        #     return temp

        # return dp(0,1)


        dp = [[-1]*d for j in range(n)]

        # fill up base case day d:
        for ijob in range(d-1,n):
            dp[ijob][d-1] = max(jobDifficulty[ijob:])

        for iday in range(d-1,0,-1):
            for ijob in range(iday-1,n - (d-iday)):
                
                rem_n = n - ijob
                rem_d = d - iday
                hardest = jobDifficulty[ijob]
                temp = dp[ijob+1][iday] + hardest
                for njobs in range(2,rem_n - rem_d + 1):
                    hardest = max(hardest, jobDifficulty[ijob+njobs-1])
                    temp = min(temp,dp[ijob+njobs][iday] + hardest)
                dp[ijob][iday-1] = temp
        
        return dp[0][0]



def main():
    jobDifficulty = [6,5,4,3,2,1]
    d = 2
    # jobDifficulty = [1,1,1]
    # d = 2
    test = Solution()
    print(test.minDifficulty(jobDifficulty,d))

if __name__ == "__main__":
    main()