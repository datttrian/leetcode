class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result: list[int] = []
        for i in arr2:
            for j in range(len(arr1)):
                if arr1[j] == i:
                    result.append(arr1[j])
                    arr1[j] = -1
        arr1.sort()
        for num in arr1:
            if num != -1:
                result.append(num)
        return result
