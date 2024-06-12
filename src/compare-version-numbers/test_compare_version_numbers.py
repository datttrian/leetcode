import pytest
from compare_version_numbers import Solution


@pytest.mark.parametrize(
    ("version1", "version2", "expected"),
    [
        ("1.0", "1.0", 0),
        ("0.1", "1.1", -1),
        ("1.2", "1.1", 1),
        ("1.0.1", "1", 1),
        ("7.5.2.4", "7.5.3", -1),
        ("1.01", "1.001", 0),
        ("1.0", "1.0.0", 0),
        ("1.0.0", "1.0", 0),
        ("1.0.0.0", "1.0", 0),
        ("1.0", "1.0.0.0", 0),
    ],
)
def test_compareVersion(version1: str, version2: str, expected: int) -> None:
    solution = Solution()
    assert solution.compareVersion(version1, version2) == expected
