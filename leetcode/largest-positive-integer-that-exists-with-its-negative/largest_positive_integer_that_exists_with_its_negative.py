import heapq


class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        max_heap: list[int] = []

        for num in nums:
            heapq.heappush(max_heap, -num)

        while max_heap:
            num = -heapq.heappop(max_heap)
            if num in max_heap:
                return num
        return -1
