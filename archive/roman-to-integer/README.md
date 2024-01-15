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

## Intuition
The problem involves converting a Roman numeral to an integer. One common strategy is to iterate through the Roman numeral string from right to left, adding the corresponding values to the result. If a smaller numeral appears before a larger one, it subtracts its value instead.

## Approach
1. Create a dictionary (`roman_dict`) to map each Roman numeral character to its corresponding integer value.
2. Initialize `result` to 0 and `prev_value` to 0. These variables will be used to keep track of the running total and the value of the previous numeral, respectively.
3. Iterate through the reversed Roman numeral string.
4. For each character, get its integer value from the dictionary.
5. If the current value is less than the previous value, subtract it from the result. Otherwise, add it to the result.
6. Update `prev_value` for the next iteration.
7. Return the final result.

## Complexity
- Time complexity: O(n), where n is the length of the input string `s`. The algorithm iterates through each character in the string once.
- Space complexity: O(1), as the space required is constant. The dictionary and a few integer variables do not depend on the size of the input.

## Code
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

        for _, char in enumerate(reversed(s)):
            current_value = roman_dict[char]

            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value

            prev_value = current_value

        return result
```