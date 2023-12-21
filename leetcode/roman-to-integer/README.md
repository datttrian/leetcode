# Roman to Integer


Roman numerals are represented by seven different symbols: `I`, `V`,
`X`, `L`, `C`, `D` and `M`.

    Symbol       Value
    I            1
    V            5
    X            10
    L            50
    C            100
    D            500
    M            1000

For example, `2` is written as `II` in Roman numeral, just two ones
added together. `12` is written as `XII`, which is simply `X + II`. The
number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to
right. However, the numeral for four is not `IIII`. Instead, the number
four is written as `IV`. Because the one is before the five we subtract
it making four. The same principle applies to the number nine, which is
written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

**Example 1:**

    Input: s = "III"
        Output: 3
        Explanation: III = 3.
        

**Example 2:**

    Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.
        

**Example 3:**

    Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
        

 

**Constraints:**

- `1 <= s.length <= 15`
- `s` contains only the characters
  `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range
  `[1, 3999]`.

# Intuition
The problem is to convert a Roman numeral to an integer. Roman numerals follow a specific pattern where a smaller numeral appearing before a larger one means subtraction. For example, in "IV", "I" is before "V" (which is larger), so it means 4 (5-1).

# Approach
The approach is to iterate over the string in reverse order. For each character, we get its corresponding integer value from a predefined dictionary. If the current value is less than the previous value, it means we have a case like "IV", so we subtract the current value from the result. Otherwise, we add the current value to the result. The previous value is then updated to the current value for the next iteration.

# Complexity
- Time complexity: The time complexity is O(n), where n is the length of the string. This is because we are iterating over the string once.
- Space complexity: The space complexity is O(1), as we are using a constant amount of space to store the Roman numeral dictionary and a few integer variables.

# Code
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer.

        Parameters:
        s (str): A string representing a Roman numeral.

        Returns:
        int: The integer representation of the Roman numeral.
        """

        # Define a dictionary to map numerals to integer
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Initialize the result and the previous value
        result = 0
        prev_value = 0

        # Iterate over the string in reverse order
        for char in reversed(s):
            # Get the integer value of the current Roman numeral
            current_value = roman_dict[char]

            # If the current value is less than the previous value
            if current_value < prev_value:
                # Subtract it from the result
                result -= current_value
            else:
                # Otherwise, add the current value to the result
                result += current_value

            # Update the previous value for the next iteration
            prev_value = current_value

        # Return the final result
        return result
```
