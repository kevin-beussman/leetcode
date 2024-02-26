from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for j in range(1,n+1):
            if not (j % 5):
                if not (j % 3):
                    out.append("FizzBuzz")
                else:
                    out.append("Buzz")
            elif not (j % 3):
                out.append("Fizz")
            else:
                out.append(str(j))
        return out

test = Solution()
print(test.fizzBuzz(7))