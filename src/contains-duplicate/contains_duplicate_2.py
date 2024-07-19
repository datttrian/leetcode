class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique_nums: set[int] = set()
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        return False
