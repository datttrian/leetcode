from typing import List, Optional

import pytest
from merge_k_sorted_lists import ListNode, Solution


@pytest.mark.parametrize(
    ('lists', 'expected'),
    [
        (
            [
                ListNode(1, ListNode(4, ListNode(5))),
                ListNode(1, ListNode(3, ListNode(4))),
                ListNode(2, ListNode(6)),
            ],
            ListNode(
                1,
                ListNode(
                    1,
                    ListNode(
                        2,
                        ListNode(
                            3,
                            ListNode(4, ListNode(4, ListNode(5, ListNode(6)))),
                        ),
                    ),
                ),
            ),
        ),
    ],
)
def test_mergeKLists(
    lists: List[Optional[ListNode]],
    expected: Optional[ListNode],
):
    solution = Solution()
    result = solution.mergeKLists(lists)
    assert compare_linked_lists(result, expected)


def compare_linked_lists(
    list1: Optional[ListNode],
    list2: Optional[ListNode],
) -> bool:
    while list1 and list2:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next
    return list1 is None and list2 is None
