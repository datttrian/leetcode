import pytest
from remove_element.Solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "input_list, elem, expected_length",
        [
            ([3, 2, 2, 3], 3, 2),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
            ([1, 2, 3, 4], 5, 4),
            ([1, 2, 3, 4], 1, 3),
            ([], 0, 0),
        ],
    )
    def test_removeElement(self, input_list, elem, expected_length):
        solution = Solution()
        actual_length = solution.removeElement(input_list, elem)
        assert actual_length == expected_length

    # Add more test cases as needed
