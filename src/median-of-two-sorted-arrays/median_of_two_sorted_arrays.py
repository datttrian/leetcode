from typing import List


class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> float:
        # Make sure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m: int = len(nums1)
        n: int = len(nums2)
        imin: int = 0
        imax: int = m
        half_len: int = (m + n + 1) // 2

        while imin <= imax:
            i: int = (imin + imax) // 2
            j: int = half_len - i

            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left: int = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_of_left)

                if i == m:
                    min_of_right: int = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

        # Fallback return statement, this should logically never be reached
        # due to the nature of the problem.
        # But it's required to satisfy static type checking and ensure
        # the function signature contract (always returning a float) is met.
        return 0.0
