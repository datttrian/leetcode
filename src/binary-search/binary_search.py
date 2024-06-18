class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], target=9))
print(solution.search([-1, 0, 3, 5, 9, 12], target=2))
