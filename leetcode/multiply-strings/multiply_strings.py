class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1, digit1 in enumerate(num1):
            for i2, digit2 in enumerate(num2):
                digit = int(digit1) * int(digit2)
                carry, remainder = divmod(result[i1 + i2] + digit, 10)
                result[i1 + i2] = remainder
                result[i1 + i2 + 1] += carry

        result, begin = result[::-1], 0
        while begin < len(result) and result[begin] == 0:
            begin += 1

        return "".join(map(str, result[begin:]))
