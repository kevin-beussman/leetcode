# Sort an Array
from typing import List #, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # method 1
        # if len(nums) <= 1:
        #     return nums
        # pivot = nums[0]
        # left = []
        # right = []
        # for n in nums:
        #     if n < pivot:
        #         left.append(n)
        #     elif n > pivot:
        #         right.append(n)
        # return self.sortArray(left) + [pivot] + self.sortArray(right)

        # Divide and Conquer (merge sort)
        if len(nums) <= 1:
            return nums
        half = len(nums)//2
        left = self.sortArray(nums[:half])
        right = self.sortArray(nums[half:])
        out = []
        while left and right:
            if left[0] < right[0]:
                out.append(left.pop(0))
            else:
                out.append(right.pop(0))
        out += left + right # anything remaining in left or right gets appended on end
        return out


def main():
    nums = [5,2,7,3,1,6]
    test = Solution()
    print(test.sortArray(nums))

if __name__ == "__main__":
    main()