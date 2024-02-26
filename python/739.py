from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        out = [0]*len(temperatures)

        j = 0
        stack = []
        for j,t in enumerate(temperatures):
            if not stack:
                stack.append((j,t))
                continue

            if t < stack[-1][1]:
                stack.append((j,t))
            else:
                while stack and t > stack[-1][1]:
                    (jo,to) = stack.pop()
                    out[jo] = j - jo
                stack.append((j,t))
        
        return out

# temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
test = Solution()
print(test.dailyTemperatures(temperatures))