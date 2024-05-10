from typing import Tuple


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        fractions: list[Tuple[float, int, int]] = []

        for idx_i, val_i in enumerate(arr):
            for _, val_j in enumerate(arr[idx_i + 1 :], start=idx_i + 1):
                fractions.append((val_i / val_j, val_i, val_j))

        fractions.sort()

        return [fractions[k - 1][1], fractions[k - 1][2]]
