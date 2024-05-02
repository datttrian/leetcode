class Solution:
    def findMaxK(self, nums: list[int]) -> int:

        nums.sort()
        left, right = 0, len(nums) - 1
        largest_k = -1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == 0:
                if nums[right] > 0:
                    largest_k = max(largest_k, nums[right])
                left += 1
                right -= 1
            elif current_sum > 0:
                right -= 1
            else:
                left += 1

        return largest_k
