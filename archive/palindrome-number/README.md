# Palindrome Number


Given an integer `x`, return `true` *if* `x` *is a* ***palindrome*** *, and* `false` *otherwise*.

 

**Example 1:**

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

**Example 2:**

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

**Constraints:**

- `-2`^(`31`)` <= x <= 2`^(`31`)` - 1`

 

**Follow up:** Could you solve it without converting the integer to a
string?


# Intuition
The problem involves determining whether an integer is a palindrome. A palindrome is a number that reads the same backward as forward. The approach involves reversing the given integer and comparing it with the original to check for equality.

# Approach
1. Check for special cases: If the input integer is negative or ends with a zero (except for zero itself), it cannot be a palindrome, and we return False.
2. Initialize `reversed_num` to 0 and `original_num` to the input integer.
3. Use a while loop to reverse the digits of the input integer and store the result in `reversed_num`.
4. Compare the reversed integer with the original integer. If they are equal, the number is a palindrome, and we return True; otherwise, return False.

# Complexity
- Time complexity: O(log10(n)), where n is the input integer. The number of digits in the integer is proportional to log10(n).
- Space complexity: O(1), as only a constant amount of extra space is used.

# Code
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        original_num = x

        while x > 0:
            x, digit = divmod(x, 10)
            reversed_num = reversed_num * 10 + digit

        return reversed_num == original_num
```