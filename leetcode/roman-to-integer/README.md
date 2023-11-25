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
The problem involves converting a Roman numeral string to an integer. Roman numerals have specific rules for representation, such as additive and subtractive combinations. The given code seems to implement a solution using a dictionary to map Roman numeral characters to their corresponding values. The approach appears to be iterating through the string in reverse order and updating the result based on the current and previous values.

# Approach
The approach used in the code is to iterate through the Roman numeral string in reverse order. For each character, the corresponding value is obtained from the dictionary. If the current value is less than the previous value, it indicates a subtractive combination, and the result is decremented; otherwise, it is an additive combination, and the result is incremented. The final result is returned.

# Complexity
- Time complexity: O(n), where n is the length of the input string. The algorithm iterates through the string once.
- Space complexity: O(1), as the space required is constant. The dictionary and a few variables are used regardless of the input size.

The time complexity is linear because the algorithm processes each character in the input string once. The space complexity is constant because the size of the data structures used (dictionary and variables) does not depend on the size of the input.

# Code
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
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

The code looks correct and follows a clear logic for converting Roman numerals to integers. The use of a dictionary for quick value lookup and the iteration through the string in reverse order are appropriate for this problem.