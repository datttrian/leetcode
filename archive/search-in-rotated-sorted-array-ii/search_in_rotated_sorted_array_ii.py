class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the mid element is equal to the target
            if nums[mid] == target:
                return True

            # Handle the case where there are duplicates at both ends
            while left < mid and nums[left] == nums[mid]:
                left += 1

            # Check which half is sorted and adjust the pointers accordingly
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
