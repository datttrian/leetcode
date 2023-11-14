from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum == target:
                        result.append(
                            [nums[i], nums[j], nums[left], nums[right]],
                        )

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1

        return result
