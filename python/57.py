"""57. Insert Interval
Medium
Topics
Companies

You are given an array of non-overlapping intervals intervals where intervals[i]
= [starti, endi] represent the start and the end of the ith interval and
intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another
interval.

Insert newInterval into intervals such that intervals is still sorted in
ascending order by starti and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start, end = newInterval

        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]

        remove = []
        i = 0
        for i in range(len(intervals) + 1):
            if (i == len(intervals)) or (start <= starts[i]):

                # handle colliding with previous interval
                if (i > 0) and (start <= ends[i - 1]):
                    # merge with prev
                    remove.append(i - 1)
                    start = starts[i - 1]

                # handle colliding with next interval(s)
                j = i
                while (j < len(intervals)) and (starts[j] <= end):
                    remove.append(j)
                    end = max(end, ends[j])
                    j += 1
                break
            elif (start >= starts[i]) and (end <= ends[i]):
                return intervals
            else:
                continue
        print(remove)
        if not remove:
            return intervals[:i] + [[start, end]] + intervals[i:]
        return intervals[:remove[0]] + [[start, end]] + intervals[remove[-1] + 1:]

def main():
    test = Solution()
    print(test.insert([[3,5],[12,15]], [6,6]))

if __name__ == "__main__":
    main()
