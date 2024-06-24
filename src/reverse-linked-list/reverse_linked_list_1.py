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


# Helper function to convert list to linked list
def list_to_linkedlist(head: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in head:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


# Helper function to convert linked list to list
def linkedlist_to_list(node: Optional[ListNode]) -> list[int]:
    result: list[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result


solution = Solution()
print(
    linkedlist_to_list(solution.reverseList(
        list_to_linkedlist(head=[1, 2, 3, 4, 5])))
)
print(linkedlist_to_list(solution.reverseList(
    list_to_linkedlist(head=[1, 2]))))
print(linkedlist_to_list(solution.reverseList(list_to_linkedlist(head=[]))))
