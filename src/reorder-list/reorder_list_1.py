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

        # Base case: If the list is empty or has only one node, no need to reorder
        if not head or not head.next:
            return

        # Use two pointers to find the middle of the list
        slow, fast = head, head.next
        while slow.next and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list starting from slow.next
        prev, curr = None, slow
        while curr:

            # Store the next node
            next_temp = curr.next

            # Reverse the link
            curr.next = prev

            # Move prev to the current node and the current node to the next node
            prev, curr = curr, next_temp

        # Merge the two halves together
        first, second = head, prev
        while first and second and second.next:

            # Store the next nodes
            temp1, temp2 = first.next, second.next

            # Reorder nodes
            first.next, second.next = second, temp1

            # Move to the next nodes
            first, second = temp1, temp2
