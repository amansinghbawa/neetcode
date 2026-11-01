class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def get_next(head, output):
            if head.next:
                next_val = head.val
                print("in", next_val)
                return get_next(head.next, ListNode(next_val, output))
            else:
                print("out", head.val)
                return ListNode(head.val, output)
        
        if head is None:
            return None
        op =  get_next(head, None)
        return op
        # return output

