from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqlist = {}
        forward = {}
        ineligible = set()
        eligible = set()
        for coursepair in prerequisites:
            if coursepair[0] not in reqlist:
                reqlist[coursepair[0]] = [coursepair[1]]
            else:
                reqlist[coursepair[0]].append(coursepair[1])
            if coursepair[1] not in forward:
                forward[coursepair[1]] = [coursepair[0]]
            else:
                forward[coursepair[1]].append(coursepair[0])
            ineligible.add(coursepair[0])
        
        def addclass(c: int):
            if c not in ineligible:
                out.append(c)
                eligible.discard(c)
                if c in forward:
                    for rc in forward[c]:
                        reqlist[rc].remove(c)
                        if not reqlist[rc]:
                            ineligible.remove(rc)
                            eligible.add(rc)
                    forward.pop(c)
                return True

        if len(ineligible) == numCourses:
            return []
        
        out = []
        for j in range(numCourses):
            addclass(j)
        
        added = True
        while eligible:
            for j in list(eligible):
                addclass(j)
        
        if ineligible:
            return []

        return out
            
# numCourses = 2
# prerequisites = [[0,1]]
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
test = Solution()
print(test.findOrder(numCourses,prerequisites))