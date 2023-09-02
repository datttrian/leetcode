import pytest

# Import the Solution class and ListNode if not already imported
from swap_nodes_in_pairs.Solution import Solution, ListNode


class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize(
        "input_list, expected_output",
        [
            # Edge case: Empty input
            (None, None),
            ([], []),
            # Edge case: Single node
            ([1], [1]),
            # General case: Multiple pairs
            ([1, 2, 3, 4], [2, 1, 4, 3]),
            ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
        ],
    )
    def test_swapPairs(self, solution, input_list, expected_output):
        # Convert the input list to a ListNode linked list
        def list_to_linked_list(lst):
            if not lst:
                return None
            head = ListNode(lst[0])
            current = head
            for val in lst[1:]:
                current.next = ListNode(val)
                current = current.next
            return head

        # Convert the expected output list to a ListNode linked list
        expected_head = list_to_linked_list(expected_output)

        # Call the swapPairs method
        result_head = solution.swapPairs(list_to_linked_list(input_list))

        # Compare the result with the expected output
        while expected_head and result_head:
            assert expected_head.val == result_head.val
            expected_head = expected_head.next
            result_head = result_head.next

        # Both expected_head and result_head should be None at this point
        assert expected_head is None
        assert result_head is None
