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
Looks like we're dealing with division here. The code probably handles edge cases like division by zero and overflows.

# Approach
The approach seems to be a classic long division method, but implemented in a way that avoids repeated subtraction. Instead, it uses bit manipulation to find the closest multiple of the divisor in each iteration.

# Complexity
- Time complexity: O(\log n), where n is the absolute value of the dividend.
- Space complexity: O(1), as there's no extra space used that scales with the input.

Seems like a solid implementation! Anything specific you'd like to discuss about it?
