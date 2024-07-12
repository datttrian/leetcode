# LeetCode

## Easy

### 217. Contains Duplicate

Given an integer array `nums`, return `true` if any value appears **at
least twice** in the array, and return `false` if every element is
distinct.

**Example 1:**

    Input: nums = [1,2,3,1]
    Output: true

**Example 2:**

    Input: nums = [1,2,3,4]
    Output: false

**Example 3:**

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

**Constraints:**

- `1 <= nums.length <= 10`<sup>`5`</sup>
- `-10`<sup>`9`</sup>`<= nums[i] <= 10`<sup>`9`</sup>

#### Brute Force - O(n^2), O(1)

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


solution = Solution()
print(solution.containsDuplicate(nums=[1, 2, 3, 1]))
print(solution.containsDuplicate(nums=[1, 2, 3, 4]))
print(solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
```

    True
    False
    True

#### Sorting - O(n log n), O(1)

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


solution = Solution()
print(solution.containsDuplicate(nums=[1, 2, 3, 1]))
print(solution.containsDuplicate(nums=[1, 2, 3, 4]))
print(solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
```

    True
    False
    True

#### Arrays & Hashing - O(n), O(n)

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_unique: set[int] = set()
        for num in nums:
            if num in nums_unique:
                return True
            nums_unique.add(num)
        return False


solution = Solution()
print(solution.containsDuplicate(nums=[1, 2, 3, 1]))
print(solution.containsDuplicate(nums=[1, 2, 3, 4]))
print(solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
```

    True
    False
    True

### 242. Valid Anagram

Given two strings `s` and `t`, return `true` *if* `t` *is an anagram of*
`s`*, and* `false` *otherwise*.

An **Anagram** is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters
exactly once.

**Example 1:**

    Input: s = "anagram", t = "nagaram"
    Output: true

**Example 2:**

    Input: s = "rat", t = "car"
    Output: false

**Constraints:**

- `1 <= s.length, t.length <= 5 * 10`<sup>`4`</sup>
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would
you adapt your solution to such a case?

#### Brute Force - O(n^2), O(1)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            is_matched = False

            for i, c in enumerate(t):
                if c == char:
                    t = t[:i] + t[i + 1 :]
                    is_matched = True
                    break

            if not is_matched:
                return False

        return True


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
```

    True
    False

#### Sorting - O(n log n), O(n)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
```

    True
    False

#### Arrays & Hashing - O(n), O(1)

```python
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
```

    True
    False

#### Using Character Count as Key - O(n), O(1)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26  # lowercase English letters

        for i, char in enumerate(s):
            count[ord(char) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1

        return all(c == 0 for c in count)


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
```

    True
    False

#### Using Prime Numbers - O(n), O(1)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        prime_numbers = {
            "a": 2,
            "b": 3,
            "c": 5,
            "d": 7,
            "e": 11,
            "f": 13,
            "g": 17,
            "h": 19,
            "i": 23,
            "j": 29,
            "k": 31,
            "l": 37,
            "m": 41,
            "n": 43,
            "o": 47,
            "p": 53,
            "q": 59,
            "r": 61,
            "s": 67,
            "t": 71,
            "u": 73,
            "v": 79,
            "w": 83,
            "x": 89,
            "y": 97,
            "z": 101,
        }

        product_s = 1
        for char in s:
            product_s *= prime_numbers[char]

        product_t = 1
        for char in t:
            product_t *= prime_numbers[char]

        return product_s == product_t


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
```

    True
    False

### 1. Two Sum

Given an array of integers `nums` and an integer `target`, return
*indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**,
and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

**Example 3:**

    Input: nums = [3,3], target = 6
    Output: [0,1]

**Constraints:**

- `2 <= nums.length <= 10`<sup>`4`</sup>
- `-10`<sup>`9`</sup>`<= nums[i] <= 10`<sup>`9`</sup>
- `-10`<sup>`9`</sup>`<= target <= 10`<sup>`9`</sup>
- **Only one valid answer exists.**

**Follow-up:** Can you come up with an algorithm that is less than
`O(n`<sup>`2`</sup>`)` time complexity?

#### Brute Force - O(n^2), O(1)

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
print(solution.twoSum(nums=[3, 2, 4], target=6))
print(solution.twoSum(nums=[3, 3], target=6))
```

    [0, 1]
    [1, 2]
    [0, 1]

#### Two Pointers - O(n log n), O(n)

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_sorted = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums_sorted[left][1] + nums_sorted[right][1]
            if current_sum == target:
                return [nums_sorted[left][0], nums_sorted[right][0]]

            if current_sum < target:
                left += 1
            else:
                right -= 1
        return []


solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
print(solution.twoSum(nums=[3, 2, 4], target=6))
print(solution.twoSum(nums=[3, 3], target=6))
```

    [0, 1]
    [1, 2]
    [0, 1]

#### Arrays & Hashing - O(n), O(n)

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_index: dict[int, int] = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in nums_index:
                return [nums_index[complement], index]

            nums_index[num] = index

        return []


solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
print(solution.twoSum(nums=[3, 2, 4], target=6))
print(solution.twoSum(nums=[3, 3], target=6))
```

    [0, 1]
    [1, 2]
    [0, 1]

### 125. Valid Palindrome

A phrase is a **palindrome** if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters, it
reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or*
`false` *otherwise*.

**Example 1:**

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

**Example 2:**

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

**Example 3:**

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

**Constraints:**

- `1 <= s.length <= 2 * 10`<sup>`5`</sup>
- `s` consists only of printable ASCII characters.

#### Brute Force - O(n), O(n)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_s = "".join(char.lower() for char in s if char.isalnum())
        return normalized_s == normalized_s[::-1]


solution = Solution()
print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
print(solution.isPalindrome(s="race a car"))
print(solution.isPalindrome(s=" "))
```

    True
    False
    True

#### Two Pointers - O(n), O(1)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alpha_num(c: str) -> bool:
            return (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            )

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not alpha_num(s[left]):
                left += 1
            while left < right and not alpha_num(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


solution = Solution()
print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
print(solution.isPalindrome(s="race a car"))
print(solution.isPalindrome(s=" "))
```

    True
    False
    True

### 170. Two Sum III - Data structure design

Design a data structure that accepts a stream of integers and checks if
it has a pair of integers that sum up to a particular value.

Implement the `TwoSum` class:

- `TwoSum()` Initializes the `TwoSum` object, with an empty array
    initially.
- `void add(int number)` Adds `number` to the data structure.
- `boolean find(int value)` Returns `true` if there exists any pair of
    numbers whose sum is equal to `value`, otherwise, it returns
    `false`.

**Example 1:**

    Input
    ["TwoSum", "add", "add", "add", "find", "find"]
    [[], [1], [3], [5], [4], [7]]
    Output
    [null, null, null, null, true, false]

    Explanation
    TwoSum twoSum = new TwoSum();
    twoSum.add(1);   // [] --> [1]
    twoSum.add(3);   // [1] --> [1,3]
    twoSum.add(5);   // [1,3] --> [1,3,5]
    twoSum.find(4);  // 1 + 3 = 4, return true
    twoSum.find(7);  // No two integers sum up to 7, return false

**Constraints:**

- `-10^5 <= number <= 10^5`
- `-2^31 <= value <= 2^31 - 1`
- At most `5 * 10^4` calls will be made to `add` and `find`.

### 121. Best Time to Buy and Sell Stock

You are given an array `prices` where `prices[i]` is the price of a
given stock on the `i`<sup>`th`</sup> day.

You want to maximize your profit by choosing a **single day** to buy one
stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If
you cannot achieve any profit, return `0`.

**Example 1:**

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

**Constraints:**

- `1 <= prices.length <= 10`<sup>`5`</sup>
- `0 <= prices[i] <= 10`<sup>`4`</sup>

#### Brute Force - O(n^2), O(1)

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0

        for i in range(n):
            for j in range(i + 1, n):
                max_profit = max(prices[j] - prices[i], max_profit)

        return max_profit


solution = Solution()
print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
```

    5
    0

#### Sliding Window - O(n), O(1)

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


solution = Solution()
print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
```

    5
    0

### 20. Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`,
`'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same
    type.

**Example 1:**

    Input: s = "()"
    Output: true

**Example 2:**

    Input: s = "()[]{}"
    Output: true

**Example 3:**

    Input: s = "(]"
    Output: false

**Constraints:**

- `1 <= s.length <= 10`<sup>`4`</sup>
- `s` consists of parentheses only `'()[]{}'`.

#### Brute Force - O(n^2), O(n)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        matching_parentheses = ["()", "{}", "[]"]
        while any(pair in s for pair in matching_parentheses):
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return not s


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
```

    True
    True
    False

#### Recursion - O(n^2), O(n)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        n = len(s)
        i = 0
        matching_parentheses = [("(", ")"), ("{", "}"), ("[", "]")]

        while i < n - 1:
            for opening, closing in matching_parentheses:
                if s[i] == opening and s[i + 1] == closing:
                    new_s = s[:i] + s[i + 2 :]
                    return self.isValid(new_s)
            i += 1

        return False


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
```

    True
    True
    False

#### Stack - O(n), O(n)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        matching_parentheses = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in matching_parentheses:
                if not stack or stack.pop() != matching_parentheses[char]:
                    return False
            else:
                stack.append(char)

        return not stack


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
```

    True
    True
    False

### 704. Binary Search

Given an array of integers `nums` which is sorted in ascending order,
and an integer `target`, write a function to search `target` in `nums`.
If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

**Example 2:**

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

**Constraints:**

- `1 <= nums.length <= 10`<sup>`4`</sup>
- `-10`<sup>`4`</sup>`< nums[i], target < 10`<sup>`4`</sup>
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

#### Two Pointers - O(log n), O(1)

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            left, right = (mid + 1, right) if nums[mid] < target else (left, mid - 1)

        return -1


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], target=9))
print(solution.search([-1, 0, 3, 5, 9, 12], target=2))
```

    4
    -1

#### Recursion - O(log n), O(1)

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            return (
                binary_search(mid + 1, right)
                if nums[mid] < target
                else binary_search(left, mid - 1)
            )

        return binary_search(0, len(nums) - 1)


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], target=9))
print(solution.search([-1, 0, 3, 5, 9, 12], target=2))
```

    4
    -1

