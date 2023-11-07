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
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists and return the sum.

        Each node in the input lists contains a single digit, and the digits
        are stored in reverse order, with the head node representing the least
        significant digit. The function computes the sum digit by digit, taking
        care to manage the carry from the sum that exceeds 9.

        Args:
            l1 (Optional[ListNode]): The head node of the first linked list.
            l2 (Optional[ListNode]): The head node of the second linked list.

        Returns:
            Optional[ListNode]: The head node of the linked list that
            represents the sum.

        The method uses a dummy head node to simplify the handling of the edge
        case where a new digit is added (e.g., when the sum of the highest
        digits plus a carry results in a new digit). The function iterates
        through both lists until all digits have been processed. In each
        iteration, it adds the digits along with the carry from the previous
        iteration.

        Complexity:
        - Time: O(max(n, m)), where n and m are number of nodes in the first
        and second linked list .
        - Space: O(max(n, m)), since we may need to store the sum in a new
        linked list, the space required for the new list is at most the length
        of the longer input list plus one additional node for a potential
        carry-over.
        """
        # Initialize a dummy head node to simplify addition when a new node is
        # required.
        head: ListNode = ListNode(0)
        # Start with the current node pointing to the dummy head.
        current: ListNode = head
        # Initialize carry to zero.
        carry: int = 0

        # Loop until both lists are exhausted and there is no carry.
        while l1 or l2 or carry:
            # Extract values from the lists, defaulting to 0 if the list is
            # exhausted.
            val1: int = l1.val if l1 else 0
            val2: int = l2.val if l2 else 0

            # Sum the values with the carry, calculate the new carry and the
            # digit to store.
            carry, out = divmod(val1 + val2 + carry, 10)

            # Append the calculated digit to the result list.
            current.next = ListNode(out)

            # Move to the next node in the result list.
            current = current.next

            # Move to the next nodes in the input lists, if available.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the sum list, which is next to the dummy head.
        return head.next
