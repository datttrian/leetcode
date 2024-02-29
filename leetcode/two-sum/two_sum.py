class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict: dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement], i]

            num_dict[num] = i

        return []
