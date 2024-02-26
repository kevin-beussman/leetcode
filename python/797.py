from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # out = []
        # end = len(graph) - 1
        
        # def goDeep(s,i):
        #     s.append(i)
        #     if i == end:
        #         out.append(s[:])
        #         return
        #     for j in graph[i]:
        #         goDeep(s,j)
        #         s.pop()
        
        # goDeep([],0)
        # return out
    
        if not graph:
            return[]
        
        stack = [(0, [0])]
        result = []
        while stack:
            node, path = stack.pop()
            
            if node==len(graph)-1:
                result.append(path)
            
            for neighbour in graph[node]:
                stack.append((neighbour, path+[neighbour]))
        return result

    
# graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]
test = Solution()
print(test.allPathsSourceTarget(graph[:]))

#%%
def goDeep(s,i):
    s.append(i)
    if i == end:
        return s
    for j in graph[s[-1]]:
        goDeep(s,i)

graph = [[4,3,1],[3,2,4],[3],[4],[]]
end = len(graph) - 1
goDeep([],0)