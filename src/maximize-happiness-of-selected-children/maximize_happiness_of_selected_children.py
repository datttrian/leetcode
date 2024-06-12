import heapq


class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        neg_happiness = [-h for h in happiness]
        heapq.heapify(neg_happiness)

        total_sum = 0
        turns = 0

        for _ in range(k):
            total_sum += max(-heapq.heappop(neg_happiness) - turns, 0)
            turns += 1

        return total_sum
