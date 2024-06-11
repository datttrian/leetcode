from typing import Counter


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]

count = Counter(arr1)
print(count[1])
result = []

print(result.extend([arr1[1]] * count[arr2[1]]))  # type: ignore
