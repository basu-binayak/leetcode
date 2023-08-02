# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # Approach:
        # Notice that we are told the given node is not a tail node. Therefore, we can delete the next
        # node instead of the current node given, and "pretend" that the node we are given is the next
        # node.
        
        
        # Store the next node in a temporary variable.
        next_node = node.next
        
        # Copy data of the next node to the current node.
        node.val = next_node.val 
        
        # Change the next pointer of the current node to the next pointer of the next node.
        node.next = next_node.next 
        
        
        
        