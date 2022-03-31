#Leetcode #21 merge two sorted lists 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
    
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                
            else:
                 tail.next = l2
                 l2 = l2.next
                
            tail = tail.next
            
            
        if l1:
        
            tail.next = l1
       
        elif l2:
            tail.next = l2
            
            
        return dummy.next
    
    
#     #Leetcode #21. Merge Two Sorted Lists
# # how to create a list in python first thing to consider
# # A single node of a singly linked list
# class Node:
#     # constructor
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# # A Linked List class with a single head node
# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

#     # insertion method for the linked list
#     def insert(self, data):
#         newNode = Node(data)
#         if (self.head):
#             current = self.head
#             while (current.next):
#                 current = current.next
#             current.next = newNode
#         else:
#             self.head = newNode

#     # print method for the linked list
#     def printLL(self):

#         current = self.head
#         while (current):
#             print(current.data, "->")
#             current = current.next


#     def merged_list(self,List_1, List_2):
        
#         current_1 = List_1.head
#         current_2 = List_2.head

#         while current_1.next and current_2.next:

#                 newnode_1 = Node(current_1.data)
#                 newnode_2 = Node(current_2.data)

#                 if self.head:
#                     curr = self.head

#                     while curr.next:
#                         curr = curr.next
#                     if current_1.data <= current_2.data:
#                         curr.next = newnode_1
#                         newnode_1.next= newnode_2

#                     elif current_1.data > current_2.data:
#                         curr.next = newnode_2
#                         newnode_2.next = newnode_1


#                 else:

#                     if current_1.data <= current_2.data:

#                         self.head = newnode_1
#                         newnode_1.next = newnode_2

#                     elif current_1.data > current_2.data:
#                         self.head = newnode_2
#                         newnode_2.next = newnode_1

#                 current_1 = current_1.next
#                 current_2 = current_2.next

#         newnode_1= Node(current_1.data)
#         newnode_2 = Node(current_2.data)

#         if self.head:
#             curr = self.head
#             while curr.next:
#                 curr = curr.next

#             if current_1.data <= current_2.data:
#                 curr.next = newnode_1
#                 newnode_1.next = newnode_2

#                 while current_2.next:
#                     curr = curr.next
#                     current_2 = current_2.next
#                     newnode = Node(current_2.data)
#                     curr.next = newnode


#             else:

#                 curr.next = newnode_2
#                 newnode_2.next = newnode_1

#                 while current_2.next:
#                     curr = curr.next
#                     current_2 = current_2.next
#                     newnode = Node(current_2.data)
#                     curr.next = newnode


# # Singly Linked List with insertion and print methods
# LL1 = LinkedList()
# LL1.insert(1)
# LL1.insert(2)
# LL1.insert(4)
# LL1.printLL()

# LL2 = LinkedList()
# LL2.insert(1)
# LL2.insert(3)
# LL2.insert(4)
# LL2.insert(4)
# LL2.insert(6)
# LL2.printLL()

# LL3 = LinkedList()
# LL3.merged_list(LL1,LL2)
# LL3.printLL()




    
                
