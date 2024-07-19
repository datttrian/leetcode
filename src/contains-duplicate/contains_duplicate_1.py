class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        length = len(nums)
        for current_index in range(length):
            for comparison_index in range(current_index + 1, length):
                if nums[current_index] == nums[comparison_index]:
                    return True
        return False
