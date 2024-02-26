from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        stack = []
        for j,h in enumerate(height):
            if not stack:
                stack.append((h,h,j)) # height, tallest height to left, index
                continue

            if h < stack[-1][1]:
                stack.append((h,stack[-1][1],j))
                continue
            else:
                while stack and (h >= stack[-1][0]):
                    hl,hmaxl,jl = stack.pop()
                    water += min(h,hmaxl) - hl
                stack.append((h,h,j))
        
        while stack:
            h,hmaxl,j = stack.pop()
            while stack and (h >= stack[-1][0]):
                hl,hmaxl,jl = stack.pop()
                water += h - hl

        return water
        
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
test = Solution()
print(test.trap(height))