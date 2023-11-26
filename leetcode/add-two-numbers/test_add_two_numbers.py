from typing import List, Optional

import pytest
from add_two_numbers import ListNode, Solution


# Helper function to convert a list to a ListNode chain
def to_listnode(numbers: List[int]) -> Optional[ListNode]:
    dummy_root = ListNode(0)
    ptr = dummy_root
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    return dummy_root.next


# Helper function to convert a ListNode chain to a list
def to_list(head: Optional[ListNode]) -> List[int]:
    numbers: List[int] = []
    while head:
        numbers.append(head.val)
        head = head.next
    return numbers


@pytest.mark.parametrize(
    ('l1', 'l2', 'expected'),
    [
        ([], [], []),  # Both lists are empty
        ([], [0], [0]),  # First list is empty
        ([0], [], [0]),  # Second list is empty
        ([0], [0], [0]),  # Both lists have one node with zero
        (
            [2, 4, 3],
            [5, 6, 4],
            [7, 0, 8],
        ),  # Normal case with no carry over at the last digit
        (
            [9, 9, 9],
            [1],
            [0, 0, 0, 1],
        ),  # Normal case with carry over at the last digit
        ([1], [9, 9, 9], [0, 0, 0, 1]),  # l2 is longer than l1
        (
            [9, 9],
            [1],
            [0, 0, 1],
        ),  # Sum results in a new most significant digit
    ],
)
def test_add_two_numbers(l1: List[int], l2: List[int], expected: List[int]):
    listnode1 = to_listnode(l1)
    listnode2 = to_listnode(l2)
    solution = Solution()
    result = solution.addTwoNumbers(listnode1, listnode2)
    assert to_list(result) == expected


def test_add_two_numbers_large_numbers():
    l1 = [int(i) for i in str(10**100)]
    l2 = [int(i) for i in str(10**100)]
    expected = [int(i) for i in str(2 * 10**100)]
    listnode1 = to_listnode(l1)
    listnode2 = to_listnode(l2)
    solution = Solution()
    result = solution.addTwoNumbers(listnode1, listnode2)
    assert to_list(result) == expected


def test_add_two_numbers_single_digit_carry():
    l1 = [5]
    l2 = [5]
    expected = [0, 1]
    listnode1 = to_listnode(l1)
    listnode2 = to_listnode(l2)
    solution = Solution()
    result = solution.addTwoNumbers(listnode1, listnode2)
    assert to_list(result) == expected
