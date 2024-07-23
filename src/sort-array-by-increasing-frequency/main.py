from collections import Counter

nums = [7, 1, 4, 1, 7, 1, 4, 4, 2, 2, 2, 3, 7, 3, 3, 5, 5, 5, 5, 5, 8, 8, 8, 6, 6, 6, 6, 6, 6, 9, 9, 9, 9]

nums_count = Counter(nums)
print(nums_count)

group_count = {}

nums_count[1]
for num, count in nums_count.items():
    group_count[count].append(num) if count in group_count else group_count = [num]
