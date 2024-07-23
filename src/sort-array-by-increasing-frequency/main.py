from collections import Counter

nums = [7, 1, 4, 1, 7, 1, 4, 4, 2, 2, 2, 3, 7, 3, 3, 5, 5, 5, 5, 5, 8, 8, 8, 6, 6, 6, 6, 6, 6, 9, 9, 9, 9]

nums_count = Counter(nums)
print(nums_count)

group_count = {}

for num, count in nums_count.items():
    if count in group_count:
        group_count[count].append(num)
    else:
        group_count[count] = [num]



print(group_count.keys())

for group, count in enumerate(group_count):
    count.sort(reverse=True)

print(group_count)
