from typing import List


class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> float:
        """
        Find the median of two sorted arrays.

        This function takes two sorted arrays and finds their median as if
        they were part of the same sorted array. It uses a binary search
        algorithm to find the correct partition between the arrays that would
        form a merged sorted array, and calculates the median from the
        elements around the partition.

        Args:
            nums1 (List[int]): The first sorted array.
            nums2 (List[int]): The second sorted array.

        Returns:
            float: The median of the two sorted arrays.

        Complexity:
            Time: O(log(min(m, n))), because the binary search is performed on
            the smaller array.
            Space: O(1), as the solution uses constant extra space.
        """
        # Assign nums1 and nums2 to A and B with A being the smaller array
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        # Calculate the total length of both arrays and the middle index
        total_length = len(A) + len(B)
        half_point = total_length // 2

        # Initialize the binary search on the smaller array A
        left_index, right_index = 0, len(A) - 1

        # Perform a binary search to find the correct partition
        while True:
            # Find the index i in array A such that it is approximately the
            # median
            i = (left_index + right_index) // 2  # index in A
            # Find the corresponding index j in array B using the half_point
            j = half_point - i - 2  # index in B

            # Determine the edge values around the partition to compare, with
            # -infinity and +infinity as defaults for out-of-bound indices
            Aleft = (
                A[i] if i >= 0 else float('-infinity')
            )  # Left partition of A
            Aright = (
                A[i + 1] if (i + 1) < len(A) else float('infinity')
            )  # Right partition of A
            Bleft = (
                B[j] if j >= 0 else float('-infinity')
            )  # Left partition of B
            Bright = (
                B[j + 1] if (j + 1) < len(B) else float('infinity')
            )  # Right partition of B

            # Check if we have found a valid partition
            if Aleft <= Bright and Bleft <= Aright:
                # For odd total length, the median is the first middle element
                if total_length % 2:
                    return min(Aright, Bright)
                # For even total length, the median is the average of the two
                # middle elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # If elements on the left side of A are greater, move the
            # partition left
            elif Aleft > Bright:
                right_index = i - 1  # Move partition left in A
            # If elements on the left side of B are greater, move the
            # partition right
            else:
                left_index = i + 1  # Move partition right in A
