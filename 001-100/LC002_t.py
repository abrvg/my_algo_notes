"""
You are given two non-empty linked list representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contain a single digit. Add the two numbers and return the sum as a linked list

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example
input: l1 = [2,4,3], l2 = [5,6,4]
output: [7,0,8]
Explanation: 342 + 465 = 807
"""

# Definition of singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
    """
	Extract the digits as strings and concatenate them
	Reverse the strings, cast to integers and make the sum.
	Cast the sum to string, reverse it
	Iterate the reverse string and create the nodes and output list
	
	"""
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
	
	num1 = num2 = ""
	
	while l1:
		num1 += str(l1.val)
		l1 = l1.next

	while l2:
		num2 += str(l2.val)
		l2 = l2.next

	res = str(int(num1[::-1]) + int(num2[::-1]))[::-1]

	n = ListNode()
	head = n

	for i in res:
		n.next = ListNode(i)
		n = n.next
		
	return head.next	
