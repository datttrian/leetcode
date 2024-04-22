class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        length = len(s)

        for i in range(length):
            value = roman_values[s[i]]
            if i + 1 < length and roman_values[s[i + 1]] > value:
                total -= value
            else:
                total += value

        return total
