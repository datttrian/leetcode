class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0
        for i in range(n - 1, -1, -1):
            if citations[i] >= n - i:
                h = max(h, n - i)
            else:
                break
        return h
