import heapq
from typing import Optional, List


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next_node: 'Optional[ListNode]' = None,
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next_node


class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]],
    ) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into a single sorted linked list.

        Summary:
        ----------
        This method takes a list of k sorted linked lists and merges them into
        a single sorted linked list using a min heap.

        Description:
        ------------
        The method uses a min heap to efficiently select the smallest element
        from the heads of all k lists at each iteration. It then builds the
        result linked list by iteratively adding the smallest element from the
        heap and updating the heap with the next element from the same list.
        This process continues until all elements are merged into the final
        sorted linked list.

        Algorithm:
        -----------
        1. Initialize a min heap to store tuples (value, index, ListNode).
        2. Push the first element of each list into the heap.
        3. Create a dummy node to simplify the code.
        4. Iterate until the heap is not empty:
            a. Pop the smallest element from the heap.
            b. Create a new node with the popped value and add it to the
            result list.
            c. If the current list has a next element, push it into the heap.
        5. Return the merged sorted linked list starting from the next node of
        the dummy node.

        Parameters:
        ------------
        lists : List[Optional[ListNode]]
            A list containing k sorted linked lists. Each linked list may be
            None.

        Returns:
        ------------
        Optional[ListNode]
            The head of the merged sorted linked list. Returns None if the
            input list is empty or if all input linked lists are empty.

        Raises:
        ------------
        No specific exceptions are raised.

        Complexity:
        ------------
        - Time: O(n log k), where n is the total number of elements in all
        lists, and k is the number of input lists.
        - Space: O(k), where k is the number of input lists, for the min heap.
        """
        # Initialize a min heap to store tuples (value, index, ListNode)
        heap: List[tuple[int, int, ListNode]] = []

        # Push the first element of each list into the heap
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        # Create a dummy node to simplify the code
        dummy = ListNode()
        current = dummy

        # Continue until the heap is not empty
        while heap:
            # Pop the smallest element from the heap
            val, i, node = heapq.heappop(heap)

            # Create a new node with the popped value and add it to the result
            # list
            current.next = ListNode(val)
            current = current.next

            # If the current list still has elements, push the next element
            # into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        # Return the merged sorted list
        return dummy.next
