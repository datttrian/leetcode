from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        nums_count = Counter(nums)
        group_count = defaultdict(list)

        [group_count[count].append(num) for num, count in nums_count.items()]

        for _, count in group_count.items():
            count.sort(reverse=True)

        result = [num for count in sorted(
            group_count) for num in group_count[count] for _ in range(count)]

        return result