#### Exponential Search - O(log n), O(1)

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if nums[0] == target:
            return 0

        n = len(nums)
        bound = 1
        while bound < n and nums[bound] < target:
            bound *= 2

        left = bound // 2
        right = min(bound, n - 1)

        def binary_search(left: int, right: int):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid

                left, right = (
                    (mid + 1, right) if nums[mid] < target else (left, mid - 1)
                )

            return -1

        return binary_search(left, right)


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], target=9))
print(solution.search([-1, 0, 3, 5, 9, 12], target=2))
```

    4
    -1

### 206. Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return
*the reversed list*.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg"
style="width: 542px; height: 222px;" />

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg"
style="width: 182px; height: 222px;" />

    Input: head = [1,2]
    Output: [2,1]

**Example 3:**

    Input: head = []
    Output: []

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or
recursively. Could you implement both?

```python
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(
        self,
        val: int = 0,
        nextNode: "Optional[ListNode]" = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = nextNode
```

```python
# Helper function to convert list to linked list
def list_to_linkedlist(lst: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


# Helper function to convert linked list to list
def linkedlist_to_list(node: Optional[ListNode]) -> list[int]:
    result: list[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result
```

#### Iterative - O(n), O(1)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node


solution = Solution()
print(linkedlist_to_list(solution.reverseList(list_to_linkedlist([1, 2, 3, 4, 5]))))
print(linkedlist_to_list(solution.reverseList(list_to_linkedlist([1, 2]))))
print(linkedlist_to_list(solution.reverseList(list_to_linkedlist([]))))
```

    [5, 4, 3, 2, 1]
    [2, 1]
    []

#### Recursive - O(n), O(n)

```python
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(
        self,
        val: int = 0,
        nextNode: "Optional[ListNode]" = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = nextNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


solution = Solution()
print(linkedlist_to_list(solution.reverseList(list_to_linkedlist([1, 2, 3, 4, 5]))))
print(linkedlist_to_list(solution.reverseList(list_to_linkedlist([1, 2]))))
print(linkedlist_to_list(solution.reverseList(list_to_linkedlist([]))))
```

    [5, 4, 3, 2, 1]
    [2, 1]
    []

### 21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by
splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg"
style="width: 662px; height: 302px;" />

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

**Example 2:**

    Input: list1 = [], list2 = []
    Output: []

**Example 3:**

    Input: list1 = [], list2 = [0]
    Output: [0]

**Constraints:**

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

```python
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(
        self,
        val: int = 0,
        nextNode: "Optional[ListNode]" = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = nextNode
```

```python
# Helper function to convert list to linked list
def list_to_linkedlist(lst: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


# Helper function to convert linked list to list
def linkedlist_to_list(node: Optional[ListNode]) -> list[int]:
    result: list[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result
```

#### Iterative - O(n), O(1)

```python
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next


solution = Solution()
print(
    linkedlist_to_list(
        solution.mergeTwoLists(
            list_to_linkedlist([1, 2, 4]), list_to_linkedlist([1, 3, 4])
        )
    )
)
print(
    linkedlist_to_list(
        solution.mergeTwoLists(list_to_linkedlist([]), list_to_linkedlist([]))
    )
)
print(
    linkedlist_to_list(
        solution.mergeTwoLists(list_to_linkedlist([]), list_to_linkedlist([0]))
    )
)
```

    [1, 1, 2, 3, 4, 4]
    []
    [0]

#### Recursive - O(n), O(n)

```python
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(
        self,
        val: int = 0,
        nextNode: "Optional[ListNode]" = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = nextNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2


solution = Solution()
print(
    linkedlist_to_list(
        solution.mergeTwoLists(
            list_to_linkedlist([1, 2, 4]), list_to_linkedlist([1, 3, 4])
        )
    )
)
print(
    linkedlist_to_list(
        solution.mergeTwoLists(list_to_linkedlist([]), list_to_linkedlist([]))
    )
)
print(
    linkedlist_to_list(
        solution.mergeTwoLists(list_to_linkedlist([]), list_to_linkedlist([0]))
    )
)
```

    [1, 1, 2, 3, 4, 4]
    []
    [0]

### 141. Linked List Cycle

Given `head`, the head of a linked list, determine if the linked list
has a cycle in it.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the `next` pointer.
Internally, `pos` is used to denote the index of the node
that tail's `next` pointer is connected to. **Note that `pos` is not
passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise,
return `false`.

**Example 1:**

<img
src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png"
style="width: 300px; height: 97px; margin-top: 8px; margin-bottom: 8px;" />

    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**

<img
src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png"
style="width: 141px; height: 74px;" />

    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

**Example 3:**

<img
src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png"
style="width: 45px; height: 45px;" />

    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

```python
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(
        self,
        val: int = 0,
        nextNode: Optional["ListNode"] = None,
    ) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = nextNode
```

```python
def list_to_linked_list(lst: list[int], pos: int) -> Optional[ListNode]:
    nodes = [ListNode(val) for val in lst]

    for i in range(1, len(lst)):
        nodes[i - 1].next = nodes[i]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]
```

#### Arrays & Hashing - O(n), O(n)

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = {}
        current_node = head

        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes[current_node] = True
            current_node = current_node.next

        return False


solution = Solution()
print(solution.hasCycle(list_to_linked_list([3, 2, 0, -4], 1)))
print(solution.hasCycle(list_to_linked_list([1, 2], 0)))
print(solution.hasCycle(list_to_linked_list([1], -1)))
```

    True
    True
    False

#### Two Pointers - O(n), O(1)

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


solution = Solution()
print(solution.hasCycle(list_to_linked_list([3, 2, 0, -4], 1)))
print(solution.hasCycle(list_to_linked_list([1, 2], 0)))
print(solution.hasCycle(list_to_linked_list([1], -1)))
```

    True
    True
    False

### 226. Invert Binary Tree

Given the `root` of a binary tree, invert the tree, and return *its
root*.

**Example 1:**

<img
src="https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg"
style="width: 500px; height: 165px;" />

    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

**Example 2:**

<img
src="https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg"
style="width: 500px; height: 120px;" />

    Input: root = [2,1,3]
    Output: [2,3,1]

**Example 3:**

    Input: root = []
    Output: []

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

```python
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(lst: list[int]) -> Optional[TreeNode]:
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while i < len(lst):
        current = queue.popleft()

        current.left = TreeNode(lst[i])
        queue.append(current.left)
        i += 1

        if i < len(lst):
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:

    result: list[Optional[int]] = []
    queue: deque[Optional[TreeNode]] = deque([root])

    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result
```

#### Iterative DFS - O(n), O(n)

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]

        while stack:
            current = stack.pop()
            current.left, current.right = current.right, current.left

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return root


solution = Solution()
print(tree_to_list(solution.invertTree(list_to_tree([4, 2, 7, 1, 3, 6, 9]))))
print(tree_to_list(solution.invertTree(list_to_tree([2, 1, 3]))))
print(tree_to_list(solution.invertTree(list_to_tree([]))))
```

    [4, 7, 2, 9, 6, 3, 1]
    [2, 3, 1]
    []

#### Iterative BFS - O(n), O(n)

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root


solution = Solution()
print(tree_to_list(solution.invertTree(list_to_tree([4, 2, 7, 1, 3, 6, 9]))))
print(tree_to_list(solution.invertTree(list_to_tree([2, 1, 3]))))
print(tree_to_list(solution.invertTree(list_to_tree([]))))
```

    [4, 7, 2, 9, 6, 3, 1]
    [2, 3, 1]
    []

#### Recursive DFS - O(n), O(n)

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


solution = Solution()
print(tree_to_list(solution.invertTree(list_to_tree([4, 2, 7, 1, 3, 6, 9]))))
print(tree_to_list(solution.invertTree(list_to_tree([2, 1, 3]))))
print(tree_to_list(solution.invertTree(list_to_tree([]))))
```

    [4, 7, 2, 9, 6, 3, 1]
    [2, 3, 1]
    []

### 104. Maximum Depth of Binary Tree

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the
longest path from the root node down to the farthest leaf node.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg"
style="width: 400px; height: 277px;" />

    Input: root = [3,9,20,null,null,15,7]
    Output: 3

**Example 2:**

    Input: root = [1,null,2]
    Output: 2

**Constraints:**

- The number of nodes in the tree is in the range
    `[0, 10`<sup>`4`</sup>`]`.
- `-100 <= Node.val <= 100`

```python
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: Optional[int] = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
```

```python
def list_to_tree(lst: list[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while i < len(lst):
        current = queue.popleft()

        current.left = TreeNode(lst[i])
        queue.append(current.left)
        i += 1

        if i < len(lst):
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root
```

#### Iterative DFS - O(n), O(n)

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack: list[tuple[Optional[TreeNode], int]] = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth


solution = Solution()
print(solution.maxDepth(list_to_tree([3, 9, 20, None, None, 15, 7])))
print(solution.maxDepth(list_to_tree([1, None, 2])))
```

    3
    2

#### Iterative BFS - O(n), O(n)

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue: deque[tuple[Optional[TreeNode], int]] = deque([(root, 1)])
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            if node:
                max_depth = max(max_depth, depth)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return max_depth


solution = Solution()
print(solution.maxDepth(list_to_tree([3, 9, 20, None, None, 15, 7])))
print(solution.maxDepth(list_to_tree([1, None, 2])))
```

    3
    2

#### Recursive DFS - O(n), O(n)

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return (
            1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
        )


solution = Solution()
print(solution.maxDepth(list_to_tree([3, 9, 20, None, None, 15, 7])))
print(solution.maxDepth(list_to_tree([1, None, 2])))
```

    3
    2

### 100. Same Tree

Given the roots of two binary trees `p` and `q`, write a function to
check if they are the same or not.

Two binary trees are considered the same if they are structurally
identical, and the nodes have the same value.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg"
style="width: 622px; height: 182px;" />

    Input: p = [1,2,3], q = [1,2,3]
    Output: true

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg"
style="width: 382px; height: 182px;" />

    Input: p = [1,2], q = [1,null,2]
    Output: false

**Example 3:**

<img src="https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg"
style="width: 622px; height: 182px;" />

    Input: p = [1,2,1], q = [1,1,2]
    Output: false

**Constraints:**

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10`<sup>`4`</sup>`<= Node.val <= 10`<sup>`4`</sup>

```python
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: Optional[int] = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(lst: list[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None

    root = TreeNode(lst[0])
    stack = [root]
    i = 1

    while i < len(lst):
        current = stack.pop()

        current.left = TreeNode(lst[i])
        stack.append(current.left)
        i += 1

        if i < len(lst):
            current.right = TreeNode(lst[i])
            stack.append(current.right)
        i += 1

    return root
```

#### Iterative DFS - O(n), O(n)

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True


solution = Solution()
print(solution.isSameTree(list_to_tree([1, 2, 3]), list_to_tree([1, 2, 3])))
print(solution.isSameTree(list_to_tree([1, 2]), list_to_tree([1, None, 2])))
print(solution.isSameTree(list_to_tree([1, 2, 1]), list_to_tree([1, 1, 2])))
```

    True
    False
    False

#### Iterative BFS - O(n), O(n)

```python
from collections import deque


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            queue.append((node1.right, node2.right))
            queue.append((node1.left, node2.left))

        return True


solution = Solution()
print(solution.isSameTree(list_to_tree([1, 2, 3]), list_to_tree([1, 2, 3])))
print(solution.isSameTree(list_to_tree([1, 2]), list_to_tree([1, None, 2])))
print(solution.isSameTree(list_to_tree([1, 2, 1]), list_to_tree([1, 1, 2])))
```

    True
    False
    False

#### Recursive DFS - O(n), O(n)

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (
            p == q
            if not p or not q
            else (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        )


solution = Solution()
print(solution.isSameTree(list_to_tree([1, 2, 3]), list_to_tree([1, 2, 3])))
print(solution.isSameTree(list_to_tree([1, 2]), list_to_tree([1, None, 2])))
print(solution.isSameTree(list_to_tree([1, 2, 1]), list_to_tree([1, 1, 2])))
```

    True
    False
    False

### 572. Subtree of Another Tree

Given the roots of two binary trees `root` and `subRoot`, return `true`
if there is a subtree of `root` with the same structure and node values
of`subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in
`tree` and all of this node's descendants. The tree `tree` could also be
considered as a subtree of itself.

**Example 1:**

<img
src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg"
style="width: 532px; height: 400px;" />

    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

**Example 2:**

<img
src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg"
style="width: 502px; height: 458px;" />

    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

**Constraints:**

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range
    `[1, 1000]`.
- `-10`<sup>`4`</sup>`<= root.val <= 10`<sup>`4`</sup>
- `-10`<sup>`4`</sup>`<= subRoot.val <= 10`<sup>`4`</sup>

```python
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: Optional[int] = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(lst: list[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        node = queue.popleft()
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1

    return root
```

#### Recursive DFS - O(n), O(n)

```python
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return (
            False
            if not root
            else self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (
            p == q
            if not p or not q
            else (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        )


solution = Solution()
print(solution.isSubtree(list_to_tree(
    [3, 4, 5, 1, 2]), list_to_tree([4, 1, 2])))
print(solution.isSubtree(list_to_tree(
    [3, 4, 5, 1, 2, None, None, None, None, 0]), list_to_tree([4, 1, 2])))
```

    True
    False

### 543. Diameter of Binary Tree

Given the `root` of a binary tree, return *the length of the
**diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path
between any two nodes in a tree. This path may or may not pass through
the `root`.

The **length** of a path between two nodes is represented by the number
of edges between them.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg"
style="width: 292px; height: 302px;" />

    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

**Example 2:**

    Input: root = [1,2]
    Output: 1

**Constraints:**

- The number of nodes in the tree is in the range
    `[1, 10`<sup>`4`</sup>`]`.
- `-100 <= Node.val <= 100`

```python
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: Optional[int] = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes: list[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    if index < len(nodes) and nodes[index] is not None:
        node = TreeNode(nodes[index])
        node.left = build_tree(nodes, 2 * index + 1)
        node.right = build_tree(nodes, 2 * index + 2)
        return node
    return None
```

#### Iterative DFS - O(n), O(n)

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack: list[tuple[Optional[TreeNode], bool]] = [(root, False)]
        depth: dict[Optional[TreeNode], int] = {}
        diameter = 0

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    left_depth = depth.get(node.left, 0)
                    right_depth = depth.get(node.right, 0)
                    depth[node] = max(left_depth, right_depth) + 1
                    diameter = max(diameter, left_depth + right_depth)
                else:
                    stack.append((node, True))
                    stack.append((node.left, False))
                    stack.append((node.right, False))

        return diameter


solution = Solution()
print(solution.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])))
print(solution.diameterOfBinaryTree(build_tree([1, 2])))
```

    3
    1

#### Recursive DFS - O(n), O(n)

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def depth(node: Optional["TreeNode"]) -> int:
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)
            diameter[0] = max(diameter[0], left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        depth(root)
        return diameter[0]


solution = Solution()
print(solution.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])))
print(solution.diameterOfBinaryTree(build_tree([1, 2])))
```

    3
    1

### 110. Balanced Binary Tree

Given a binary tree, determine if it is **height-balanced**.

A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg"
style="width: 342px; height: 221px;" />

    Input: root = [3,9,20,null,null,15,7]
    Output: true

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg"
style="width: 452px; height: 301px;" />

    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

**Example 3:**

    Input: root = []
    Output: true

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10`<sup>`4`</sup>`<= Node.val <= 10`<sup>`4`</sup>

```python
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root
```

#### Recursive DFS - O(n), O(h)

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_height, right_height = dfs(node.left), dfs(node.right)
            if (
                left_height == -1
                or right_height == -1
                or abs(left_height - right_height) > 1
            ):
                return -1
            return max(left_height, right_height) + 1

        return dfs(root) != -1


solution = Solution()
print(solution.isBalanced(build_tree([3, 9, 20, None, None, 15, 7])))
print(solution.isBalanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])))
print(solution.isBalanced(build_tree([])))
```

    True
    False
    True

### 703. Kth Largest Element in a Stream

Design a class to find the `k`<sup>`th`</sup> largest element in a
stream. Note that it is the `k`<sup>`th`</sup> largest element in the
sorted order, not the `k`<sup>`th`</sup> distinct element.

Implement `KthLargest` class:

- `KthLargest(int k, int[] nums)` Initializes the object with the
    integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and
    returns the element representing the `k`<sup>`th`</sup> largest
    element in the stream.

**Example 1:**

    Input
    ["KthLargest", "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output
    [null, 4, 5, 5, 8, 8]

    Explanation
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3);   // return 4
    kthLargest.add(5);   // return 5
    kthLargest.add(10);  // return 5
    kthLargest.add(9);   // return 8
    kthLargest.add(4);   // return 8

**Constraints:**

- `1 <= k <= 10`<sup>`4`</sup>
- `0 <= nums.length <= 10`<sup>`4`</sup>
- `-10`<sup>`4`</sup>`<= nums[i] <= 10`<sup>`4`</sup>
- `-10`<sup>`4`</sup>`<= val <= 10`<sup>`4`</sup>
- At most `10`<sup>`4`</sup> calls will be made to `add`.
- It is guaranteed that there will be at least `k` elements in the
    array when you search for the `k`<sup>`th`</sup> element.

#### Sorting - O(n log n), O(n); O(n log n), O(n)

```python
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
```

    4
    5
    5
    8
    8

#### Heap - O(log k), O(k); O(n log k), O(k)

```python
import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap: list[int] = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
```

    4
    5
    5
    8
    8

### 1046. Last Stone Weight

You are given an array of integers `stones` where `stones[i]` is the
weight of the `i`<sup>`th`</sup> stone.

We are playing a game with the stones. On each turn, we choose the
**heaviest two stones** and smash them together. Suppose the heaviest
two stones have weights `x` and `y` with `x <= y`. The result of this
smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of
    weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return *the weight of the last remaining stone*. If there are no stones
left, return `0`.

**Example 1:**

    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation: 
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

**Example 2:**

    Input: stones = [1]
    Output: 1

**Constraints:**

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

#### Sorting - O(n^2), O(1)

```python
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            x = stones.pop(0)
            y = stones.pop(0)
            if x != y:
                stones.append(x - y)

        return stones[0] if stones else 0


solution = Solution()
print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(solution.lastStoneWeight([1]))
```

    1
    1

#### Heap - O(n log n), O(n)

```python
import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, x - y)

        return -stones[0] if stones else 0


solution = Solution()
print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(solution.lastStoneWeight([1]))

```

    1
    1

## Medium

### 49. Group Anagrams

Given an array of strings `strs`, group **the anagrams** together. You
can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters
exactly once.

**Example 1:**

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

**Example 2:**

    Input: strs = [""]
    Output: [[""]]

**Example 3:**

    Input: strs = ["a"]
    Output: [["a"]]

**Constraints:**

- `1 <= strs.length <= 10`<sup>`4`</sup>
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

#### Brute Force - O(n^2 * m), O(n)

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def is_anagram(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            for char in s:
                is_matched = False

                for i, c in enumerate(t):
                    if c == char:
                        t = t[:i] + t[i + 1 :]
                        is_matched = True
                        break

                if not is_matched:
                    return False

            return True

        anagram_groups: list[list[str]] = []
        used = [False] * len(strs)

        for i, str_i in enumerate(strs):
            if not used[i]:
                group = [str_i]
                used[i] = True
                for j, str_j in enumerate(strs[i + 1 :], start=i + 1):
                    if not used[j] and is_anagram(str_i, str_j):
                        group.append(str_j)
                        used[j] = True
                anagram_groups.append(group)

        return anagram_groups


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(strs=[""]))
print(solution.groupAnagrams(strs=["a"]))
```

    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    [['']]
    [['a']]

#### Arrays & Hashing - O(n *m* log(m)), O(n * m)

```python
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams: dict[str, list[str]] = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))
            anagrams[sorted_str].append(s)

        return list(anagrams.values())


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(strs=[""]))
print(solution.groupAnagrams(strs=["a"]))
```

    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    [['']]
    [['a']]

#### Using Character Count as Key - O(n *m), O(n* m)

```python
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams: dict[tuple[int, ...], list[str]] = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            anagrams[key].append(s)

        return list(anagrams.values())


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(strs=[""]))
print(solution.groupAnagrams(strs=["a"]))
```

    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    [['']]
    [['a']]

#### Using Prime Numbers - O(n *m), O(n* m)

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        prime_numbers = {
            "a": 2,
            "b": 3,
            "c": 5,
            "d": 7,
            "e": 11,
            "f": 13,
            "g": 17,
            "h": 19,
            "i": 23,
            "j": 29,
            "k": 31,
            "l": 37,
            "m": 41,
            "n": 43,
            "o": 47,
            "p": 53,
            "q": 59,
            "r": 61,
            "s": 67,
            "t": 71,
            "u": 73,
            "v": 79,
            "w": 83,
            "x": 89,
            "y": 97,
            "z": 101,
        }

        anagrams: dict[int, list[str]] = {}

        for word in strs:
            product = 1
            for char in word:
                product *= prime_numbers[char]

            if product in anagrams:
                anagrams[product].append(word)
            else:
                anagrams[product] = [word]

        return list(anagrams.values())


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(strs=[""]))
print(solution.groupAnagrams(strs=["a"]))
```

    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    [['']]
    [['a']]

