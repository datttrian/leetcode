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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node


# Helper function to create a linked list from a list
def create_linked_list(head: list[int]) -> Optional[ListNode]:
    if not head:
        return None
    head_node = ListNode(head[0])
    current_node = head_node
    for value in head[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next
    return head_node


# Helper function to convert a linked list to a list
def linked_list_to_list(headNode: Optional[ListNode]) -> list[int]:
    result: list[int] = []
    current_node = headNode
    while current_node:
        result.append(current_node.val)
        current_node = current_node.next
    return result


solution = Solution()
print(
    linked_list_to_list(solution.reverseList(create_linked_list(head=[1, 2, 3, 4, 5])))
)
print(linked_list_to_list(solution.reverseList(create_linked_list(head=[1, 2]))))
print(linked_list_to_list(solution.reverseList(create_linked_list(head=[]))))
