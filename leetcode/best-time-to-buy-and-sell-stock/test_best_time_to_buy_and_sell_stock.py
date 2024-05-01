import pytest
from best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize(
    ["prices", "expected_max_profit"],
    [
        [[3, 0, 6, 1, 5], 6],
        [[1, 2, 3, 4, 5], 4],
        [[0, 0, 0, 0, 0], 0],
        [[4, 4, 4, 4, 5], 1],
        [[0, 1, 3, 5, 6], 6],
    ],
)
def test_maxProfit(prices: list[int], expected_max_profit: int) -> None:
    solution = Solution()
    assert solution.maxProfit(prices) == expected_max_profit
