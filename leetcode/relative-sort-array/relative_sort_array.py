arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]

result = []

for i in arr2:
    for j in arr1:
        if i == j:
            result.append(j)  # type: ignore
            arr1.remove(j)

print(arr1)
print(result)  # type: ignore
for num in arr1:
    result.append(num)  # type: ignore
print(result)  # type: ignore
