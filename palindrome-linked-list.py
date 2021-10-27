# Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: 
            return False
        current = head
        array = []
        while current: 
                # array[len(array):] = [current.val]
                array.append(current.val)
                current = current.next
        if array == array[::-1]:
            return True
