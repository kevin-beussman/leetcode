class Solution:
    def isValid(self, s: str) -> bool:
        pl = {'(':')','[':']','{':'}'}

        stack = [s]
        while stack:
            curstr = stack.pop()

            n = len(curstr)
            if n == 0:
                continue

            if curstr[0] not in pl:
                return False

            ind = 0
            count = 1
            while ind < n-1:
                ind += 1
                if curstr[ind] == curstr[0]:
                    count += 1
                elif curstr[ind] == pl[curstr[0]]:
                    count -= 1
                
                if count == 0:
                    break
            else:
                return False

            stack.append(curstr[1:ind])
            stack.append(curstr[ind+1:])
        
        return True

            

# s = "[({(())}[()])]"
# s = "{}}{"
s = "[(])"
# s = "{}{}()[]"
# s = "}{"
# s = "(]"
# s = "{}{{}}"
# s = "(){}}{"
test = Solution()
print(test.isValid(s))