from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        headlist = [head.val]
        while head.next != None:
            headlist.append(head.next.val)
            head = head.next
        return headlist == list(reversed(headlist))

head = ListNode(val=5,next=ListNode(val=6,next=ListNode(val=4)))
test = Solution()
print(test.isPalindrome(head))