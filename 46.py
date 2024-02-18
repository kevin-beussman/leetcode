from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        # return result
        
test = Solution()
print(test.permute([1,2,3,4]))
# print(test.permute([0]))