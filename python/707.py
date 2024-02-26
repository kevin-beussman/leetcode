"""707. Design Linked List
Medium
Topics
Companies

Design your implementation of the linked list. You can choose to use a singly or
doubly linked list. A node in a singly linked list should have two attributes:
val and next. val is the value of the current node, and next is a
pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute prev
to indicate the previous node in the linked list. Assume all nodes in the linked
list are 0-indexed.

Implement the MyLinkedList class:

    MyLinkedList() Initializes the MyLinkedList object.
    
    int get(int index) Get the value of the indexth node in the linked list. If
    the index is invalid, return -1.
    
    void addAtHead(int val) Add a node of value val before the first element of
    the linked list. After the insertion, the new node will be the first node of
    the linked list.
    
    void addAtTail(int val) Append a node of value val as the last element of
    the linked list.
    
    void addAtIndex(int index, int val) Add a node of value val before the
    indexth node in the linked list. If index equals the length of the linked
    list, the node will be appended to the end of the linked list. If index is
    greater than the length, the node will not be inserted.
    
    void deleteAtIndex(int index) Delete the indexth node in the linked list, if
    the index is valid.

 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

 

Constraints:

    0 <= index, val <= 1000
    Please do not use the built-in LinkedList library.
    At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.


"""

from typing import Self
#from functools import lru_cache
#from collections import defaultdict
#import heapq
from dataclasses import dataclass

@dataclass
class Node:
    val: int
    next: Self | None = None

# class Node:

#     def __init__(self, val: int, next: Self | None = None):
#         self.val = val
#         self.next = next

class MyLinkedList:

    def __init__(self, head: Node | None = None):
        self.head = head

    def get(self, index: int) -> int:
        head = self.head
        counter = 0
        while head and counter < index:
            head = head.next
            counter += 1
        return head.val if head else -1

    def addAtHead(self, val: int) -> None:
        self.head = Node(val=val, next=self.head)

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
        else:
            head = self.head
            while head and head.next:
                head = head.next
            head.next = Node(val=val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            prev= self.head
            head = self.head
            counter = 0
            while head and counter < index:
                prev = head
                head = head.next
                counter += 1
            if prev:
                prev.next = Node(val=val, next=head)

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            prev= self.head
            head = self.head
            counter = 0
            while head and counter < index:
                prev = head
                head = head.next
                counter += 1
            if prev and head:
                prev.next = head.next

def main():
    obj = MyLinkedList()
    # obj.addAtHead(1)
    # obj.addAtTail(3)
    # obj.addAtIndex(1, 2)
    # print(obj.get(1))
    # obj.deleteAtIndex(1)
    # print(obj.get(1))

    obj.addAtTail(1)
    obj.addAtTail(3)
    print(obj.get(1))

if __name__ == "__main__":
    main()