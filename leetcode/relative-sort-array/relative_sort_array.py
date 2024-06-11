arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]

result = []

for i in arr2:
    for j in range(len(arr1)):
        if i == arr1[j]:
            result.append(arr1[j])  # type: ignore
            arr1[j] = 0

print(arr1)
print(result)  # type: ignore
arr1.sort()
for num in arr1:
    if num != 0:
        result.append(num)  # type: ignore
print(result)  # type: ignore
