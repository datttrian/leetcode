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

        def binary_search(left: int, right: int):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid

                left, right = (
                    (mid + 1, right) if nums[mid] < target else (left, mid - 1)
                )

            return -1

        return binary_search(left, right)


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], target=9))
print(solution.search([-1, 0, 3, 5, 9, 12], target=2))
