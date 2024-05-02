import heapq


class Solution:
    def findMaxK(self, nums: list[int]) -> int:

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        largest_k = -1
        seen: set[int] = set()

        while max_heap:
            num = -heapq.heappop(max_heap)
            if -num in seen:
                if num > 0:
                    largest_k = max(largest_k, num)
            seen.add(num)

        return largest_k
