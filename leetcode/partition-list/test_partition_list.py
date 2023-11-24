from typing import Optional
import pytest
from partition_list import Solution, ListNode


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
    ('input_list', 'x', 'expected_result_list'),
    [
        # Test case with nodes less than x and nodes greater than or equal to x
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        # Test case with all nodes less than x
        ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
        # Test case with all nodes greater than or equal to x
        ([5, 4, 3, 2, 1], 0, [5, 4, 3, 2, 1]),
        # Test case with an empty list
        ([], 1, []),
        # Test case with a single-node list
        ([1], 0, [1]),
    ],
)
def test_partition(
    input_list: list[int],
    x: int,
    expected_result_list: list[int],
):
    solution = Solution()
    input_linked_list = list_to_linked_list(input_list)
    result_linked_list = solution.partition(input_linked_list, x)
    assert linked_list_to_list(result_linked_list) == expected_result_list
