class Solution:
    def findMedianSortedArrays(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> float:
        # pylint: disable=C0103
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        total_length = len(A) + len(B)
        half_point = total_length // 2

        left_index, right_index = 0, len(A) - 1

        while True:
            i = (left_index + right_index) // 2
            j = half_point - i - 2

            a_left = A[i] if i >= 0 else float("-infinity")
            a_right = A[i + 1] if (i + 1) < len(A) else float("infinity")
            b_left = B[j] if j >= 0 else float("-infinity")
            b_right = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total_length % 2:
                    return min(a_right, b_right)

                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            if a_left > b_right:
                right_index = i - 1

            else:
                left_index = i + 1
