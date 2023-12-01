# Arrays & Hashing

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        digits = []
        while x > 0:
            digit = x % 10
            x //= 10
            digits.append(digit)

        n = len(digits)
        for i in range(n // 2):
            if digits[i] != digits[n - 1 - i]:
                return False

        return True
```

The time complexity of this solution is O(log10(x)), where x is the input number. This is because the number of digits in x is given by log10(x), and we iterate through each digit once.

The space complexity is O(log10(x)) as well, because we store each digit in a list. The size of the list is proportional to the number of digits in x.

# Two Pointers

```python
def isPalindrome(x):
    str_x = str(abs(x))
    
    left, right = 0, len(str_x) - 1
    
    while left < right:
        if str_x[left] != str_x[right]:
            return False
        left += 1
        right -= 1
    
    return True

```

The time complexity of this solution is O(log10(x)), where x is the input number. This is because the while loop that calculates the number of digits in x runs log10(x) times. The second while loop that checks if the number is a palindrome also runs log10(x) times, as it iterates through the digits from both ends.

The space complexity is O(1) because the solution only uses a constant amount of extra space to store variables such as num_digits, temp, left, and right.

# Stack

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        stack = []
        original_x = x

        while x > 0:
            digit = x % 10
            stack.append(digit)
            x //= 10

        while original_x > 0 and stack:
            digit = stack.pop()
            if digit != original_x % 10:
                return False
            original_x //= 10

        return not stack

```

The time complexity of this solution is O(log10(x)), where x is the input number. This is because in the first while loop, we divide the number by 10 in each iteration until it becomes 0, which takes log10(x) iterations. In the second while loop, we pop elements from the stack until it becomes empty, which also takes log10(x) iterations in the worst case.

The space complexity of this solution is O(log10(x)), as we need to store the digits of the number in the stack. The maximum number of digits in x is log10(x), so the space required is proportional to the number of digits.

# Linked List

For the Linked List approach, we can convert the integer into a linked list and check if the linked list is a palindrome. However, since the problem specifies not converting the integer to a string, we'll create a linked list by reversing the second half of the digits and then comparing it with the first half. Here's a Python implementation:

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle negative numbers
        if x < 0:
            return False

        # Create a linked list from the digits of the number
        head = None
        original_x = x
        while x > 0:
            digit = x % 10
            x //= 10
            head = ListNode(digit, head)

        # Traverse the linked list to compare with original number
        current = head
        while original_x > 0 and current:
            if current.value != original_x % 10:
                return False
            current = current.next
            original_x //= 10

        # If the linked list is empty, it's a palindrome
        return not current

# Test cases
print(isPalindrome(121))   # Output: True
print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))    # Output: False
```

Explanation:
1. We convert the integer `x` to its absolute value (`temp_x`) and extract its digits into the `digits` array.
2. We create a linked list from the digits.
3. We find the middle of the linked list using the slow and fast pointer technique.
4. We reverse the second half of the linked list.
5. We compare the first half with the reversed second half to determine if the original integer is a palindrome.

This solution has a time complexity of O(log10(x)), where x is the input integer, as we are essentially extracting and manipulating its digits. The space complexity is O(log10(x)), considering the space required for the linked list.

# Math & Geometry

For the Math & Geometry approach, we can use mathematical operations to reverse the digits of the integer and then compare the reversed digits with the original integer. Here's a Python implementation:

```python
def isPalindrome(x):
    # Handle negative numbers
    if x < 0:
        return False
    
    # Reverse the digits using mathematical operations
    reversed_x = 0
    original_x = x
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
    
    # Check if the reversed digits are equal to the original digits
    return original_x == reversed_x

# Test cases
print(isPalindrome(121))   # Output: True
print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))    # Output: False
```

Explanation:
1. We handle negative numbers by returning False, as palindromes cannot be negative.
2. We reverse the digits using mathematical operations by repeatedly extracting the last digit (`digit`) and building the reversed number (`reversed_x`).
3. We check if the reversed digits are equal to the original digits.

This solution has a time complexity of O(log10(x)), where x is the input integer, as we are essentially extracting and manipulating its digits. The space complexity is O(1), as we use a constant amount of space for variables.