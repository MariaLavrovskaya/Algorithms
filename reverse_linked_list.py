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
        previous, curr = None, head
        print(curr)
        while curr:
            # save the node to next node     
            nextnode = curr.next
            curr.next = previous
            previous = curr
            curr = nextnode
        return previous
