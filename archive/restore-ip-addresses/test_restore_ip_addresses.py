import pytest
from restore_ip_addresses import Solution


@pytest.mark.parametrize(
    ('s', 'expected_result'),
    [
        ('25525511135', ['255.255.11.135', '255.255.111.35']),
        ('0000', ['0.0.0.0']),
        ('1111', ['1.1.1.1']),
        ('010010', ['0.10.0.10', '0.100.1.0']),
        (
            '101023',
            ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3'],
        ),
        # Add more test cases as needed
    ],
)
def test_restoreIpAddresses(s: str, expected_result: list[str]):
    solution = Solution()
    result = solution.restoreIpAddresses(s)
    assert result == expected_result
