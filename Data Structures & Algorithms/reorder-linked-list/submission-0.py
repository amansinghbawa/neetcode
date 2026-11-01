
def rev(mid: Optional[ListNode], op: Optional[ListNode]):
    if mid is None:
        return op

    if mid.next:
        return rev(mid.next, ListNode(mid.val, op))
    else:
        return ListNode(mid.val, op)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast, slow = head, head
        mid = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        reversed_list = rev(mid, None)


        first = head
        second = reversed_list

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
