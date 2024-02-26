from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2[:]
        
        i = 0
        while nums2 and i < m:
            if nums2[0] <= nums1[i]:
                nums1[i:] = [nums2.pop(0)] + nums1[i:-1]
                i += 1
                m += 1
            else:
                i += 1
        if nums2:
            nums1[-len(nums2):] = nums2
        return nums1
    
test = Solution()
# print(test.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
# print(test.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
print(test.merge(nums1 = [4,0,0,0,0], m = 1, nums2 = [1,2,3,5], n = 4))