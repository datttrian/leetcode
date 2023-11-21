from typing import Optional, List
import pytest
from rotate_list import Solution, ListNode


def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result: List[int] = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


@pytest.mark.parametrize(
    ('head', 'k', 'expected'),
    [
        (list_to_linked_list([1, 2, 3, 4, 5]), 2, [4, 5, 1, 2, 3]),
        (list_to_linked_list([0, 1, 2]), 4, [2, 0, 1]),
        (list_to_linked_list([]), 0, []),
        (list_to_linked_list([1, 2, 3]), 0, [1, 2, 3]),
        (list_to_linked_list([1, 2, 3]), 3, [1, 2, 3]),
        (list_to_linked_list([1, 2, 3]), 6, [1, 2, 3]),
        (list_to_linked_list([1]), 99, [1]),
    ],
)
def test_rotateRight(
    head: Optional[ListNode],
    k: int,
    expected: List[int],
) -> None:
    solution = Solution()
    result = solution.rotateRight(head, k)
    assert linked_list_to_list(result) == expected
