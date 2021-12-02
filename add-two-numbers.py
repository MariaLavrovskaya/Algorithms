# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def flatten(self, linked_list):
        array = []
        head = linked_list
        while head: 
            array.append(head.val)
            head = head.next
        strings = [str(integer) for integer in array[::-1]]
        print(strings)
        a_string = "".join(strings)
        an_integer = int(a_string)
        return an_integer
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_values = [int(x) for x in str(self.flatten(l1)+self.flatten(l2))][::-1]
#         we construct a a linked list
        new_list = ListNode(new_values[0])
        iterator = new_list
        for element in new_values[1:]:
            iterator.next = ListNode(element)
            iterator = iterator.next
        return new_list
