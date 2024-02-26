# 690. Employee Importance
from typing import List #, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map = {e.id:j for j,e in enumerate(employees)}

        out = 0
        stack = [id]
        while stack:
            e = stack.pop()
            out += employees[employee_map[e]].importance
            for s in employees[employee_map[e]].subordinates:
                stack.append(s)

        return out

def main():
    employees = [Employee(1,5,[7,4]),Employee(4,3,[]),Employee(7,3,[])]
    test = Solution()
    print(test.getImportance(employees,1))

if __name__ == "__main__":
    main()