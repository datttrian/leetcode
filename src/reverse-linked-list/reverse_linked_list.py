from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


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
def create_linked_list(arr):
    if not arr:
        return None
    head_node = ListNode(arr[0])
    current_node = head_node
    for value in arr[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next
    return head_node


# Helper function to convert a linked list to a list
def linked_list_to_list(head_node):
    result = []
    current_node = head_node
    while current_node:
        result.append(current_node.val)
        current_node = current_node.next
    return result


# solution = Solution()
input_list = [1, 2, 3, 4, 5]
# head = create_linked_list(input_list)
# reversed_head = solution.reverseList(head)
# output_list = linked_list_to_list(reversed_head)
# print(output_list)  # Output: [5, 4, 3, 2, 1]

print(input_list | create_linked_list)
