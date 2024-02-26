from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # def helper(ln,newnext):
        #     if not ln.next:
        #         ln.next = newnext
        #         return ln
        #     else:
        #         test = ln.next
        #         ln.next = newnext
        #         return helper(test,ln)
        
        # return helper(head,None)

        if not head or not head.next:
            return head
        else:
            test = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return test

head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
test = Solution()
temp = test.reverseList(head)
print(temp.val)
while temp.next:
    temp = temp.next
    print(temp.val)
    