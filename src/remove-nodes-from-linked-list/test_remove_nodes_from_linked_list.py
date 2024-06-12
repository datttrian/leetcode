from typing import Optional

import pytest
from remove_nodes_from_linked_list import ListNode, Solution


def list_to_linkedlist(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head: Optional[ListNode]) -> list[int]:
    lst: list[int] = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst


@pytest.mark.parametrize(
    "input_list, expected_list",
    [
        (
            [1, 2, 3, 4, 5],
            [5],
        ),
        ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
        ([3, 2, 5, 1, 4], [5, 4]),
        ([1], [1]),
        ([], []),
    ],
)
def test_removeNodes(input_list: list[int], expected_list: list[int]) -> None:
    solution = Solution()
    head = list_to_linkedlist(input_list)
    new_head = solution.removeNodes(head)
    output_list = linkedlist_to_list(new_head)
    assert output_list == expected_list