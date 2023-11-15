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
        """
        Remove the nth node from the end of a linked list.

        Summary:
        Given the head of a linked list and an integer n, remove the nth node
        from the end of the list and return the modified list.

        Description:
        The function uses a two-pointer approach with fast and slow pointers
        to traverse the linked list. It initializes a dummy node to handle
        edge cases. The fast pointer is moved n + 1 steps ahead to create a
        gap between the fast and slow pointers. Then, both pointers are moved
        simultaneously until the fast pointer reaches the end. The slow
        pointer will be pointing to the node just before the nth node from the
        end. Finally, the nth node from the end is removed, and the modified
        list is returned.

        Algorithm:
        1. Create a dummy node to handle edge cases.
        2. Initialize fast and slow pointers to the dummy node.
        3. Move the fast pointer n + 1 steps ahead.
        4. Move both pointers until the fast pointer reaches the end.
        5. Remove the nth node from the end.
        6. Return the modified list starting from the dummy node's next.

        Parameters:
        - head: Optional[ListNode]
            The head of the linked list.
        - n: int
            The position of the node to be removed from the end of the list.

        Returns:
        - Optional[ListNode]
            The head of the modified linked list.

        Raises:
        - No explicit exceptions are raised.

        Complexity:
        - Time complexity: O(N), where N is the number of nodes in the linked
        list.
        - Space complexity: O(1), as only constant extra space is used.
        """
        dummy: 'ListNode' = ListNode(0)
        dummy.next = head

        fast: Optional[ListNode] = dummy
        slow: Optional[ListNode] = dummy

        for _ in range(n + 1):
            if fast is not None:
                fast = fast.next

        while fast is not None:
            fast = fast.next
            if slow is not None:
                slow = slow.next

        if slow is not None:
            if slow.next is not None:
                slow.next = slow.next.next

        return dummy.next