### 167. Two Sum II - Input Array Is Sorted

Given a **1-indexed** array of integers `numbers` that is already
***sorted in non-decreasing order***, find two numbers such that they
add up to a specific `target` number. Let these two numbers be
`numbers[index`<sub>`1`</sub>`]` and `numbers[index`<sub>`2`</sub>`]`
where
`1 <= index`<sub>`1`</sub>`< index`<sub>`2`</sub>`<= numbers.length`.

Return *the indices of the two numbers,* `index`<sub>`1`</sub> *and*
`index`<sub>`2`</sub>*, **added by one** as an integer array*
`[index`<sub>`1`</sub>`, index`<sub>`2`</sub>`]` *of length 2.*

The tests are generated such that there is **exactly one solution**. You
**may not** use the same element twice.

Your solution must use only constant extra space.

**Example 1:**

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

**Example 2:**

    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

**Example 3:**

    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

**Constraints:**

- `2 <= numbers.length <= 3 * 10`<sup>`4`</sup>
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**.

#### Brute Force - O(n^2), O(1)

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)

        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        return []


solution = Solution()
print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
print(solution.twoSum(numbers=[2, 3, 4], target=6))
print(solution.twoSum(numbers=[-1, 0], target=-1))
```

    [1, 2]
    [1, 3]
    [1, 2]

#### Arrays & Hashing - O(n), O(n)

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        numbers_index: dict[int, int] = {}

        for index, num in enumerate(numbers):
            complement = target - num

            if complement in numbers_index:
                return [numbers_index[complement] + 1, index + 1]

            numbers_index[num] = index

        return []


solution = Solution()
print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
print(solution.twoSum(numbers=[2, 3, 4], target=6))
print(solution.twoSum(numbers=[-1, 0], target=-1))
```

    [1, 2]
    [1, 3]
    [1, 2]

