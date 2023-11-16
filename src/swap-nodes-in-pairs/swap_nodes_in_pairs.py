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
    """
    Summary:
    Swaps adjacent nodes in a linked list.

    Description:
    Given a linked list, the `swapPairs` method swaps each pair of adjacent
    nodes. If the number of nodes is odd, the last node remains unchanged.

    Algorithm:
    1. Initialize a dummy node to simplify handling edge cases.
    2. Traverse the linked list in pairs, swapping adjacent nodes.
    3. Update pointers accordingly to maintain the linked list structure.

    Parameters:
    - head (Optional[ListNode]): The head of the linked list.

    Returns:
    - Optional[ListNode]: The head of the linked list after swapping adjacent
    nodes.

    Raises:
    - None

    Complexity:
    - Time: O(N), where N is the number of nodes in the linked list.
    - Space: O(1), as the algorithm uses a constant amount of extra space.
    """

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify edge case handling
        dummy: ListNode = ListNode(0)
        dummy.next = head
        current: ListNode = dummy

        # Traverse the linked list in pairs
        while current.next is not None and current.next.next is not None:
            # Pointers to the current pair of nodes
            first: ListNode = current.next
            second: ListNode = current.next.next

            # Swap the adjacent nodes
            first.next = second.next
            second.next = first
            current.next = second

            # Move the current pointer to the next pair
            current = current.next

            # If there is another pair, move the current pointer again
            if current.next is not None:
                current = current.next

        # Return the head of the modified linked list
        return dummy.next
