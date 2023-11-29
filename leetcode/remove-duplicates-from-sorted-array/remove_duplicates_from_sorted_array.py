class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Initialize the left pointer to 1
        left_pointer = 1

        # Iterate through the array starting from the second element
        for right_pointer in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[right_pointer] != nums[right_pointer - 1]:
                # Update the value at the left pointer position
                nums[left_pointer] = nums[right_pointer]
                # Move the left pointer forward
                left_pointer += 1

        # Left pointer represents the length of the array without duplicates
        return left_pointer
