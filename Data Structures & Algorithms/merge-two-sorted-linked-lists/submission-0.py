# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy

class Solution:

    @staticmethod
    def append_in_op(op, next_node):
        if not op:
            op = ListNode(next_node.val)
            return op
        else:
            op.next = ListNode(next_node.val)
        return op.next
        


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        op = head = None
        while(list1 or list2):
            if not list2 or (list1 and list1.val < list2.val):
                op = Solution.append_in_op(op, list1)
                list1 = list1.next
            else:
                op = Solution.append_in_op(op, list2)
                list2 = list2.next
            
            if head is None:
                head = op
        return head

        
                

        