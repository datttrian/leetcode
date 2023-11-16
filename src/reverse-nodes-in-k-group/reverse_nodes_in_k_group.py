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
