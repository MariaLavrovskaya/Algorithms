


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.


class Solution(object):
    def __init__(self):
        self.head = None
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        iterator = 1
        
        odd_chain_iterator = ListNode(head.val)
        odd_chain = odd_chain_iterator
        
        even_chain_iterator = ListNode(head.next.val)
        even_chain = even_chain_iterator
        
        current = head.next.next
        while current: 
            iterator+=1
            remaining_chain = current.next
            if iterator % 2 == 0:
                current.next = None
                odd_chain_iterator.next = current
                current = remaining_chain
                odd_chain_iterator = odd_chain_iterator.next
            else:
                current.next = None
                even_chain_iterator.next = current
                current = remaining_chain
                even_chain_iterator = even_chain_iterator.next
        odd_chain_iterator.next = even_chain
        return odd_chain
