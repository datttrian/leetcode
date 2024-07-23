from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        nums_count = Counter(nums)
        group_count = defaultdict(list)
        result = []

        [group_count[count].append(num) for num, count in nums_count.items()]

        for _, count in group_count.items():
            count.sort(reverse=True)

        for count, nums in sorted(group_count.items()):
            for num in nums:
                for _ in range(count):
                    result.append(num)

        return result
