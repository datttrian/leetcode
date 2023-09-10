import pytest
from reverse_nodes_in_k_group.Solution import Solution, ListNode


# Define the test cases and expected results as tuples
test_cases = [
    (None, 2, None),  # Empty list, nothing to reverse
    (ListNode(1), 1, ListNode(1)),  # Single node, k=1, no change
    (
        ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
        2,
        ListNode(2, ListNode(1, ListNode(4, ListNode(3)))),
    ),  # Example case
    (
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        3,
        ListNode(3, ListNode(2, ListNode(1, ListNode(4, ListNode(5))))),
    ),  # Example case
]


@pytest.mark.parametrize("head, k, expected", test_cases)
class TestSolution:
    def test_reverseKGroup(self, head, k, expected):
        solution = Solution()
        result = solution.reverseKGroup(head, k)
        assert self.list_to_array(result) == self.list_to_array(expected)

    def list_to_array(self, head):
        result = []
        while head:
            result.append(head.value)
            head = head.next
        return result
