import pytest
from count_and_say import Solution


@pytest.mark.parametrize(
    ('n', 'expected_output'),
    [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
        # Add more test cases as needed
    ],
)
def test_countAndSay(n: int, expected_output: str):
    solution = Solution()
    result = solution.countAndSay(n)
    assert result == expected_output


# Run the tests
if __name__ == '__main__':
    pytest.main()
