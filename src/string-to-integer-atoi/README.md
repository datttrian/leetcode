# String to Integer (atoi)


Implement the `myAtoi(string s)` function, which converts a string to a
32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:

1.  Read in and ignore any leading whitespace.
2.  Check if the next character (if not already at the end of the
    string) is `'-'` or `'+'`. Read this character in if it is either.
    This determines if the final result is negative or positive
    respectively. Assume the result is positive if neither is present.
3.  Read in next the characters until the next non-digit character or
    the end of the input is reached. The rest of the string is ignored.
4.  Convert these digits into an integer (i.e. `"123" -> 123`,
    `"0032" -> 32`). If no digits were read, then the integer is `0`.
    Change the sign as necessary (from step 2).
5.  If the integer is out of the 32-bit signed integer range
    `[-2`^(`31`)`, 2`^(`31`)` - 1]`, then clamp the integer so that it
    remains in the range. Specifically, integers less than `-2`^(`31`)
    should be clamped to `-2`^(`31`), and integers greater than
    `2`^(`31`)` - 1` should be clamped to `2`^(`31`)` - 1`.
6.  Return the integer as the final result.

**Note:**

- Only the space character `' '` is considered a whitespace character.
- **Do not ignore** any characters other than the leading whitespace or
  the rest of the string after the digits.

 

**Example 1:**

    Input: s = "42"
        Output: 42
        Explanation: The underlined characters are what is read in, the caret is the current reader position.
        Step 1: "42" (no characters read because there is no leading whitespace)
                 ^
        Step 2: "42" (no characters read because there is neither a '-' nor '+')
                 ^
        Step 3: "42" ("42" is read in)
                   ^
        The parsed integer is 42.
        Since 42 is in the range [-231, 231 - 1], the final result is 42.
        

**Example 2:**

    Input: s = "   -42"
        Output: -42
        Explanation:
        Step 1: "   -42" (leading whitespace is read and ignored)
                    ^
        Step 2: "   -42" ('-' is read, so the result should be negative)
                     ^
        Step 3: "   -42" ("42" is read in)
                       ^
        The parsed integer is -42.
        Since -42 is in the range [-231, 231 - 1], the final result is -42.
        

**Example 3:**

    Input: s = "4193 with words"
        Output: 4193
        Explanation:
        Step 1: "4193 with words" (no characters read because there is no leading whitespace)
                 ^
        Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
                 ^
        Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
                     ^
        The parsed integer is 4193.
        Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
        

 

**Constraints:**

- `0 <= s.length <= 200`
- `s` consists of English letters (lower-case and upper-case), digits
  (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.


# Intuition
The problem is to convert the initial portion of a string to a 32-bit signed integer. The approach is to iterate through the string, handling optional leading white spaces, an optional sign, and numerical characters. Non-numeric characters are ignored, and the function stops processing upon encountering them. The function also handles integer overflow and underflow by clamping the result to the range of 32-bit signed integers.

# Approach
1. Define the range of a 32-bit signed integer: `INT_MAX` (2^31 - 1) and `INT_MIN` (-2^31).
2. Initialize variables: `i` for iterating through the string, `n` for the length of the string, `sign` to keep track of the sign, and `result` to store the converted integer.
3. Skip leading whitespace by incrementing `i` while `s[i]` is a space character.
4. Check for the sign:
   - If `s[i]` is '-' or '+', update `sign` accordingly and increment `i`.
5. Convert numbers and stop at the first non-digit:
   - While `i` is less than `n` and `s[i]` is a digit, convert the digit to an integer.
   - Check for overflow/underflow and clamp the result if necessary. This check prevents overflow during the calculation.
   - Update `result` by multiplying it by 10 and adding the digit.
   - Increment `i`.
6. Return `sign * result`.

# Complexity
- Time complexity: O(n), where n is the length of the string. The function iterates through the string once.
- Space complexity: O(1), as it uses a constant amount of space.

# Code
```python
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        i = 0
        n = len(s)
        sign = 1
        result = 0

        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Check for sign
        if i < n and s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Convert numbers and stop at the first non-digit
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow/underflow and clamp if necessary
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
```