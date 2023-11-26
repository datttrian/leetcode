from typing import List, Optional

import pytest
from merge_two_sorted_lists import ListNode, Solution


# Helper function to convert a list to a linked list
def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for num in lst[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


# Helper function to convert a linked list to a list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result: List[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


@pytest.mark.parametrize(
    ('list1', 'list2', 'expected_list'),
    [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([], [], []),
    ],
)
def test_mergeTwoLists(
    list1: List[int],
    list2: List[int],
    expected_list: List[int],
):
    solution = Solution()
    head1 = list_to_linked_list(list1)
    head2 = list_to_linked_list(list2)
    expected_head = list_to_linked_list(expected_list)

    result_head = solution.mergeTwoLists(head1, head2)

    assert linked_list_to_list(result_head) == linked_list_to_list(
        expected_head,
    )
