class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start: int, path: list[int]):
            result.append(path[:])  # Make a copy of the current subset
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result: list[list[int]] = []
        backtrack(0, [])
        return result
