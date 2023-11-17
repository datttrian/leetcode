# Reverse Integer


Given a signed 32-bit integer `x`, return `x` *with its digits
reversed*. If reversing `x` causes the value to go outside the signed
32-bit integer range `[-2`^(`31`)`, 2`^(`31`)` - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).**

 

**Example 1:**

    Input: x = 123
        Output: 321
        

**Example 2:**

    Input: x = -123
        Output: -321
        

**Example 3:**

    Input: x = 120
        Output: 21
        

 

**Constraints:**

- `-2`^(`31`)` <= x <= 2`^(`31`)` - 1`


# Intuition
The problem is to reverse an integer, considering the 32-bit signed integer range. The approach here is to determine the sign of the input number, convert the absolute value of the number to a string, reverse it, and then convert it back to an integer. The original sign is applied to the reversed integer. The function checks if the reversed number is within the 32-bit signed integer range and returns it; otherwise, it returns 0.

# Approach
1. Determine the sign of the input number (`sign`). If it's negative, `sign` will be -1; otherwise, it will be 1.
2. Convert the absolute value of the input number to a string, reverse it, and then convert it back to an integer. Apply the original sign.
3. Check if the reversed number is within the 32-bit signed integer range (from -2^31 to 2^31 - 1).
   - If it is, return the reversed number.
   - If it is not, return 0.

# Complexity
- Time complexity: O(n), where n is the number of digits in `x`. This is because the method converts the integer to a string and iterates over its characters.
- Space complexity: O(n), as it creates a string of length `n` for the reversal process.

# Code
```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_num = sign * int(str(abs(x))[::-1])

        if -(2**31) <= reversed_num <= 2**31 - 1:
            return reversed_num
        else:
            return 0
```