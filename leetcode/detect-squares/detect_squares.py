from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self) -> None:
        self.xPoints: defaultdict[int, List[int]] = defaultdict(list)
        self.cnt: defaultdict[tuple[int, int], int] = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xPoints[x].append(y)
        self.cnt[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0
        for y2 in self.xPoints[x1]:
            if y2 == y1:
                continue  # Skip empty square
            sideLen = abs(y2 - y1)

            # Case: p3, p4 points are in the left side
            x3, y3 = x1 - sideLen, y2
            x4, y4 = x1 - sideLen, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]

            # Case 2: p3, p4 points are in the left side
            x3, y3 = x1 + sideLen, y2
            x4, y4 = x1 + sideLen, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]
        return ans
