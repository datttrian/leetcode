from typing import List, Optional


class Solution:
    def findMedianSortedArrays(
        self,
        a: List[int],
        b: List[int],
    ) -> Optional[float]:
        """
        Find the median of two sorted arrays.

        This method handles both even
        and odd total lengths by calling the helper method `get_median` which
        performs a binary search.

        The median is defined as the middle number of a sorted list of numbers
        or the average
        of the two middle numbers if the list has an even number of elements.
        This function
        handles both empty and non-empty lists, and it can return a float or
        None if the input
        lists are empty.

        Parameters:
        - a (List[int]): The first sorted list of integers.
        - b (List[int]): The second sorted list of integers.

        Returns:
        - Optional[float]: The median value as a float if the total length is
        odd, or the average of the two medians if the total length is even.
        Returns None if both input lists are empty.

        Complexity:
        - Time: O(log(min(n, m))), where n and m are the lengths of arrays a
        and b.
        - Space: O(1), since this approach only uses a constant amount of
        extra space.
        """
        l: int = len(a) + len(b)  # Total length of both arrays combined.

        if l == 0:
            return None  # Edge case: if both arrays are empty, return None.

        if l % 2:
            return self.get_median(
                a,
                b,
                l // 2,
            )  # If odd, return the middle element.
        else:
            # If even, calculate the average of the two middle elements.
            return (
                self.get_median(a, b, l // 2)
                + self.get_median(a, b, l // 2 - 1)
            ) / 2

    def get_median(self, a: List[int], b: List[int], idx: int) -> int:
        """
        Find the median of two sorted arrays using a binary search approach.

        The function is recursively called until the median is found.

        This helper method assumes that at least one of the arrays is
        non-empty and it is
        designed to be called by `findMedianSortedArrays`.

        Parameters:
        - a (List[int]): Non-empty sorted array or the relevant subarray from
        the first array.
        - b (List[int]): Non-empty sorted array or the relevant subarray from
        the second array.
        - idx (int): The index of the median to find in the merged array view.

        Returns:
        - int: The value of the median found at the specified index.

        Note:
        This method will modify the input lists `a` and `b` by slicing, which
        does not affect
        the original lists passed to `findMedianSortedArrays` due to Python's
        list slicing
        creating new lists.
        """
        # Base cases: if one of the arrays is empty, return the idx-th element
        # of the other array.
        if not a:
            return b[idx]
        if not b:
            return a[idx]

        # Find the middle indices and values of the current arrays.
        ai: int = len(a) // 2
        bi: int = len(b) // 2
        ma: int = a[ai]
        mb: int = b[bi]

        # Ensure that 'a' contains the smaller middle element to simplify the
        # logic.
        if ma > mb:
            a, b = b, a
            ai, bi = bi, ai

        # Recursively call `get_median` with adjusted arrays and index based
        # on comparison.
        max_idx_ma: int = ai + bi
        if max_idx_ma < idx:
            # If the index is in the second half, narrow down to that side.
            return self.get_median(a[ai + 1 :], b, idx - (ai + 1))
        else:
            # If the index is in the first half, narrow down to that side.
            return self.get_median(a, b[:bi], idx)
