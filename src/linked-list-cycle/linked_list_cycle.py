from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(
        self,
        val: int = 0,
        nextNode: Optional["ListNode"] = None,
    ) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = nextNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


def list_to_linked_list(lst: list[int], pos: int) -> Optional[ListNode]:
    head = ListNode(lst[0])
    current = head
    cycle_entry = head

    for index in range(1, len(lst)):
        current.next = ListNode(lst[index])
        current = current.next
        if index == pos:
            cycle_entry = current

    if pos != -1:
        current.next = cycle_entry

    return head


solution = Solution()
print(solution.hasCycle(list_to_linked_list([3, 2, 0, -4], 1)))
print(solution.hasCycle(list_to_linked_list([1, 2], 0)))
print(solution.hasCycle(list_to_linked_list([1], -1)))
