import pytest
from merge_k_sorted_lists.Solution import Solution, ListNode


class TestSolution:
    @pytest.mark.parametrize(
        "lists, expected",
        [
            # Basic test case with small lists
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
                                3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))
                            ),
                        ),
                    ),
                ),
            ),
            # Edge case: Empty list
            ([], None),
            # Edge case: List with one empty sublist
            ([None], None),
            # Edge case: Single-element lists
            (
                [ListNode(1), ListNode(2), ListNode(3)],
                ListNode(1, ListNode(2, ListNode(3))),
            ),
            # Edge case: Lists with single element, one of them is empty
            ([None, ListNode(1), None], ListNode(1)),
            # Edge case: Lists with single element, all of them are empty
            ([None, None, None], None),
            # Edge case: Lists with only one element in the middle
            (
                [ListNode(1, ListNode(2)), ListNode(2), ListNode(1, ListNode(3))],
                ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3))))),
            ),
        ],
    )
    def test_mergeKLists(self, lists, expected):
        solution = Solution()
        result = solution.mergeKLists(lists)
        assert self.compare_linked_lists(result, expected)

    def compare_linked_lists(self, list1, list2):
        while list1 and list2:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
        return list1 is None and list2 is None
