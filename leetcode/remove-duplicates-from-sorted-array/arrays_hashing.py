class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Convert the list to a set to remove duplicates
        unique_nums = set(nums)

        # Update the original list with the unique elements
        nums[: len(unique_nums)] = sorted(unique_nums)

        # Return the length of the updated array
        return len(unique_nums)
