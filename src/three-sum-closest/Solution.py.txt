from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        result = float("inf")
        stored_sum = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                k = nums[i] + nums[left] + nums[right]

                if k > target:
                    right -= 1
                elif k < target:
                    left += 1
                else:
                    return k

                if abs(target - k) < result:
                    result = abs(target - k)
                    stored_sum = k

        return stored_sum
