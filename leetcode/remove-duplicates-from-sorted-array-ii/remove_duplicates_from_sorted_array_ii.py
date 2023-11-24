class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Initialize variables
        count = 1  # Count of the current element
        j = 1  # Position to overwrite duplicate elements

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            # Keep the element if the count is less than or equal to 2
            if count <= 2:
                nums[j] = nums[i]
                j += 1

        return j
