import pytest
from typing import List
from letter_combinations_of_a_phone_number.Solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "digits, expected",
        [
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ("", []),  # Test case for an empty input, should return an empty list
            ("2", ["a", "b", "c"]),
            ("7", ["p", "q", "r", "s"]),
            ("9", ["w", "x", "y", "z"]),
            (
                "234",
                [
                    "adg",
                    "adh",
                    "adi",
                    "aeg",
                    "aeh",
                    "aei",
                    "afg",
                    "afh",
                    "afi",
                    "bdg",
                    "bdh",
                    "bdi",
                    "beg",
                    "beh",
                    "bei",
                    "bfg",
                    "bfh",
                    "bfi",
                    "cdg",
                    "cdh",
                    "cdi",
                    "ceg",
                    "ceh",
                    "cei",
                    "cfg",
                    "cfh",
                    "cfi",
                ],
            ),  # Test case for multiple digits
            ("0", []),  # Test case for a digit '0', should return an empty list
            ("1", []),  # Test case for a digit '1', should return an empty list
        ],
    )
    def test_letterCombinations(self, digits: str, expected: List[str]):
        solution = Solution()
        assert solution.letterCombinations(digits) == expected
