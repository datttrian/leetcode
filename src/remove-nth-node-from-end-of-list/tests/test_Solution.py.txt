import pytest
from submissions.Solution import Solution, ListNode

class TestSolution:
    @pytest.mark.parametrize("input_list, n, expected_output", [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2,
         ListNode(1, ListNode(2, ListNode(3, ListNode(5))))),
        (ListNode(1), 1, None),  # Edge case: Removing the only element
        (ListNode(1, ListNode(2)), 1, ListNode(1)),  # Edge case: Removing the last element
        (ListNode(1, ListNode(2)), 2, ListNode(2)),  # Edge case: Removing the first element
    ])
    def test_removeNthFromEnd(self, input_list, n, expected_output):
        solution = Solution()
        new_head = solution.removeNthFromEnd(input_list, n)
        assert self.list_equal(new_head, expected_output)

    def list_equal(self, list1, list2):
        while list1 and list2:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
        return list1 is None and list2 is None
