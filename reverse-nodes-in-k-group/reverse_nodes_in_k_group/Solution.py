class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy

        while pointer:
            node = pointer
            # First, check whether there are k nodes to reverse
            for i in range(k):
                if not node:
                    break
                node = node.next
            if not node:
                break

            # Now that we have k nodes, start from the first node
            prev, curr, next_node = None, pointer.next, None
            for i in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            tail = pointer.next
            tail.next = curr
            pointer.next = prev
            pointer = tail

        return dummy.next
