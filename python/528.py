from random import uniform
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        wsum = sum(w)
        self.edges = [0]
        for index,weight in enumerate(w[:-1]):
            self.edges.append(weight/wsum + self.edges[index])
            

    def pickIndex(self) -> int:
        tempval = uniform(0,1)
        print(tempval)
        print(self.edges)
        a = 0
        b = len(self.edges)
        while a != b-1:
            mid = (a+b)//2
            if self.edges[mid] > tempval:
                b = mid
            else:
                a = mid
        return a

test = Solution([3,14,1,7])
print(test.pickIndex())