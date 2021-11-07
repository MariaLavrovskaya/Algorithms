# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_list_iterator = l1
        second_list_iterator = l2
        first_list_array = []
        second_list_array = []
#         check the boundary conditions
        if l1 == None and l2 == None:
            return 
        if l1 == None and l2.next == None:
            return ListNode(l2.val)
        if l2 == None and l1.next == None:
            return ListNode(l1.val)
#         aggregate values in both into different arrays
        while first_list_iterator: 
            first_list_array.append(first_list_iterator.val)
            first_list_iterator = first_list_iterator.next
        while second_list_iterator: 
            second_list_array.append(second_list_iterator.val)
            second_list_iterator = second_list_iterator.next
# sort array in the ascending order and construct a new LinkedList
        new_array = sorted(first_list_array + second_list_array)
        new_list = ListNode(new_array[0])
        # print(iterator)
        iterator = new_list
        for element in new_array[1:]:
            # print(element)
            iterator.next = ListNode(element)
            iterator = iterator.next
            # print(new_list)
        return new_list
            
