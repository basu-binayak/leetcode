# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The provided code defines a Python class Solution with a method reverseList. The method
        # takes a singly-linked list represented by the head node and returns the reversed version of
        # the linked list.
        
        # The idea is to use three pointers curr, prev, and next to keep track of nodes to update
        # reverse links.
        
        # Follow the steps below to solve the problem:

        # Initialize three pointers prev as NULL, curr as head, and next as NULL.
        prev , curr, next = None, head , None 
        
        # Iterate through the linked list. In a loop, do the following:
        while curr!=None:
            
            # Before changing the next of curr, store the next node
            # next = curr -> next
            next = curr.next 
            
            # Now update the next pointer of curr to the prev
            # curr -> next = prev
            curr.next = prev
            
            # Update prev as curr and curr as next 
            prev = curr
            curr = next
        
        return prev

# An alternate recursive solution 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_recursive(node, prev=None):
            if not node:
                return prev

            next_node = node.next
            node.next = prev
            return reverse_recursive(next_node, node)

        return reverse_recursive(head)

            
        
        
