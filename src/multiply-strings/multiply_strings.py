from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Reverse the input strings for easier calculation
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Initialize the result array with zeros
        result: List[int] = [0] * (len(num1) + len(num2))

        # Perform the multiplication digit by digit
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += int(num1[i]) * int(num2[j])
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Remove leading zeros from the result
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Convert the result array to a string and reverse it
        result_str: str = ''.join(map(str, result[::-1]))

        return result_str
