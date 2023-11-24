# Roman to Integer


Roman numerals are represented by seven different symbols: `I`, `V`,
`X`, `L`, `C`, `D` and `M`.

    Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

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
The goal is to convert a Roman numeral string to an integer. This solution uses a dictionary (`roman_dict`) to map Roman numerals to their corresponding values. It iterates through the input string in reverse order and applies the rules of Roman numeral representation to compute the integer value.

# Approach
1. Create a dictionary (`roman_dict`) to map Roman numerals to their corresponding values.
2. Initialize variables (`result` and `prev_value`) to keep track of the accumulated integer value and the value of the previous Roman numeral.
3. Iterate through the input string (`s`) in reverse order.
4. For each character, retrieve its corresponding value from the dictionary (`current_value`).
5. Compare the current value with the previous value:
   - If the current value is smaller than the previous, subtract it from the result.
   - If the current value is greater or equal to the previous, add it to the result.
6. Update the `prev_value` for the next iteration.
7. Return the final result.

# Time Complexity
The time complexity is O(n), where n is the length of the input string. The algorithm iterates through each character of the string once.

# Space Complexity
The space complexity is O(1), as the space required is constant. The dictionary and variables used for computation do not scale with the input size.

# Code
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping Roman numerals to their corresponding values
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        # Initialize the result and keep track of the previous Roman numeral value
        result = 0
        prev_value = 0

        # Iterate through the input string in reverse order
        for char in reversed(s):
            current_value = roman_dict[char]
            # Compare the current value with the previous one
            if current_value < prev_value:
                # If the current value is smaller than the previous, subtract it
                result -= current_value
            else:
                # If the current value is greater or equal to the previous, add it
                result += current_value
            # Update the previous value for the next iteration
            prev_value = current_value

        # Return the final result
        return result
```