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
        # Make sure A is the smaller array to apply binary search on it.
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        total_length = len(A) + len(B)
        half_point = total_length // 2

        left_index, right_index = 0, len(A) - 1
        while True:
            i = (left_index + right_index) // 2  # Index in A
            j = half_point - i - 2  # Corresponding index in B

            # Calculate partition values, taking care of edges
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i + 1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if (j + 1) < len(B) else float('infinity')

            # Check if the partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Return the middle value for odd total length
                if total_length % 2:
                    return min(Aright, Bright)
                # Return average of two middle values for even total length
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right_index = i - 1  # Move left in A
            else:
                left_index = i + 1  # Move right in A
