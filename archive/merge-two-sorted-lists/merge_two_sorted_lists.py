from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next_node: 'Optional[ListNode]' = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next_node


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into a single sorted linked list.

        Summary:
        Combines two sorted linked lists into one while maintaining the sorted
        order.

        Description:
        Given two sorted linked lists, this method merges them into a new
        linked list in sorted order.
        The resulting linked list contains all the nodes from both input lists.

        Algorithm:
        The function uses a dummy node to simplify the code and keep track of
        the merged list.
        It iterates through the input lists, comparing the values of the
        current nodes in list1 and list2.
        The smaller value is appended to the merged list, and the
        corresponding pointer is moved to the next node.
        This process continues until one of the input lists becomes empty. Any
        remaining nodes in the non-empty list
        are then appended to the merged list.

        Parameters:
        - list1 (Optional[ListNode]): The head of the first sorted linked list.
        - list2 (Optional[ListNode]): The head of the second sorted linked
        list.

        Returns:
        Optional[ListNode]: The head of the merged sorted linked list.

        Raises:
        No specific exceptions are raised.

        Complexity:
        Time: O(m + n), where m and n are the lengths of the input lists.
        Space: O(1), as the function uses a constant amount of extra space
        regardless of the input sizes.
        """
        # Create a dummy node to simplify the code and keep track of the
        # merged list
        dummy = ListNode()
        # Initialize a pointer to the current node in the merged list
        current = dummy

        # Iterate until either list1 or list2 becomes empty
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2
            if list1.val < list2.val:
                # If the value in list1 is smaller, append it to the merged
                # list
                current.next = list1
                # Move the pointer in list1 to the next node
                list1 = list1.next
            else:
                # If the value in list2 is smaller or equal, append it to the
                # merged list
                current.next = list2
                # Move the pointer in list2 to the next node
                list2 = list2.next

            # Move the pointer in the merged list to the newly appended node
            current = current.next

        # If one of the lists is not empty, append the remaining nodes to the
        # merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # The merged list starts from the next of the dummy node
        return dummy.next
