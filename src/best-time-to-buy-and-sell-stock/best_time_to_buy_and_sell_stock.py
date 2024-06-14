class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


solution = Solution()
print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
