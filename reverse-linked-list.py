# Given the head of a singly linked list, reverse the list, and return the reversed list.


class Solution:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head 
        previous_history = None
        current = head 
        while current: #while current chain of linked nodes is not exhausted 
            remaining_chain = current.next
            current.next = previous_history
            previous_history=current
            current = remaining_chain
        return previous_history
