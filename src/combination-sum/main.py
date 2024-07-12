class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []

        def backtrack(
            start: int, current: list[int], total: int
        ) -> None:
            if total == target:
                result.append(current[:])
            if total <= target:
                for i in range(start, len(candidates)):
                    current.append(candidates[i])
                    backtrack(i, current, total + candidates[i])
                    current.pop()

        backtrack(0, [], 0)
        return result
