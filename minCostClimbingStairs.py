from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        results = [cost[0],cost[1],0]

        for k in range(2,n):
            results[2] = min(results[1],results[0]) + cost[k]
            results[0],results[1] = results[1],results[2]
        
        return min(results[0],results[1])
        

def main():
    # cost = [1,100,1,1,1,100,1,1,100,1] # 6
    cost = [10,15,20] # 30
    test = Solution()
    print(test.minCostClimbingStairs(cost))

if __name__ == "__main__":
    main()