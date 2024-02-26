from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        out = [intervals.pop(0)]
        while intervals:
            c = intervals.pop(0)
            if c[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1],c[1])
            else:
                out.append(c)
        return out


intervals = [[8,10],[15,18],[1,3],[2,6]]
test = Solution()
print(test.merge(intervals))