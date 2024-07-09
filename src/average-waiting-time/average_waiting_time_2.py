class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current, total = 0, 0
        waiting_times = [(current := max(current, arrival) +  # noqa: F841, W504
                          time) - arrival for arrival, time in customers]
        total = sum(waiting_times)
        return total / len(customers)
