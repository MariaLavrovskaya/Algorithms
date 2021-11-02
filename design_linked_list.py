
#Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
#A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
#If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

#Implement the MyLinkedList class:

#MyLinkedList() Initializes the MyLinkedList object.
#int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
#void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#void addAtTail(int val) Append a node of value val as the last element of the linked list.
#void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
#void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.



class Node: 
    def __init__(self, data):
        self.val = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index< 0 and index > self.size: 
            return -1
        if self.head is None: 
            return -1
        curr = self.head
        for value in range(index):
            if curr.next is None:
                return -1
            else:
                curr = curr.next
        return curr.val if curr !=None else -1


    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        curr = Node(val)
        curr.next = self.head
        self.head = curr
        self.size +=1
        
        
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr= curr.next
            new = Node(val)
            curr.next = new
        
        self.size +=1
        
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        
        node = Node(val)
        
        if index <= 0:
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node.next = curr.next
            curr.next = node

        self.size += 1
            
        

#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         
#         if index < 0 or index > self.size: 
#             return 
        
#         if index == 0:
#             self.head = curr.next
#         else:
#             for value in range(index-1):
#                 curr = curr.next
#             curr = curr.next.next
            
#         self.size -=1
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
