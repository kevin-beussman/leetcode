"""19. Remove Nth Node From End of List
Medium
Topics
Companies
Hint

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow up: Could you do this in one pass?
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        original_head = head
        head_n_forward = head
        count = 0
        while head_n_forward and head_n_forward.next and (count < n):
            head_n_forward = head_n_forward.next
            count += 1
        
        while head_n_forward.next:
            head = head.next
            head_n_forward = head_n_forward.next
        
        # handle when we want to remove the first head
        if head is original_head and (count < n):
            original_head = original_head.next
        else:
            head.next = head.next.next
        
        # Debugging
        vals = []
        sent = original_head
        while sent:
            vals.append(sent.val)
            sent = sent.next
        print(vals)

        return original_head

def main():
    test = Solution()
    # print(test.removeNthFromEnd(ListNode(1), 1))
    print(test.removeNthFromEnd(ListNode(1, ListNode(2)), 1))
    print(test.removeNthFromEnd(ListNode(1, ListNode(2)), 2))

if __name__ == "__main__":
    main()
