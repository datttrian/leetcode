from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(
        self,
        val: int = 0,
        nextNode: "Optional[ListNode]" = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = nextNode


# Helper function to convert list to linked list
def list_to_linked_list(lst: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


# Helper function to convert linked list to list
def linked_list_to_list(node: Optional[ListNode]) -> list[int]:
    result: list[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow, fast = head, head.next

        while slow.next and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while first.next and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
