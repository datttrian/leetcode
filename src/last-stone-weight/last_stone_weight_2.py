class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()

            if first != second:
                difference = first - second
                import bisect

                bisect.insort(stones, difference)

        return stones[0] if stones else 0
