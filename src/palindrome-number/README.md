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
The problem is to determine whether a given integer is a palindrome. A palindrome is a number that reads the same backward as forward. The approach is to reverse the digits of the original number and check if the reversed number equals the original number.

# Approach
1. Special cases: Negative numbers and numbers ending with 0 are not palindromes. Return False in such cases.
2. Initialize variables to store the reversed number (`reversed_num`) and the original number (`original_num`).
3. Reverse the digits of the original number using a while loop:
   - Extract the last digit (`digit`) from the original number.
   - Update `reversed_num` by multiplying it by 10 and adding the digit.
   - Remove the last digit from the original number (`x //= 10`).
4. Check if the reversed number equals the original number, indicating a palindrome.
5. Return True if the number is a palindrome; otherwise, return False.

# Time Complexity
O(log10(x)) - The number of iterations in the while loop is proportional to the number of digits in the input integer.

# Space Complexity
O(1) - Constant space is used to store the reversed number and the original number.

# Code
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases: Negative numbers and numbers ending with 0 are not
        # palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Initialize variables to store the reversed number and the original
        # number
        reversed_num = 0
        original_num = x

        # Reverse the digits of the original number
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        # Check if the reversed number equals the original number, indicating
        # a palindrome
        return reversed_num == original_num
```