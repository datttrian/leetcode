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
        visited_nodes = {}
        current_node = head

        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes[current_node] = True
            current_node = current_node.next

        return False


def list_to_linked_list(lst: list[int], pos: int) -> Optional[ListNode]:
    nodes = [ListNode(val) for val in lst]

    for i in range(1, len(lst)):
        nodes[i - 1].next = nodes[i]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


solution = Solution()
print(solution.hasCycle(list_to_linked_list([3, 2, 0, -4], 1)))
print(solution.hasCycle(list_to_linked_list([1, 2], 0)))
print(solution.hasCycle(list_to_linked_list([1], -1)))
