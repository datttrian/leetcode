from typing import List, Optional

import pytest
from swap_nodes_in_pairs import ListNode, Solution


@pytest.mark.parametrize(
    ('head', 'expected'),
    [
        (None, None),
        (ListNode(1), ListNode(1)),
        (ListNode(1, ListNode(2)), ListNode(2, ListNode(1))),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(2, ListNode(1, ListNode(4, ListNode(3)))),
        ),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5))))),
        ),
    ],
)
def test_swapPairs(head: Optional[ListNode], expected: Optional[ListNode]):
    solution = Solution()
    result = solution.swapPairs(head)
    assert list_node_to_list(result) == list_node_to_list(expected)


def list_node_to_list(node: Optional[ListNode]) -> List[int]:
    result: List[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result
