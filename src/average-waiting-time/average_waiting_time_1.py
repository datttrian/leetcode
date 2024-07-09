class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current, total = 0, 0
        for arrival, time in customers:
            current = max(current, arrival) + time
            total += current - arrival
        return total / len(customers)
