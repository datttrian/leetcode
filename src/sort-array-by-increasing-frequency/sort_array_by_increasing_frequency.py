from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:

        # Count the frequency of the numbers in 'nums'
        nums_count: Counter[int] = Counter(nums)

        # Group the numbers by their frequency
        group_count: defaultdict[int, list[int]] = defaultdict(list)
        for num, count in nums_count.items():
            group_count[count].append(num)

        # Sort each group of numbers in descending order
        for num_list in group_count.values():
            num_list.sort(reverse=True)

        # Loop through the groups of sorted frequency in ascending order
        result: list[int] = []
        for count, num_list in sorted(group_count.items()):

            # Loop through all numbers in the group
            for num in num_list:

                # Append the number count times to the result list
                for _ in range(count):
                    result.append(num)

        # Return the final sorted list
        return result
