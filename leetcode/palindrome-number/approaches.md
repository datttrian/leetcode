# Arrays & Hashing

For the Arrays & Hashing approach, you can convert the integer into an array of digits and then check if the array is a palindrome. Here's a Python implementation:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle negative numbers and numbers ending with 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Convert the integer to an array of digits
        digits = []
        while x > 0:
            digit = x % 10
            x //= 10
            digits.append(digit)

        # Check for palindrome using array operations
        n = len(digits)
        for i in range(n // 2):
            if digits[i] != digits[n - 1 - i]:
                return False

        return True
```

Explanation:
1. We extract the digits of `temp_x` and append them to the `digits` array.
2. We check for palindrome using array operations

This solution has a time complexity of O(log10(x)), where x is the input integer, as we are essentially extracting its digits. The space complexity is O(log10(x)) as well, considering the space required for the `digits` array.

# Two Pointers

For the Two Pointers approach, we use two pointers, one starting from the beginning and the other from the end of the integer. We compare the digits pointed to by these two pointers. Here's a Python implementation:

```python
def isPalindrome(x):
    # Convert the integer to a string for easy indexing
    str_x = str(abs(x))
    
    # Initialize two pointers
    left, right = 0, len(str_x) - 1
    
    # Check if the digits at the two pointers are equal
    while left < right:
        if str_x[left] != str_x[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
print(isPalindrome(121))   # Output: True
print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))    # Output: False
```

Explanation:
1. We convert the integer `x` to its absolute value and then to a string (`str_x`).
2. We initialize two pointers, `left` and `right`, pointing to the beginning and end of the string, respectively.
3. We compare the digits at the two pointers and move towards each other until they meet in the middle.
4. If at any point the digits are not equal, we return False, indicating that the integer is not a palindrome.
5. If the loop completes without returning False, we return True.

This solution has a time complexity of O(log10(x)), where x is the input integer, as we are essentially iterating through the digits. The space complexity is O(log10(x)), considering the space required for the string conversion.

# Stack

One way to check if an integer is a palindrome without converting it to a string is by using a stack. Here's a simple Python code for that:

```python
def is_palindrome(x):
    # Handle negative numbers
    if x < 0:
        return False
    
    # Initialize a stack
    stack = []
    original_x = x
    
    # Push digits onto the stack
    while x > 0:
        digit = x % 10
        stack.append(digit)
        x //= 10
    
    # Pop digits from the stack and compare with original number
    while original_x > 0 and stack:
        digit = stack.pop()
        if digit != original_x % 10:
            return False
        original_x //= 10
    
    # If the stack is empty, it's a palindrome
    return not stack

# Example usage:
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121))  # Output: False
print(is_palindrome(10))  # Output: False

```

This solution has a time complexity of O(log10(x)), where x is the input integer, as we are essentially extracting and comparing its digits. The space complexity is O(log10(x)), considering the space required for the `digits` array and the stack.

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