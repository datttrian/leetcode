import pytest
from merge_two_sorted_lists.Solution import Solution, ListNode

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize(
        "list1, list2, expected",
        [
            # Test case with both lists being empty
            ([], [], []),
            
            # Test case with one list being empty and the other non-empty
            ([], [1, 3, 5], [1, 3, 5]),
            ([7, 9, 11], [], [7, 9, 11]),
            
            # Test case with both lists having the same values
            ([2, 4, 6], [2, 4, 6], [2, 2, 4, 4, 6, 6]),
            
            # Test case with mixed values
            ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
            
            # Test case with one list's values entirely smaller than the other's
            ([1, 3, 5], [6, 8, 10], [1, 3, 5, 6, 8, 10]),
            
            # Test case with one list's values entirely larger than the other's
            ([7, 9, 11], [2, 4, 6], [2, 4, 6, 7, 9, 11]),
        ],
    )
    def test_mergeTwoLists(self, solution, list1, list2, expected):
        # Convert input lists to linked lists if necessary
        list1 = self.create_linked_list(list1)
        list2 = self.create_linked_list(list2)
        
        result = solution.mergeTwoLists(list1, list2)
        result_values = self.extract_linked_list_values(result)
        
        assert result_values == expected

    def create_linked_list(self, values):
        # Create a linked list from the given list of values
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return head

    def extract_linked_list_values(self, head):
        # Extract values from a linked list and return as a list
        values = []
        current = head
        
        while current:
            values.append(current.val)
            current = current.next
        
        return values
