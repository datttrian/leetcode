class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            """Perform binary search on a sorted list of integers."""

            # Base case: if the left index exceeds the right index, the target is not found
            if left > right:
                return -1

            # Calculate the middle index of the current search range
            mid = (left + right) // 2

            # Return the index if the element at the middle index equal `target`
            if nums[mid] == target:
                return mid

            return (

                # Recursively search the right half if the target is greater than the mid element
                binary_search(mid + 1, right)

                # otherwise, search the left half
                if nums[mid] < target
                else binary_search(left, mid - 1)
            )

        return binary_search(0, len(nums) - 1)


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], target=9))
print(solution.search([-1, 0, 3, 5, 9, 12], target=2))
