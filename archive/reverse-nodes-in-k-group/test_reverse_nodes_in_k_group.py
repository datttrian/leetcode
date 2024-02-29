from typing import List, Optional

import pytest
from reverse_nodes_in_k_group import ListNode, Solution


@pytest.mark.parametrize(
    ('head', 'k', 'expected'),
    [
        (None, 2, None),
        (ListNode(1), 2, ListNode(1)),
        (ListNode(1, ListNode(2)), 2, ListNode(2, ListNode(1))),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            2,
            ListNode(2, ListNode(1, ListNode(4, ListNode(3)))),
        ),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            3,
            ListNode(3, ListNode(2, ListNode(1, ListNode(4, ListNode(5))))),
        ),
    ],
)
def test_reverseKGroup(
    head: Optional[ListNode],
    k: int,
    expected: Optional[ListNode],
):
    solution = Solution()
    result = solution.reverseKGroup(head, k)
    assert list_node_to_list(result) == list_node_to_list(expected)


def list_node_to_list(node: Optional[ListNode]) -> List[int]:
    result: List[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result
