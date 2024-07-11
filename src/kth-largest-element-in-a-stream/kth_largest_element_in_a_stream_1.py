import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap: list[int] = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
