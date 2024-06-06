class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        nums_index = list(enumerate(numbers))
        left, right = 0, len(numbers) - 1

        while left < right:
            sum = nums_index[left][1] + nums_index[right][1]
            if sum == target:
                return [nums_index[left][0] + 1, nums_index[right][0] + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return []


solution = Solution()
print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
print(solution.twoSum(numbers=[2, 3, 4], target=6))
print(solution.twoSum(numbers=[-1, 0], target=-1))
