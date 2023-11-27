from typing import List, Optional

import pytest
from remove_nth_node_from_end_of_list import ListNode, Solution


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
    ('input_list', 'n', 'expected_list'),
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1, 2], 2, [2]),
        ([1], 1, []),
        ([], 1, []),
    ],
)
def test_removeNthFromEnd(
    input_list: List[int],
    n: int,
    expected_list: List[int],
):
    solution = Solution()
    head = list_to_linked_list(input_list)
    expected_head = list_to_linked_list(expected_list)

    result_head = solution.removeNthFromEnd(head, n)

    assert linked_list_to_list(result_head) == linked_list_to_list(
        expected_head,
    )
