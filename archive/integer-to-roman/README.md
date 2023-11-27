# Integer to Roman


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
The goal is to convert an integer to a Roman numeral. This solution uses a greedy algorithm that iteratively subtracts the largest possible values from the input integer. It employs a predefined set of Roman numeral symbols and their corresponding values to construct the resulting Roman numeral.

# Approach
1. Define the symbols and their corresponding values in lists (`symbols` and `values`).
2. Initialize an empty string (`result`) to store the Roman numeral.
3. Iterate through the symbols and values simultaneously using `zip`.
4. In each iteration, repeat the current symbol as many times as it fits in the number, and subtract the corresponding value from the number.
5. Return the constructed Roman numeral.

# Time Complexity
The time complexity is O(13 * log(num)), where "num" is the input integer. The algorithm iterates through the set of symbols, and in the worst case, the while loop may run log(num) times for each symbol.

# Space Complexity
The space complexity is O(1) as the space required for the algorithm is constant regardless of the input size. It primarily uses the "result" string and the predefined sets of symbols and values.

# Code
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the symbols and their values
        symbols = [
            'M',
            'CM',
            'D',
            'CD',
            'C',
            'XC',
            'L',
            'XL',
            'X',
            'IX',
            'V',
            'IV',
            'I',
        ]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        # Initialize an empty string to store the Roman numeral
        result = ''

        # Iterate through the symbols and values
        for symbol, value in zip(symbols, values):
            # Repeat the symbol as many times as it fits in the number
            while num >= value:
                result += symbol
                num -= value

        return result
```