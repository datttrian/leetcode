from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int):
            if start == len(nums):
                result.append(
                    nums.copy(),
                )  # Make a copy of the current permutation
                return

            for i in range(start, len(nums)):
                # Skip duplicates to avoid duplicate permutations
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Swap the current element with the element at the current
                # position
                nums[start], nums[i] = nums[i], nums[start]

                # Recursively generate permutations for the remaining elements
                backtrack(start + 1)

                # Undo the swap to backtrack and explore other possibilities
                nums[start], nums[i] = nums[i], nums[start]

        result: List[List[int]] = []
        nums.sort()  # Sort the input array to handle duplicates
        backtrack(0)
        return result
