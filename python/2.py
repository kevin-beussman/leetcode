from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

		l1str = ''
		for j in l1:
			l1str = str(j) + l1str
		l1num = int(l1str)

		l2str = ''
		for j in l2:
			l2str = str(j) + l2str
		l2num = int(l2str)

		sum = [int(j) for j in str(l1num + l2num)]
		sum.reverse()
		return(sum)

test = Solution()
print(test.addTwoNumbers([2,4,3],[5,6,4]))

#%%
# l1 = [2,4,3]
l1 = ListNode(val=2,next=ListNode(val=4,next=ListNode(val=3)))
# l2 = [5,6,4]
l2 = ListNode(val=5,next=ListNode(val=6,next=ListNode(val=4)))

l1str = str(l1.val)
while l1.next != None:
	l1 = l1.next
	l1str = str(l1.val) + l1str
l1num = int(l1str)

l2str = str(l2.val)
while l2.next != None:
	l2 = l2.next
	l2str = str(l2.val) + l2str
l2num = int(l2str)

sumstr = str(l1num + l2num)
sum = ListNode(val=sumstr[0])
for j in range(len(sumstr)-1):
	sum = ListNode(val=sumstr[j+1],next=sum)
print(sum)