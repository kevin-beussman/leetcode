from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        def backtracking(s):
            if s == len(nums):
                out.append(nums[:])
                return
            
            completed = set()
            
            for j in range(s,len(nums)):
                if nums[j] not in completed:
                    nums[s],nums[j] = nums[j],nums[s]
                    backtracking(s+1)
                    nums[s],nums[j] = nums[j],nums[s]
                    completed.add(nums[j])
                
        backtracking(0)
        return out
        # def permAll(start):
        #     if len(start) == 0:
        #         return []
            
        #     if len(start) == 1:
        #         return start
            
        #     out = []
        #     for j in range(len(start)):
        #         rem = start[:]
        #         node = rem.pop(j)
                
        #         for p in permAll(rem):
        #             out.append([node, p])
        #     return out
        
        # result = permAll(nums)
        # result_set = set()
        # if len(result) == 1:
        #     return [result]
        # for k in range(len(result)):
        #     cont = True
        #     while cont:
        #         temp = []
        #         cont = False
        #         for item in result[k]:
        #             if type(item) == int:
        #                 temp += [item]
        #             else:
        #                 temp += item
        #                 cont = True
        #         result[k] = temp
        #     result_set.add(tuple(result[k]))
        # return [list(k) for k in result_set]
        
test = Solution()
print(test.permuteUnique([1,2,3,4,5,6]))
# print(test.permute([0]))