from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        queue = [(sr,sc)]
        while queue:
            r,c = queue.pop(0)

            if image[r][c] == newColor:
                continue

            if (r+1 < m) and (image[r+1][c] == image[r][c]):
                queue.append((r+1,c))
            if (r-1 >= 0) and (image[r-1][c] == image[r][c]):
                queue.append((r-1,c))
            if (c+1 < n) and (image[r][c+1] == image[r][c]):
                queue.append((r,c+1))
            if (c-1 >= 0) and (image[r][c-1] == image[r][c]):
                queue.append((r,c-1))

            image[r][c] = newColor
        
        return image

# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# newColor = 2
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
test = Solution()
print(test.floodFill(image,sr,sc,newColor))