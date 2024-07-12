class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            x = stones.pop(0)
            y = stones.pop(0)
            if x != y:
                stones.append(x - y)

        return stones[0] if stones else 0


solution = Solution()
print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(solution.lastStoneWeight([1]))
