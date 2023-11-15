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
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int,
    ) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy: 'ListNode' = ListNode(0)
        dummy.next = head

        # Initialize two pointers, fast and slow, to the dummy node
        fast: Optional[ListNode] = dummy
        slow: Optional[ListNode] = dummy

        # Move fast pointer n + 1 steps ahead
        for _ in range(n + 1):
            if fast is not None:
                fast = fast.next

        # Move both pointers until the fast pointer reaches the end
        while fast is not None:
            fast = fast.next
            if slow is not None:
                slow = slow.next

        # Remove the nth node from the end
        if slow is not None:
            if slow.next is not None:
                slow.next = slow.next.next

        return dummy.next
