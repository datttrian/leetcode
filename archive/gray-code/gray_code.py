class Solution:
    def grayCode(self, n: int) -> list[int]:
        result: list[int] = []
        for i in range(2**n):
            result.append(i ^ (i >> 1))
        return result
