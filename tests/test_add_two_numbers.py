import pytest
from leetcode.add_two_numbers import Solution, ListNode
        
class TestSolution:
    @pytest.mark.parametrize("l1_values, l2_values, expected_result", [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9], [1], [0, 0, 0, 0, 1]),
    ])

    def test_addTwoNumbers(self, l1_values, l2_values, expected_result):
        def create_linked_list(values):
            dummy = ListNode()
            current = dummy
            for val in values:
                current.next = ListNode(val)
                current = current.next
            return dummy.next

        solution = Solution()
        l1 = create_linked_list(l1_values)
        l2 = create_linked_list(l2_values)
        result = solution.addTwoNumbers(l1, l2)
        
        # Compare the linked list values with expected_result
        actual_values = []
        while result:
            actual_values.append(result.val)
            result = result.next
        
        assert actual_values == expected_result
