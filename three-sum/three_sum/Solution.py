class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sorted Array
        if len(nums) < 3:  # Base case 1
            return []
        if nums[0] > 0:  # Base case 2
            return []

        answer = []
        for i in range(len(nums)):  # Traversing the array to fix the number.
            if (
                nums[i] > 0
            ):  # If the fixed number is positive, stop because we can't make it zero by searching after it.
                break
            if (
                i > 0 and nums[i] == nums[i - 1]
            ):  # If the number is repeated, ignore the lower loop and continue.
                continue

            low, high = (
                i + 1,
                len(nums) - 1,
            )  # Make two pointers 'low' and 'high', and initialize 'sum' as 0.
            while low < high:  # Search between two pointers, similar to binary search.
                s = nums[i] + nums[low] + nums[high]
                if (
                    s > 0
                ):  # If sum is positive, we need more negative numbers to make it 0, decrement high (high -= 1).
                    high -= 1
                elif (
                    s < 0
                ):  # If sum is negative, we need more positive numbers to make it 0, increment low (low += 1).
                    low += 1
                else:
                    answer.append(
                        [nums[i], nums[low], nums[high]]
                    )  # We have found the required triplet, add it to the answer list.
                    last_low_occurrence = nums[low]
                    last_high_occurrence = nums[high]
                    while (
                        low < high and nums[low] == last_low_occurrence
                    ):  # Update 'low' and 'high' with last occurrences of 'low' and 'high'.
                        low += 1
                    while low < high and nums[high] == last_high_occurrence:
                        high -= 1
        return answer  # Return the answer list.
