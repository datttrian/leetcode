class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
