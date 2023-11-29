# Divide Two Integers


Given two integers `dividend` and `divisor`, divide two integers
**without** using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its
fractional part. For example, `8.345` would be truncated to `8`, and
`-2.7335` would be truncated to `-2`.

Return *the **quotient** after dividing* `dividend` *by* `divisor`.

**Note:** Assume we are dealing with an environment that could only
store integers within the **32-bit** signed integer range:
`[−2`^(`31`)`, 2`^(`31`)` − 1]`. For this problem, if the quotient is
**strictly greater than** `2`^(`31`)` - 1`, then return
`2`^(`31`)` - 1`, and if the quotient is **strictly less than**
`-2`^(`31`), then return `-2`^(`31`).

 

**Example 1:**

    Input: dividend = 10, divisor = 3
        Output: 3
        Explanation: 10/3 = 3.33333.. which is truncated to 3.
        

**Example 2:**

    Input: dividend = 7, divisor = -3
        Output: -2
        Explanation: 7/-3 = -2.33333.. which is truncated to -2.
        

 

**Constraints:**

- `-2`^(`31`)` <= dividend, divisor <= 2`^(`31`)` - 1`
- `divisor != 0`


# Intuition
This problem revolves around efficiently dividing two integers, with a key focus on optimizing the process through bit manipulation. The approach carefully considers the sign of the result to handle cases where the dividend and divisor have different signs.

# Approach
1. Define constants for maximum and minimum integer values.
2. Check for special cases: division by zero and if the dividend is zero.
3. Determine the sign of the result based on the signs of the dividend and divisor.
4. Take the absolute values of the dividend and divisor for easier manipulation.
5. Initialize the quotient to 0.
6. Use a loop to perform the division:
   - Find the largest multiple of the divisor that can be subtracted from the current dividend.
   - Subtract this multiple and update the quotient.
7. Adjust the sign of the quotient and ensure it doesn't exceed the integer limits.
8. Return the final quotient.

# Complexity
- Time complexity: O(log n), where n is the absolute value of the dividend. The algorithm essentially performs binary division, repeatedly halving the dividend.
- Space complexity: O(1), as the space required is constant.

# Code
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN
        if dividend == 0:
            return 0

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dividend -= temp_divisor
            quotient += multiple

        quotient *= sign

        return min(max(quotient, INT_MIN), INT_MAX)
```