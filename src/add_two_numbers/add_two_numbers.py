# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Initialize the result linked list with a dummy node
        head = ListNode()
        current = head  # Initialize a pointer to the current node
        carry = 0  # Initialize a variable to keep track of the carry

        # Loop until both input linked lists are empty and there is no carry left
        while (l1 != None or l2 != None or carry != 0):
            # Determine the values to add from the current nodes of l1 and l2
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            # Calculate the total value, including the carry from the previous iteration
            total = l1_value + l2_value + carry
            # Create a new node in the result linked list with the units digit of the total
            current.next = ListNode(total % 10)
            carry = total // 10  # Update the carry for the next iteration

            # Move the pointers of l1 and l2 to the next nodes, if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next  # Move the result linked list pointer to the next node

        # Return the result linked list, starting from the node after the dummy node
        return head.next
