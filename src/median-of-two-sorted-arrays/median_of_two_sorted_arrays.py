from typing import List, Optional


class Solution:
    def findMedianSortedArrays(
        self,
        a: List[int],
        b: List[int],
    ) -> Optional[float]:
        l: int = len(a) + len(b)

        if l == 0:
            return None
        if l % 2:
            return self.get_median(a, b, l // 2)
        else:
            return (
                self.get_median(a, b, l // 2)
                + self.get_median(a, b, l // 2 - 1)
            ) / 2

    def get_median(self, a: List[int], b: List[int], idx: int) -> int:
        if not a:
            return b[idx]
        if not b:
            return a[idx]

        ai: int = len(a) // 2
        bi: int = len(b) // 2
        ma: int = a[ai]
        mb: int = b[bi]

        if ma > mb:
            a, b = b, a
            ai, bi = bi, ai

        max_idx_ma: int = ai + bi

        if max_idx_ma < idx:
            return self.get_median(a[ai + 1 :], b, idx - (ai + 1))
        else:
            return self.get_median(a, b[:bi], idx)
