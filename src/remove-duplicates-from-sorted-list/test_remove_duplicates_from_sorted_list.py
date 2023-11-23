from typing import Optional
import pytest
from remove_duplicates_from_sorted_list import Solution, ListNode


# Helper function to convert a list to a linked list
def list_to_linked_list(lst: list[int]):
    if not lst:
        return None
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Helper function to convert a linked list to a list
def linked_list_to_list(node: Optional[ListNode]):
    result: list[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result


@pytest.mark.parametrize(
    ('input_list', 'expected_result_list'),
    [
        # Test case with duplicates
        # ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        # Test case without duplicates
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        # Test case with all elements being duplicates
        ([1, 1, 1, 1, 1], [1]),
        # Test case with an empty list
        ([], []),
    ],
)
def test_deleteDuplicates(
    input_list: list[int],
    expected_result_list: list[int],
):
    solution = Solution()
    input_linked_list = list_to_linked_list(input_list)
    result_linked_list = solution.deleteDuplicates(input_linked_list)
    assert linked_list_to_list(result_linked_list) == expected_result_list
