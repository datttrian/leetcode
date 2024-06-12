class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_sorted = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums_sorted[left][1] + nums_sorted[right][1]
            if current_sum == target:
                return [nums_sorted[left][0], nums_sorted[right][0]]

            if current_sum < target:
                left += 1
            else:
                right -= 1
        return []


solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
print(solution.twoSum(nums=[3, 2, 4], target=6))
print(solution.twoSum(nums=[3, 3], target=6))
