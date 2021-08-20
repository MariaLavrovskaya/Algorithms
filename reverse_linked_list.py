# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        prev, curr = None, head
        print(curr)
        while curr:
            # save the node to next node     
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
