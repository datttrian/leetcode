class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if nums[0] == target:
            return 0

        n = len(nums)
        bound = 1
        while bound < n and nums[bound] < target:
            bound *= 2

        left = bound // 2
        right = min(bound, n - 1)

        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        return binary_search(left, right)
