from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int = 0,
        nextNode: "Optional[ListNode]" = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = nextNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next
        while slow and slow.next and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = slow.next if slow else None
        if slow:
            slow.next = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev, curr = curr, next_temp

        first: Optional[ListNode] = head
        second: Optional[ListNode] = prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2
