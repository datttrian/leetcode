from typing import Counter


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
intersection = []

count_nums1 = Counter(nums1)

for num in nums2:
    if count_nums1[num]:
        intersection.append(num)  # type:ignore
        count_nums1[num] -= 1  # type:ignore

print(count_nums1)
print(intersection)  # type:ignore

