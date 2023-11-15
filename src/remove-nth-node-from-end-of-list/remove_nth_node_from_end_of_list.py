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
        Summary:
        Removes the Nth node from the end of a linked list.

        Description:
        Given the head of a linked list and an integer n, the function removes
        the Nth node from the end of the list and returns the updated head.
        The algorithm uses two pointers, a slow and a fast pointer, to
        traverse the list efficiently.

        Algorithm:
        1. Create a dummy node to handle edge cases.
        2. Initialize two pointers, slow and fast, to the dummy node.
        3. Move the fast pointer n + 1 steps ahead to create a gap between
        slow and fast.
        4. Move both pointers until the fast pointer reaches the end of the
        list.
        5. Update pointers to remove the Nth node from the end.
        6. Return the updated head of the linked list.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.
        - n (int): The position of the node to be removed from the end.

        Returns:
        - Optional[ListNode]: The head of the linked list after removal.

        Raises:
        - No explicit exceptions are raised.

        Complexity:
        - Time: O(n), where n is the number of nodes in the linked list.
        - Space: O(1), as the algorithm uses a constant amount of extra space.
        """
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
            slow.next = (
                slow.next.next
            )  # Remove the Nth node by updating pointers

        return dummy.next  # Return the updated head of the linked list
