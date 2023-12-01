class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        stack: list[int] = []

        for char in s:
            current_value = roman_dict[char]

            while stack and current_value > stack[-1]:
                result -= stack.pop()

            stack.append(current_value)

        result += sum(stack)

        return result
