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
        l1: ListNode | None,
        l2: ListNode | None,
    ) -> ListNode | None:
        head: ListNode = ListNode(
            0,
        )  # dummy head node to simplify the addition

        current: ListNode = (
            head  # pointer to the current node in the result list
        )
        carry: int = 0  # initialize carry to zero

        # Continue looping until both lists are exhausted and there is no carry
        while l1 or l2 or carry:
            val1: int = (
                l1.val if l1 else 0
            )  # get the value of the current node of l1, 0 if l1 is exhausted

            val2: int = (
                l2.val if l2 else 0
            )  # get the value of the current node of l2, 0 if l2 is exhausted
            carry, out = divmod(
                val1 + val2 + carry,
                10,
            )  # calculate the sum and the new carry

            current.next = ListNode(
                out,
            )  # create a new node with the sum value
            current = current.next  # move to the next node

            l1 = (
                l1.next if l1 else None
            )  # advance to the next node in l1 if available
            l2 = (
                l2.next if l2 else None
            )  # advance to the next node in l2 if available

        return head.next  # return the sum list, excluding the dummy head node
