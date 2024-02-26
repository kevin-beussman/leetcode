"""61. Rotate List
Medium
Topics
Companies

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        originalhead = head

        # get length of list
        list_length = 0
        while head:
            list_length += 1
            head = head.next
        n_from_end = k % list_length

        if n_from_end == 0:
            return originalhead

        head = originalhead
        head_n_forward = head
        count = 0
        while head_n_forward and head_n_forward.next and (count < n_from_end):
            head_n_forward = head_n_forward.next
            count += 1
        
        lefthead = ListNode()
        left = lefthead
        while head_n_forward:
            left.next = ListNode(head.val)
            left = left.next
            head = head.next
            head_n_forward = head_n_forward.next
        
        rotated = head
        while rotated and rotated.next:
            rotated = rotated.next
        rotated.next = lefthead.next

        # Debugging
        vals = []
        sent = head
        while sent:
            vals.append(sent.val)
            sent = sent.next
        print(vals)

        return head

def main():
    test = Solution()
    # print(test.rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4))
    print(test.rotateRight(ListNode(1, ListNode(2)), 1))

if __name__ == "__main__":
    main()
