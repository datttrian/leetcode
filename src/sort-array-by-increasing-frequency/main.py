from collections import Counter

nums = [7, 1, 4, 1, 7, 1, 4, 4, 2, 2, 2, 3, 7, 3, 3, 5, 5, 5, 5, 5, 8, 8, 8, 6, 6, 6, 6, 6, 6, 9, 9, 9, 9]

nums_count = Counter(nums)
print(nums_count)

group_count = {}

for num, freq in freq_dict.items():
    if freq in freq_group:
        freq_group[freq].append(n)
