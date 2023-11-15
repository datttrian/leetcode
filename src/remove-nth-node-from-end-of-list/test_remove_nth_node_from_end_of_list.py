from typing import Optional
import pytest
from remove_nth_node_from_end_of_list import Solution, ListNode


@pytest.mark.parametrize(
    ('input_list', 'n', 'expected_output'),
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            2,
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        ),
        (ListNode(1), 1, None),  # Edge case: Removing the only element
        (
            ListNode(1, ListNode(2)),
            1,
            ListNode(1),
        ),  # Edge case: Removing the last element
        (
            ListNode(1, ListNode(2)),
            2,
            ListNode(2),
        ),  # Edge case: Removing the first element
    ],
)
def test_removeNthFromEnd(
    input_list: Optional[ListNode],
    n: int,
    expected_output: Optional[ListNode],
):
    solution = Solution()
    new_head = solution.removeNthFromEnd(input_list, n)
    assert list_equal(new_head, expected_output)


def list_equal(list1: Optional[ListNode], list2: Optional[ListNode]):
    while list1 and list2:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next
        return list1 is None and list2 is None
