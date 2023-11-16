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
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        """
        Reverse nodes in k-group in a linked list.

        Args:
        - head (Optional[ListNode]): The head of the linked list.
        - k (int): The size of each group to be reversed.

        Returns:
        - Optional[ListNode]: The head of the modified linked list.

        Raises:
        - None

        Complexity:
        - Time: O(N), where N is the number of nodes in the linked list.
        - Space: O(1), as the reversal is done in-place without using
        additional space.
        """
        dummy = jump = ListNode(0)
        dummy.next = start = end = head

        while True:
            count = 0
            # Use end to locate the range of the k-group
            while end and count < k:
                end = end.next
                count += 1

            # Reverse the inner linked list
            if count == k:
                pre, cur = end, start

                # Standard reversing
                for _ in range(k):
                    if cur is not None:
                        cur.next, cur, pre = (
                            pre,
                            cur.next,
                            cur,
                        )

                # Connect two k-groups
                if start is not None:
                    jump.next, jump, start = (
                        pre,
                        start,
                        end,
                    )

            # If the size of the remaining nodes is less than k, return
            # the modified list
            else:
                return dummy.next
