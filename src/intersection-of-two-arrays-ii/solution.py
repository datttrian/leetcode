from typing import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count_nums1 = Counter(nums1)
        intersection: list[int] = []

        for num in nums2:
            if count_nums1[num]:
                intersection.append(num)
                count_nums1[num] -= 1

        return intersection
