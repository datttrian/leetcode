class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current, total = 0, 0
        wait = [
            (current := max(current, arrival) + time) - arrival  # noqa: F841, W504
            for arrival, time in customers
        ]
        total = sum(wait)
        return total / len(customers)
