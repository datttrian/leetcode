class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_unique: set[int] = set()
        for num in nums:
            if num in nums_unique:
                return True
            nums_unique.add(num)
        return False


solution = Solution()
print(solution.containsDuplicate(nums=[1, 2, 3, 1]))
print(solution.containsDuplicate(nums=[1, 2, 3, 4]))
print(solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
