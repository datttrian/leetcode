Alright, let's break it down by the mentioned techniques:

1. **Arrays & Hashing:**
   - You can use a hash map to store the values of each Roman numeral. Then, iterate through the input string, adding the corresponding values to the total.

2. **Two Pointers:**
   - Not the most suitable for this problem, as it involves parsing characters one by one. Two pointers are more useful for dealing with ranges.

3. **Sliding Window:**
   - Sliding window won't be directly applicable to this problem. It's more useful for problems where you need to maintain a window of elements in an array.

4. **Stack:**
   - You can use a stack to keep track of the Roman numerals. Iterate through the string, pushing onto the stack, but if you encounter a smaller numeral after a larger one, pop the larger one and subtract its value from the total.

5. **Binary Search:**
   - Not applicable here, as Roman numerals are not in a sorted order where binary search would be useful.

6. **Linked List:**
   - Not directly applicable. Linked lists are more about dynamic data structures, not relevant for parsing characters in a sequence.

7. **Trees:**
   - Not directly applicable. Trees are more useful for hierarchical structures, not for parsing linear sequences.

8. **Tries:**
   - Similar to hashing, you can use a trie to store the Roman numerals and traverse it based on the input string.

9. **Heap / Priority Queue:**
   - Not directly applicable. Heaps are useful for maintaining the highest or lowest element in a collection, not for parsing characters.

10. **Backtracking:**
    - Backtracking is not directly applicable to this problem. It's more suitable for problems involving decisions at each step.

11. **Graphs:**
    - Not applicable. The problem doesn't involve a graph structure.

12. **Advanced Graphs:**
    - Not applicable. Similar to basic graphs, no graph structure here.

13. **1-D Dynamic Programming:**
    - Not directly applicable. Dynamic programming is more for optimizing solutions by breaking a problem into subproblems.

14. **2-D Dynamic Programming:**
    - Not directly applicable. This problem is more about parsing a sequence, not about optimal substructure.

15. **Greedy:**
    - Greedy is a good fit here. Iterate through the string, adding the value of each numeral. If a smaller numeral appears before a larger one, subtract twice the value of the smaller numeral.

16. **Intervals:**
    - Not applicable. Intervals are more relevant for problems involving ranges of values.

17. **Math & Geometry:**
    - Greedy would be the most mathematical approach for this problem. Converting Roman numerals to integers involves simple addition and subtraction based on their rules.

18. **Bit Manipulation:**
    - Not directly applicable. Bit manipulation is more suitable for binary representation and bitwise operations.

For this problem, I'd suggest focusing on the Greedy approach as it aligns well with the nature of Roman numerals.

## Arrays & Hashing

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            else:
                total += roman_values[s[i]]

        return total
        
```

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through the string once to calculate the total value.

The space complexity is O(1) because we only use a constant amount of space to store the roman_values dictionary and the total variable. The space used does not depend on the size of the input string.



## Stack

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        stack: list[int] = []

        for char in s:
            current_value = roman_dict[char]

            while stack and current_value > stack[-1]:
                result -= stack.pop()

            stack.append(current_value)

        result += sum(stack)

        return result

```

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through each character in the string once.

The space complexity is O(n) as well. In the worst case, the stack can contain all the characters in the string, resulting in a space complexity of O(n).

## Tries



## Backtracking

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        def backtrack(index, current_value):
            if index == len(s):
                return current_value

            if (
                index < len(s) - 1
                and roman_dict[s[index]] < roman_dict[s[index + 1]]
            ):
                return backtrack(
                    index + 2,
                    current_value
                    - roman_dict[s[index]]
                    + roman_dict[s[index + 1]],
                )
            else:
                return backtrack(
                    index + 1, current_value + roman_dict[s[index]]
                )

        return backtrack(0, 0)

```

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through each character in the string once.

The space complexity is O(1) because we only use a constant amount of extra space to store the roman_dict dictionary and the variables used in the backtrack function.

## Greedy



## Math & Geometry


