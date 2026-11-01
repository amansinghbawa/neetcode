# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        first = head
        second = head.next


        while (second):
            if not second.next or not second.next.next:
                return False
            first = first.next
            second = second.next.next

            if first is second:
                return True
        return False
            

        