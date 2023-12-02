# Integer to Roman


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

For example, `2` is written as `II` in Roman numeral, just two one's
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

Given an integer, convert it to a roman numeral.

 

**Example 1:**

    Input: num = 3
        Output: "III"
        Explanation: 3 is represented as 3 ones.
        

**Example 2:**

    Input: num = 58
        Output: "LVIII"
        Explanation: L = 50, V = 5, III = 3.
        

**Example 3:**

    Input: num = 1994
        Output: "MCMXCIV"
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
        

 

**Constraints:**

- `1 <= num <= 3999`


# Intuition
The problem involves converting an integer to a Roman numeral. The given solution uses a dictionary `roman_extend_dict` to map the integer values to their corresponding Roman numeral symbols. The approach appears to iterate through the dictionary in descending order of values and repeatedly divides the given number by the current value to determine the count of symbols needed.

# Approach
1. Define a dictionary `roman_extend_dict` that maps integer values to Roman numeral symbols.
2. Initialize an empty string `result` to store the final Roman numeral.
3. Iterate through the dictionary in descending order of values.
4. In each iteration, use the `divmod` function to find the quotient and remainder when dividing the given number by the current value.
5. Append the corresponding Roman numeral symbol repeated by the quotient to the result string.
6. Update the given number to be the remainder for the next iteration.
7. Repeat the process until the given number becomes zero.
8. Return the final result.

# Complexity
- Time complexity: O(1) since the number of iterations is constant, determined by the number of keys in the dictionary.
- Space complexity: O(1) since the dictionary and result string have fixed sizes.

# Code
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_extend_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        result = ""

        for value, symbol in roman_extend_dict.items():
            count, num = divmod(num, value)

            result += symbol * count

        return result
```