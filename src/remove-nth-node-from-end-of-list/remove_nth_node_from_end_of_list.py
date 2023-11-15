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
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers, slow and fast, to the dummy node
        slow: Optional[ListNode] = dummy
        fast: Optional[ListNode] = dummy

        # Move the fast pointer n + 1 steps ahead
        for _ in range(n + 1):
            assert fast is not None
            fast = fast.next
            assert slow is not None
            slow = slow.next

        # Move both pointers until the fast pointer reaches the end
        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next

        # Remove the Nth node from the end
        if slow and slow.next:
            assert slow.next is not None  # assert that slow.next is not None
            slow.next = slow.next.next

        return dummy.next
