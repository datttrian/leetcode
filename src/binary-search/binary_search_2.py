class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            return (
                binary_search(mid + 1, right)
                if nums[mid] < target
                else binary_search(left, mid - 1)
            )

        return binary_search(0, len(nums) - 1)


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], target=9))
print(solution.search([-1, 0, 3, 5, 9, 12], target=2))
