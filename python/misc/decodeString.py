class Solution:
    # def decodeString(self, s: str) -> str:
    #     memo = {}
    #     stack = [(1,s)]
    #     while stack:
    #         curm,curs = stack.pop()
    #         m = ""
    #         allm = []
    #         count = 0
    #         next = ""
    #         allnext = []
    #         pre = ""
    #         post = ""
    #         for j,c in enumerate(curs):
    #             if count > 0:
    #                 next += c
    #             elif c.isnumeric():
    #                 m += c
    #             else:

    #             if c == "[":
    #                 count += 1
    #                 allm.append(int(m))
    #                 m = ""
    #             elif c == "]":
    #                 count -= 1
            
    #         next = next[:-1]
    #         pre = pre[:-1]
    #         if m:
    #             m = int(m)

    #         if not allm:
    #             memo[(curm,curs)] = curs*curm
    #         else:
    #             if (m,next) not in memo:
    #                 stack.append((curm,curs))
    #                 stack.append((int(m),next))
    #             else:
    #                 memo[(curm,curs)] = (pre + memo[m,next])*curm
        
    #     return memo[(1,s)]

    def decodeString(self, s: str) -> str:

        memo = {}
        stack = [s]
        while stack:
            curs = stack.pop()
            m = ""
            next = ""
            word = ""
            count = 0
            todo = []
            for c in curs:
                if c == "]":
                    count -= 1
                    if count == 0:
                        if next in memo:
                            word += memo[next]*mnext
                        else:
                            todo.append(next)
                        next = ""

                if count > 0:
                    next += c
                elif c.isnumeric():
                    m += c
                elif c.isalpha():
                    word += c

                if c == "[":
                    count += 1
                    if count == 1:
                        mnext = int(m)
                        m = ""

            if todo:
                stack.append(curs)
                for j in todo:
                    stack.append(j)
            else:
                memo[curs] = word
        
        return memo[s]

s = "3[a2[c]b3[d]]"
# s = "2[abc]3[cd]ef"
test = Solution()
print(test.decodeString(s))