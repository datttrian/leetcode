from typing import List


class Solution:
    def combinationSum2(
        self,
        candidates: List[int],
        target: int,
    ) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]) -> None:
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Skip elements if they exceed the remaining target
                if candidates[i] > target:
                    continue

                path.append(candidates[i])
                # Recursively find combinations with the remaining target
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        candidates.sort()
        result: List[List[int]] = []
        backtrack(0, target, [])
        return result
