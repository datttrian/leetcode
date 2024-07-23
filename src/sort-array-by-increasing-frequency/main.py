from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        nums_count = Counter(nums)
        group_count = defaultdict(list)

        for num, count in nums_count.items():
            group_count[count].append(num)

        for num_list in group_count.values():
            num_list.sort(reverse=True)

        result = [
            num
            for count in sorted(group_count)
            for num in group_count[count]
            for _ in range(count)
        ]

        return result
