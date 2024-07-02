from typing import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count_nums1 = Counter(nums1)
        return [num for num in nums2 if count_nums1[num] > 0 and not count_nums1.subtract([num])]
