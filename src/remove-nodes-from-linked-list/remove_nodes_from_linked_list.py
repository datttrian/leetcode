from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next_node: "Optional[ListNode]" = None,  # pylint: disable=invalid-name
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next_node


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.removeNodes(head.next)
        if new_head and head.val < new_head.val:
            return new_head
        head.next = new_head
        return head
