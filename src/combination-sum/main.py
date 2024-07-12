class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []

        def backtrack(
            start: int, current: list[int], total: int
        ) -> None:
            if total == target:
                result.append(current.copy())
                return
            if start >= len(candidates) or total > target:
                return

            current.append(candidates[start])
            backtrack(start, current, total + candidates[start])
            current.pop()
            backtrack(start + 1, current, total)

        backtrack(0, [], 0)
        return result
