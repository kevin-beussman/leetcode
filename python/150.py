from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arith = ("+","-","*","/")
        
        stack = []
        for t in tokens:
            if t in arith:
                tm1 = stack.pop()
                tm2 = stack.pop()
                stack.append(str(int(eval(tm2 + t + tm1))))
            else:
                stack.append(t)
        
        return stack.pop()


# tokens = ["2","1","+","3","*"] 
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]       
test = Solution()
print(test.evalRPN(tokens))