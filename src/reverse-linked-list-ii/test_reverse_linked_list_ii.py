from typing import Optional
import pytest
from reverse_linked_list_ii import Solution, ListNode


# Helper function to convert a list to a linked list
def list_to_linked_list(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for num in lst[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


# Helper function to convert a linked list to a list
def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result: list[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


@pytest.mark.parametrize(
    ('head', 'left', 'right', 'expected_result'),
    [
        # Test case with reversing the entire list
        ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),
        # Test case with reversing a portion in the middle
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        # Test case with reversing a single node
        ([1], 1, 1, [1]),
        # Test case with an empty list
        ([], 1, 1, []),
        # Test case with left and right equal (no change)
        ([1, 2, 3], 2, 2, [1, 2, 3]),
    ],
)
def test_reverseBetween(
    head: list[int],
    left: int,
    right: int,
    expected_result: Optional[ListNode],
):
    solution = Solution()
    input_linked_list = list_to_linked_list(head)

    result_linked_list = solution.reverseBetween(
        input_linked_list,
        left,
        right,
    )

    assert linked_list_to_list(result_linked_list) == expected_result
