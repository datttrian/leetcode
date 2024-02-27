from typing import List


class Solution:
    def combinationSum(
        self,
        candidates: List[int],
        target: int,
    ) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]) -> None:
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                # Notice the start parameter to avoid duplicate combinations
                backtrack(i, target - candidates[i], path)
                path.pop()

        result: List[List[int]] = []
        candidates.sort()
        backtrack(0, target, [])
        return result
