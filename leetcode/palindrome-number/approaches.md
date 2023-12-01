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
        if x < 0:
            return False

        head = None
        original_x = x
        while x > 0:
            digit = x % 10
            x //= 10
            head = ListNode(digit, head)

        current = head
        while original_x > 0 and current:
            if current.value != original_x % 10:
                return False
            current = current.next
            original_x //= 10

        return not current

```

The time complexity of this solution is O(n), where n is the number of digits in the input x. This is because we iterate through the digits of x twice - once to create the linked list and once to compare the values.

The space complexity is also O(n) because we create a linked list to store the digits of x. The space required is proportional to the number of digits in x.

# Math & Geometry

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
The time complexity of this solution is O(log10(x)), where x is the input number. This is because in each iteration of the while loop, we divide the number by 10, reducing its size by a factor of 10. Therefore, the number of iterations required is equal to the number of digits in the input number, which is log10(x).

The space complexity of this solution is O(1) because we only use a constant amount of extra space to store the reversed number and the original number.
