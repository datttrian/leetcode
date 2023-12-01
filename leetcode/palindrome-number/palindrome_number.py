from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next_node: "Optional[ListNode]" = None,
    ) -> None:
        self.value: int = val
        self.next: Optional[ListNode] = next_node


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
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
