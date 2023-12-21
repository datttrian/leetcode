The problem of converting a Roman numeral to an integer can be solved using different approaches. Here are two common ones:

1. **Right-to-Left Parsing (as described in your question)**

This approach involves iterating through the Roman numeral string from right to left, adding the corresponding values to the result. If a smaller numeral appears before a larger one, it subtracts its value instead.

```python
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
        prev_value = 0

        for char in reversed(s):
            current_value = roman_dict[char]

            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value

            prev_value = current_value

        return result
```

2. **Left-to-Right Parsing**

This approach involves iterating through the Roman numeral string from left to right. If a larger numeral appears after a smaller one, it subtracts the smaller numeral from the larger one and adds the result to the total. Otherwise, it simply adds the value of the numeral to the total.

```python
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
        i = 0

        while i < len(s):
            if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
                result += roman_dict[s[i+1]] - roman_dict[s[i]]
                i += 2
            else:
                result += roman_dict[s[i]]
                i += 1

        return result
```

Both approaches have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1), as the space required is constant and does not depend on the size of the input.