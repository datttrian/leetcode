# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy node as the head of the result linked list.
        head = ListNode()
        # Create a pointer 'current' to keep track of the current node in the result list.
        current = head
        # Initialize a carry variable to store any carry-over from adding digits.
        carry = 0

        # Continue looping as long as there are digits left in either l1, l2, or there's a carry-over.
        while l1 is not None or l2 is not None or carry != 0:
            # Get the values of the current nodes in l1 and l2 (or 0 if they are None).
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            # Calculate the total sum of the current digits from l1, l2, and any carry-over.
            total = l1_value + l2_value + carry
            # Calculate the digit to be stored in the current node of the result list.
            current.next = ListNode(total % 10)
            # Update the carry with the value to be carried over (0 or 1).
            carry = total // 10
            # Move the l1 and l2 pointers forward if they are not None.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # Move the current pointer to the next node in the result list.
            current = current.next

        # Return the result list starting from the first non-dummy node.
        return head.next
