#%%
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = []
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                out.append(l1.val)
                l1 = l1.next
            else:
                out.append(l2.val)
                l2 = l2.next
        else:
            if l1 == None:
                while l2 != None:
                    out.append(l2.val)
                    l2 = l2.next
            else:
                while l1 != None:
                    out.append(l1.val)
                    l1 = l1.next
        if out:
            lout = ListNode(val=out[-1])
            for j in range(len(out)-1):
                lout = ListNode(val=out[-(j+2)],next=lout)
        else:
            lout = None
        return lout

test = Solution()
# l1 = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=4)))
# l2 = ListNode(val=1,next=ListNode(val=3,next=ListNode(val=4)))
l1 = None
l2 = None
testout = test.mergeTwoLists(l1,l2)

#%%
# l1 = [1,2,4]
l1 = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=4)))
# l2 = [1,3,4]
l2 = ListNode(val=1,next=ListNode(val=3,next=ListNode(val=4)))
out = []
for j in range(0,len(l1)+len(l2)):
    if l1[0] < l2[0]:
        out.append(l1.pop(0))
    else:
        out.append(l2.pop(0))