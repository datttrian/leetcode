from typing import Optional  # Not necessary if you're using Python 3.10+


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next_node: 'Optional[ListNode]' = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next_node


class Solution:
    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None,
    ) -> ListNode | None:
        head: ListNode = ListNode(0)
        current: ListNode = head
        carry: int = 0

        while l1 or l2 or carry:
            val1: int = l1.val if l1 else 0
            val2: int = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)

            current.next = ListNode(out)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
