from collections import deque


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current = 0
        total = 0
        queue = deque(customers)
        num_customers = len(customers)

        while queue:
            arrival, time = queue.popleft()
            current = max(current, arrival)
            current += time
            waiting_time = current - arrival
            total += waiting_time

        return total / num_customers
