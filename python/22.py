from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # out = set()
        # stack = [(1,'()')]
        # while stack:
        #     d,cur = stack.pop()
        #     if d < n:
        #         stack.append((d+1,'()' + cur))
        #         stack.append((d+1,'(' + cur + ')'))
        #         stack.append((d+1,cur + '()'))
        #     for j in range(2,n//d+1):
        #         stack.append((d*j,cur*j))
        #     if d == n:
        #         out.add(cur)
        # return list(out)
        out = set()
        countL = 1
        countR = 0
        stack = [(countL,countR,'')]
        while stack:
            countL,countR,cur = stack.pop()
            if len(cur) == 2*n-2:
                out.add('(' + cur + ')')
                continue
            if countL < n:
                stack.append((countL+1,countR,cur + '('))
            if countR < countL:
                stack.append((countL,countR+1,cur + ')'))
        return list(out)
    
test = Solution()
print(test.generateParenthesis(5))

#%%
ans = ["((((()))))","(((()())))","(((())()))","(((()))())","(((())))()","((()(())))","((()()()))","((()())())","((()()))()","((())(()))","((())()())","((())())()","((()))(())","((()))()()","(()((())))","(()(()()))","(()(())())","(()(()))()","(()()(()))","(()()()())","(()()())()","(()())(())","(()())()()","(())((()))","(())(()())","(())(())()","(())()(())","(())()()()","()(((())))","()((()()))","()((())())","()((()))()","()(()(()))","()(()()())","()(()())()","()(())(())","()(())()()","()()((()))","()()(()())","()()(())()","()()()(())","()()()()()"]
test2 = test.generateParenthesis(5)
for j in ans:
    if j not in test2:
        print(j)