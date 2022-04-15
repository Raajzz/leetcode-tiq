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
    # node is the node to be deleted
    # Look, when you have 'a variable' and if you did <some_var> = <something_else> the variable would be 
    # changed, but the overall structure of the LinkedList won't be changed.
    # But if you do node.next, then that literally means the overall structure will be changed.
    
    if(node is not None):
      node.val = node.next.val
      node.next = node.next.next