#### Two Pointers - O(n), O(1)

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            if current_sum < target:
                left += 1
            else:
                right -= 1

        return []


solution = Solution()
print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
print(solution.twoSum(numbers=[2, 3, 4], target=6))
print(solution.twoSum(numbers=[-1, 0], target=-1))
```

    [1, 2]
    [1, 3]
    [1, 2]

### 15. 3Sum

Given an integer array nums, return all the triplets
`[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and
`j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

**Example 2:**

    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

**Example 3:**

    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

**Constraints:**

- `3 <= nums.length <= 3000`
- `-10`<sup>`5`</sup>`<= nums[i] <= 10`<sup>`5`</sup>

#### Brute Force - O(n^3), O(n)

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        triplets: list[list[int]] = []

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in triplets:
                            triplets.append(triplet)

        return triplets


solution = Solution()
print(solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(solution.threeSum(nums=[0, 1, 1]))
print(solution.threeSum(nums=[0, 0, 0]))
```

    [[-1, 0, 1], [-1, -1, 2]]
    []
    [[0, 0, 0]]

### 39. Combination Sum

Given an array of **distinct** integers `candidates` and a target
integer `target`, return *a list of all **unique combinations** of*
`candidates` *where the chosen numbers sum to* `target`*.* You may
return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited
number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations
that sum up to `target` is less than `150` combinations for the given
input.

**Example 1:**

    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

**Example 2:**

    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

**Example 3:**

    Input: candidates = [2], target = 1
    Output: []

**Constraints:**

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 40`

#### Backtracking - O(n^2), O(n)

```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []

        def backtrack(start: int, current: list[int], total: int) -> None:
            if total == target:
                result.append(current[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
print(solution.combinationSum([2, 3, 5], 8))
print(solution.combinationSum([2], 1))
```

    [[2, 2, 3], [7]]
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    []

## Hard

### 778. Swim in Rising Water

You are given an `n x n` integer matrix `grid` where each value
`grid[i][j]` represents the elevation at that point `(i, j)`.

The rain starts to fall. At time `t`, the depth of the water everywhere
is `t`. You can swim from a square to another 4-directionally adjacent
square if and only if the elevation of both squares individually are at
most `t`. You can swim infinite distances in zero time. Of course, you
must stay within the boundaries of the grid during your swim.

Return *the least time until you can reach the bottom right square*
`(n - 1, n - 1)` *if you start at the top left square* `(0, 0)`.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/06/29/swim1-grid.jpg"
style="width: 164px; height: 165px;" />

    Input: grid = [[0,2],[1,3]]
    Output: 3
    Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
    You cannot reach point (1, 1) until time 3.
    When the depth of water is 3, we can swim anywhere inside the grid.

**Example 2:**

<img
src="https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg"
style="width: 404px; height: 405px;" />

    Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    Explanation: The final route is shown.
    We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

**Constraints:**

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n`<sup>`2`</sup>
- Each value `grid[i][j]` is **unique**.

#### Binary Search - O(n^2 * log(n^2)), O(n^2)

```python
from collections import deque


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)

        def can_swim(t: int) -> bool:
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            queue: deque[tuple[int, int]] = deque([(0, 0)])
            visited: set[tuple[int, int]] = set()
            visited.add((0, 0))

            while queue:
                x, y = queue.popleft()
                if x == n - 1 and y == n - 1:
                    return True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < n
                        and 0 <= ny < n
                        and (nx, ny) not in visited
                        and grid[nx][ny] <= t
                    ):
                        visited.add((nx, ny))
                        queue.append((nx, ny))

            return False

        low, high = grid[0][0], max(max(row) for row in grid)

        while low < high:
            mid = (low + high) // 2
            if can_swim(mid):
                high = mid
            else:
                low = mid + 1

        return low
```
