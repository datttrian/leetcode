class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start: int):
            if start == len(nums) - 1:
                result.append(nums[:])
                return
            unique_set: set[int] = set()
            for i in range(start, len(nums)):
                if nums[i] in unique_set:
                    continue
                unique_set.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result: list[list[int]] = []
        nums.sort()
        backtrack(0)
        return result
