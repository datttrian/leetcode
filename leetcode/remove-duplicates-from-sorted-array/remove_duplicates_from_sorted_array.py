class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        left_pointer = 1

        for right_pointer in range(1, len(nums)):
            if nums[right_pointer] != nums[right_pointer - 1]:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
        return left_pointer
