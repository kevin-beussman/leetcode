from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n

        stack = [0]
        while stack:
            curroom = stack.pop()
            if visited[curroom]:
                continue
            visited[curroom] = True
            newkeys = rooms[curroom]
            for newroom in newkeys:
                if not visited[newroom]:
                    stack.append(newroom)
        
        return all(visited)

rooms = [[1,3],[3,0,1],[2],[0]]
# rooms = [[1],[2],[3],[]]
test = Solution()
print(test.canVisitAllRooms(rooms))