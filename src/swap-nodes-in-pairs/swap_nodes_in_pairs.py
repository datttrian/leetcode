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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy: ListNode = ListNode(0)
        dummy.next = head
        current: ListNode = dummy

        while current.next is not None and current.next.next is not None:
            first: ListNode = current.next
            second: ListNode = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current.next = current.next.next

        return dummy.next
