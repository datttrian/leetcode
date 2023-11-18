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
        Add two numbers represented by linked lists and returns the sum as a
        linked list.

        Parameters:
        - l1 (Optional[ListNode]): The head of the first linked list
        representing the first number.
        - l2 (Optional[ListNode]): The head of the second linked list
        representing the second number.

        Returns:
        - Optional[ListNode]: The head of the resulting linked list
        representing the sum of the two numbers.

        Raises:
        - None: No specific exceptions are raised by this function.
        """
        # Initialize a dummy head node to simplify cases requiring a new node
        head: ListNode = ListNode()

        # Start with the current node pointing to the dummy head
        current: ListNode = head

        # Initialize carry to zero
        carry: int = 0

        # Loop until both lists are exhausted, and there is no carry
        while l1 or l2 or carry:
            # Extract values from the lists
            val1: int = l1.val if l1 else 0
            val2: int = l2.val if l2 else 0

            # Calculate the new carry and digit
            carry, val = divmod(val1 + val2 + carry, 10)

            # Append the new digit to the result list
            current.next = ListNode(val)

            # Move to the next node in the result list and the input lists
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the sum list, which is next to the dummy head.
        return head.next
