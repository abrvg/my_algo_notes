"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
    #Create a head
    head = ListNode()
    #create a pointer
    pointer = head

    # Traverse both lists and compare values
    # add the smaller value in the pointer
    while list1 and list2:
        if list1.val < list2.val:
            pointer.next = list1
            list1 = list1.next
        else:
            pointer.next = list2
            list2 = list2.next
        pointer = pointer.next

    # When one list is finished, we do not need to iterate, just add the remaining list
    # since it's already sorted
    pointer.next = list1 or list2
    
    return head.next