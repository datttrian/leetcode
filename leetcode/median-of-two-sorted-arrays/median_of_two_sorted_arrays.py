class Solution:
    def findMedianSortedArrays(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> float:
        """
        Find the median of two sorted arrays.

        Parameters:
        - nums1 (list[int]): The first sorted array.
        - nums2 (list[int]): The second sorted array.

        Returns:
        - float: The median of the combined sorted arrays.

        Raises:
        - None: No specific exceptions are raised by this function.
        """
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        total_length = len(A) + len(B)
        half_point = total_length // 2

        left_index, right_index = 0, len(A) - 1

        while True:
            i = (left_index + right_index) // 2
            j = half_point - i - 2

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i + 1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if (j + 1) < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if total_length % 2:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            if Aleft > Bright:
                right_index = i - 1

            else:
                left_index = i + 1
