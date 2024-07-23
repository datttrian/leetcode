from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        # Count the frequency of each number in the input list
        nums_count: Counter[int] = Counter(nums)

        # Create a defaultdict to group numbers by their frequency
        group_count: defaultdict[int, list[int]] = defaultdict(list)

        # Populate the defaultdict with numbers grouped by their frequency
        for num, count in nums_count.items():
            group_count[count].append(num)

        # Sort each group of numbers in descending order
        for num_list in group_count.values():
            num_list.sort(reverse=True)

        # Loop through the groups of sorted counts
        result: list[int] = []
        for count, num_list in sorted(group_count.items()):

            # For each number in the group
            for num in num_list:

                # Append the number count times to the result list
                for _ in range(count):
                    result.append(num)

        return result
