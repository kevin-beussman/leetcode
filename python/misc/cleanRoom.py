# Robot Room Cleaner
#from typing import List, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def backtrack(cur,dir):
            i,j = cur
            if cur not in visited:
                visited.add(cur)
                robot.clean()
            for newdir in range(4):
                dx,dy = directions[(dir + newdir) % 4]
                if (i+dx,j+dy) not in visited:
                    if robot.move():
                        backtrack((i+dx,j+dy),(dx,dy))
                        robot.turnRight()
                        robot.turnRight()
                        robot.move()
                        robot.turnLeft()
                    else:
                        robot.turnRight()
            
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()
        backtrack((0,0),0)
        
        pass

def main():
    test = Solution()
    print(test.cleanRoom())

if __name__ == "__main__":
    main()