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
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # Move to the node just before the reversal starts
        for _ in range(left - 1):
            if pre.next:
                pre = pre.next

        # Reverse the nodes from left to right
        current = pre.next
        prev = None
        for _ in range(right - left + 1):
            if current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

        # Connect the reversed portion back to the original list
        if pre.next:
            pre.next.next = current
        pre.next = prev

        return dummy.next
