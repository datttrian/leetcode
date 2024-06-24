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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to form the new sorted list
        dummy = ListNode()
        current = dummy

        # Traverse both lists and compare the current nodes of both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If either list is not empty, append the remaining elements
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return the merged list, which starts at dummy.next
        return dummy.next


# Helper function to convert list to linked list
def list_to_linkedlist(lst: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in lst:
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


# Example usage
solution = Solution()
print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist(
    [1, 2, 4]), list_to_linkedlist([1, 3, 4]))))
print(linkedlist_to_list(solution.mergeTwoLists(
    list_to_linkedlist([]), list_to_linkedlist([]))))
print(linkedlist_to_list(solution.mergeTwoLists(
    list_to_linkedlist([]), list_to_linkedlist([0]))))
