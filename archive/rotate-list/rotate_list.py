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
    def rotateRight(
        self,
        head: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        """
        Rotate the linked list to the right by k places.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.
        - k (int): The number of places to rotate the list.

        Returns:
        - Optional[ListNode]: The head of the rotated linked list.
        """
        if not head or k == 0:
            return head

        # Find the length of the linked list
        current, length = head, 1
        while current.next:
            current = current.next
            length += 1

        # Adjust k to handle cases where k is greater than the length
        k %= length

        if k == 0:
            return head  # No rotation needed

        # Find the new head and tail after rotation
        current = head
        for _ in range(length - k - 1):
            if current and current.next:
                current = current.next

        new_head = current.next
        current.next = None

        if new_head is not None:
            current = new_head

        while current.next:
            current = current.next

        current.next = head

        return new_head
