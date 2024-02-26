from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        dif = 10**7
        out = []
        for j in range(1,len(arr)):
            curdif = arr[j] - arr[j-1]
            if curdif < dif:
                dif = curdif
                out = [[arr[j-1],arr[j]]]
            elif curdif == dif:
                out.append([arr[j-1],arr[j]])
        return out

arr = [4,2,1,3]
test = Solution()
print(test.minimumAbsDifference(arr))