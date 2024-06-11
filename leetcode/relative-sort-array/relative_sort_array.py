class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result = [num for num in arr2 for _ in range(arr1.count(num))]
        arr1 = [num for num in arr1 if num not in arr2]
        return result + sorted(arr1)
