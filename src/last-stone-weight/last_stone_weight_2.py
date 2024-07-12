from bisect import insort


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            x = stones.pop()
            y = stones.pop()

            if x != y:
                insort(stones, x - y)

        return stones[0] if stones else 0
