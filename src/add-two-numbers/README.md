# Add Two Numbers


You are given two **non-empty** linked lists representing two
non-negative integers. The digits are stored in **reverse order**, and
each of their nodes contains a single digit. Add the two numbers and
return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except
the number 0 itself.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

    Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
        

**Example 2:**

    Input: l1 = [0], l2 = [0]
        Output: [0]
        

**Example 3:**

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]
        

 

**Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have
  leading zeros.

# Intuition
The problem involves adding two numbers represented as linked lists, where each node in the lists contains a single digit, and the digits are stored in reverse order. The approach is to iterate through both linked lists, adding corresponding digits along with any carry from the previous iteration. A dummy head node simplifies the handling of the edge case where a new digit is added. The loop continues until both lists are exhausted, and there is no remaining carry.

# Approach
1. Initialize a dummy head node (`head`) to simplify cases requiring a new node.
2. Start with the current node (`current`) pointing to the dummy head.
3. Initialize carry to zero.
4. Loop until both input lists (`l1` and `l2`) are exhausted, and there is no carry.
   - Extract values from the current nodes of the lists (default to 0 if the node is None).
   - Calculate the new carry and digit using the sum of values and the carry from the previous iteration.
   - Append the new digit to the result list.
   - Move to the next node in the result list and the input lists.
5. Return the sum list, which is next to the dummy head.

# Complexity
- Time complexity: O(max(n, m)), where n and m are the number of nodes in the first and second linked lists. The function iterates through both lists.
- Space complexity: O(max(n, m)), as we may need to store the sum in a new linked list. The space required for the new list is at most the length of the longer input list plus one additional node for a potential carry-over.

# Code
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        head: ListNode = ListNode()
        current: ListNode = head
        carry: int = 0

        while l1 or l2 or carry:
            val1: int = l1.val if l1 else 0
            val2: int = l2.val if l2 else 0

            carry, val = divmod(val1 + val2 + carry, 10)

            current.next = ListNode(val)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
```