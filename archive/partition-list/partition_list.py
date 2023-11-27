from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next_node: 'Optional[ListNode]' = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next_node


class Solution:
    def partition(
        self,
        head: Optional[ListNode],
        x: int,
    ) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less_current = less_head
        greater_current = greater_head

        while head:
            if head.val < x:
                less_current.next = head
                less_current = less_current.next
            else:
                greater_current.next = head
                greater_current = greater_current.next
            head = head.next

        # Concatenate the two linked lists
        less_current.next = greater_head.next
        greater_current.next = None

        return less_head.next
