from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        out = defaultdict(int)
        for entry in cpdomains:
            s1 = entry.split(" ", 1)
            num = int(s1[0])

            dom = s1[1]
            out[dom] += num
            while '.' in dom:
                dom = dom.split(".", 1)[1]
                out[dom] += num
        
        out2 = []
        for key in out:
            out2.append(str(out[key]) + " " + key)
        return out2
        
            

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
test = Solution()
print(test.subdomainVisits(cpdomains))

# test = "900 google.mail.com"
# out = test.split(" ")
# out2 = out[1].split(".",1)
# print(out[1])
# print('.' in out[1])