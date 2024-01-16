class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]

        result: list[int] = [0] * (len(num1) + len(num2))

        for i, digit1 in enumerate(num1):
            for j, digit2 in enumerate(num2):
                result[i + j] += int(digit1) * int(digit2)
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result_str: str = "".join(map(str, result[::-1]))

        return result_str
