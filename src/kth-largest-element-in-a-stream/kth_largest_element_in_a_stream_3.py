from sortedcontainers import SortedList  # type: ignore


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.sorted_list: list[int] = SortedList(nums)

    def add(self, val: int) -> int:
        self.sorted_list.add(val)  # type: ignore
        return self.sorted_list[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
