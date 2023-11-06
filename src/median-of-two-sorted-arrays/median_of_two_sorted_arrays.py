from typing import List


class Solution:
    def findMedianSortedArrays(self, a, b):
        """
        Finds the median of two sorted arrays.
        
        The overall run time complexity should be O(log (m+n)) where m and n are the lengths of the arrays.
        This method finds the median by utilizing a helper function to find the kth smallest element in the
        union of both arrays.
        
        Args:
        a (List[int]): The first sorted array.
        b (List[int]): The second sorted array.
        
        Returns:
        float: The median of the two sorted arrays. Returns None if both arrays are empty.
        
        The function handles both even and odd total lengths by computing the middle index according to
        whether the total length `l` is odd or even.
        """
        l = len(a) + len(b)

        if l == 0:  # Edge case where both arrays are empty.
            return None
        if l % 2:  # If the total length is odd, return the middle element.
            return self.get_median(a, b, l // 2)
        else:  # If the total length is even, return the average of the two middle elements.
            return (self.get_median(a, b, l // 2) + self.get_median(a, b, l // 2 - 1)) / 2

    def get_median(self, a, b, idx):
        """
        Helper function to find the value at index `idx` in the sorted array formed by merging `a` and `b`.
        
        Args:
        a (List[int]): The first sorted array, which can become empty as the recursion progresses.
        b (List[int]): The second sorted array, which can become empty as the recursion progresses.
        idx (int): The index for which we want to find the value in the merged array.
        
        Returns:
        int: The value at index `idx` in the merged sorted array.
        
        This function works by comparing middle elements of `a` and `b` and recursively calling itself on
        a subarray that must contain the kth smallest element.
        """
        if not a:  # If `a` is empty, return the element at `idx` from `b`.
            return b[idx]
        if not b:  # If `b` is empty, return the element at `idx` from `a`.
            return a[idx]

        ai = len(a) // 2
        bi = len(b) // 2
        ma = a[ai]
        mb = b[bi]

        # Ensure ma is the smaller median to proceed with the logic
        if ma > mb:
            a, b = b, a  # Swap arrays
            ai, bi = bi, ai  # Swap indices

        max_idx_ma = ai + bi  # The maximum index `ma` could be at in the merged array

        # If `idx` is greater than `max_idx_ma`, we know the kth element is not in the first `ai` elements of `a`.
        if max_idx_ma < idx:
            return self.get_median(a[ai + 1:], b, idx - (ai + 1))
        else:
            # Otherwise, the kth element is not in the elements after `bi` in `b`.
            return self.get_median(a, b[:bi], idx)

# Note: The function assumes that the arrays are sorted in non-decreasing order.
