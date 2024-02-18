from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        if list2.val < list1.val:
            temp = list2
            list2 = list2.next
        else:
            temp = list1
            list1 = list1.next
        
        temp.next = self.mergeTwoLists(list1,list2)
        return temp

list1 = ListNode(1,ListNode(2,ListNode(3)))
list2 = ListNode(1,ListNode(4,ListNode(5)))
# list1 = ListNode(1)
# list2 = None
test = Solution()
temp = test.mergeTwoLists(list1,list2)
print(temp.val)
while temp.next:
    temp = temp.next
    print(temp.val)